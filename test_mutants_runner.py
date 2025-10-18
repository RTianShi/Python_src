import os
import importlib.util
import inspect
import mutants.runner as runner
import pytest
import sys
from datetime import datetime
import traceback
import re

# 统一变量：目标函数名
TARGET_NAME = "count_k"

# 由目标名自动生成相关文件路径和前缀
MUTANT_FILE = f"{TARGET_NAME}.py"                     # mutants/src/ 下的突变体文件
TEST_FILE = f"{TARGET_NAME}Test.py"                  # mutants/tests/ 下的测试文件
MUTANT_PREFIX = f"x_{TARGET_NAME}__mutmut"            # 突变体函数名前缀
DEFAULT_LOG_NAME = f"{TARGET_NAME}.log"               # 默认日志文件名


# 供 tests 手动导入使用
CURRENT_MUTANT_FUNC = None

# ---------- 日志相关：把 stdout/stderr 同时写到多个流上（file 和 原始终端） ----------
_ansi_re = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def strip_ansi(s: str) -> str:
    """移除常见的 ANSI 控制序列"""
    try:
        return _ansi_re.sub("", s)
    except Exception:
        return s

class Tee:
    def __init__(self, *streams):
        if not streams:
            raise ValueError("Tee needs at least one stream")
        self.streams = streams
        self.primary = streams[0]

    def write(self, data):
        for s in self.streams:
            try:
                out = data if s is self.primary else strip_ansi(data)
                s.write(out)
            except Exception:
                pass

    def flush(self):
        for s in self.streams:
            try:
                s.flush()
            except Exception:
                pass

    def writelines(self, lines):
        for s in self.streams:
            try:
                if s is self.primary:
                    s.writelines(lines)
                else:
                    s.writelines([strip_ansi(l) for l in lines])
            except Exception:
                pass

    def isatty(self):
        try:
            return getattr(self.primary, "isatty", lambda: False)()
        except Exception:
            return False

    def fileno(self):
        try:
            return self.primary.fileno()
        except Exception:
            raise OSError("fileno() not supported")

    @property
    def encoding(self):
        return getattr(self.primary, "encoding", "utf-8")

    def readable(self):
        return getattr(self.primary, "readable", lambda: False)()

    def writable(self):
        return getattr(self.primary, "writable", lambda: True)()

    def __getattr__(self, name):
        return getattr(self.primary, name)

def ensure_logs_dir(path="logs"):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path

def make_run_dir(base_logs_dir="logs", prefix="run"):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(base_logs_dir, f"{prefix}_{ts}")
    os.makedirs(run_dir, exist_ok=True)
    return run_dir

def sanitize_filename(name):
    return re.sub(r'[^\w\-_\.() ]', '_', name)

def make_unique_path(dirpath: str, desired_name: str) -> str:
    base, ext = os.path.splitext(desired_name)
    if not base and ext:
        base = ext
        ext = ""
    candidate = os.path.join(dirpath, desired_name)
    if not os.path.exists(candidate):
        return candidate

    i = 2
    while True:
        new_name = f"{base}({i}){ext}"
        candidate = os.path.join(dirpath, new_name)
        if not os.path.exists(candidate):
            return candidate
        i += 1

# ---------------------------------------------------------------------------
def load_function_from_file(file_path, prefix):
    """
    动态加载文件里的函数，只返回以 prefix 开头的函数。
    返回字典 {函数名: 函数对象}
    """
    spec = importlib.util.spec_from_file_location("mutant_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    funcs = {}
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith(prefix):
            funcs[name] = obj
    return funcs

def run_tests_for_mutant(func_name, mutant_func, tests_path):
    """运行指定测试文件（tests_path）"""
    runner.CURRENT_MUTANT_FUNC = mutant_func

    print(f"\n>>> 当前使用的函数: {func_name}")

    # 打印函数源码（便于调试）
    try:
        source = inspect.getsource(mutant_func)
        print("函数源码如下：")
        print(source)
    except OSError:
        print("⚠️ 无法获取源码")

    # 运行 pytest 指定的测试文件
    rc = pytest.main([tests_path, "-q", "-s", "--tb=short"])
    if rc == 0:
        print(f"✅ {func_name} 所有测试通过")
    else:
        print(f"❌ {func_name} 存在失败 (退出码 {rc})")

def main():
    base_logs_dir = ensure_logs_dir("logs")
    run_dir = make_run_dir(base_logs_dir, prefix="run")
    start_time = datetime.now().isoformat()

    try:
        with open(os.path.join(run_dir, "run_info.txt"), "w", encoding="utf-8") as infof:
            infof.write(f"start_time: {start_time}\n")
            infof.write(f"run_dir: {run_dir}\n")
            infof.write(f"default_log_name: {DEFAULT_LOG_NAME}\n")
            infof.write(f"mutant_file: {MUTANT_FILE}\n")
            infof.write(f"test_file: {TEST_FILE}\n")
            infof.write(f"mutant_prefix: {MUTANT_PREFIX}\n")
    except Exception:
        pass

    run_log_path = make_unique_path(run_dir, DEFAULT_LOG_NAME)
    log_f = open(run_log_path, "w", encoding="utf-8", buffering=1)

    orig_stdout = sys.__stdout__
    orig_stderr = sys.__stderr__
    sys.stdout = Tee(orig_stdout, log_f)
    sys.stderr = Tee(orig_stderr, log_f)

    try:
        mutants_dir = os.path.join(os.path.dirname(__file__), "mutants", "src")
        tests_dir = os.path.join(os.path.dirname(__file__), "mutants", "tests")

        mutant_path = os.path.join(mutants_dir, MUTANT_FILE)
        test_path = os.path.join(tests_dir, TEST_FILE)

        if not os.path.exists(mutant_path):
            print(f"错误：突变体文件不存在：{mutant_path}")
            return

        if not os.path.exists(test_path):
            print(f"错误：测试文件不存在：{test_path}")
            return

        print(f"\n=== Running tests for single mutant file: {MUTANT_FILE} ===")

        # 加载并仅筛选以 MUTANT_PREFIX 开头的函数（确保行为与之前程序一致）
        funcs = load_function_from_file(mutant_path, prefix=MUTANT_PREFIX)

        if not funcs:
            print("⚠️ 在突变体文件中未找到以指定前缀开头的函数。")
            print(f"（已按前缀筛选：{MUTANT_PREFIX}）")
            return

        # 逐个函数运行测试
        for name, func in funcs.items():
            try:
                # 在 log 中写入不可见的分隔信息（不会影响终端）
                try:
                    log_f.write("\n" + "="*80 + "\n")
                    log_f.write(f"RUNNING {MUTANT_FILE} :: {name}  -  {datetime.now().isoformat()}\n")
                    log_f.write("="*80 + "\n")
                    log_f.flush()
                except Exception:
                    pass

                run_tests_for_mutant(name, func, test_path)

            except Exception:
                print(f"Error while running tests for {name}:")
                traceback.print_exc()

    except Exception:
        print("UNEXPECTED ERROR IN MAIN:")
        traceback.print_exc()
    finally:
        try:
            sys.stdout = orig_stdout
            sys.stderr = orig_stderr
        except Exception:
            pass

        end_time = datetime.now().isoformat()
        try:
            with open(os.path.join(run_dir, "run_info.txt"), "a", encoding="utf-8") as infof:
                infof.write(f"end_time: {end_time}\n")
                infof.write(f"final_log_path: {run_log_path}\n")
        except Exception:
            pass

        try:
            log_f.close()
        except Exception:
            pass

        print(f"All logs for this run were saved to: {run_log_path}")

if __name__ == "__main__":
    main()
