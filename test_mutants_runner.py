import os
import importlib.util
import inspect
import mutants.runner as runner
import pytest
import sys
from datetime import datetime
import traceback
import re

# 供 tests 手动导入使用
CURRENT_MUTANT_FUNC = None
# 在脚本顶部靠近 import 的地方添加或修改这个变量：
DEFAULT_LOG_NAME = "add_values.log"   # <- 在这里修改为你想要的默认日志名（例如 "mylog.txt"）

# ---------- 日志相关：把 stdout/stderr 同时写到多个流上（file 和 原始终端） ----------
_ansi_re = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def strip_ansi(s: str) -> str:
    """移除常见的 ANSI 控制序列"""
    # 如果传入非 str（例如 bytes），先尝试 decode
    try:
        return _ansi_re.sub("", s)
    except Exception:
        return s

class Tee:
    """
    将输出同时写到多个流：
    - primary（第一个流）收到原始数据（保留颜色），
    - 其它流收到 strip_ansi(data)（去掉颜色码）
    其它方法/属性代理给 primary，兼容 isatty/fileno/encoding 等。
    """
    def __init__(self, *streams):
        if not streams:
            raise ValueError("Tee needs at least one stream")
        self.streams = streams
        self.primary = streams[0]

    def write(self, data):
        # data 通常是 str
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
    # remove potentially problematic chars for filenames
    return re.sub(r'[^\w\-_\.() ]', '_', name)

def make_unique_path(dirpath: str, desired_name: str) -> str:
    """
    在 dirpath 下为 desired_name 寻找一个不冲突的文件路径。
    若 desired_name 存在，则返回 name(2).ext、name(3).ext … 等第一个可用的路径。
    返回完整路径（dirpath + sep + final_name）。
    """
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

def load_function_from_file(file_path, prefix="x_add_values__mutmut_"):
    """动态加载文件里的所有 mutant 函数"""
    spec = importlib.util.spec_from_file_location("mutant_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    funcs = {}
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith(prefix):
            funcs[name] = obj
    return funcs  # 返回字典 {函数名: 函数对象}


def run_tests_for_mutant(func_name, mutant_func):
    """运行 tests 目录下的所有测试（保持原行为）"""
    runner.CURRENT_MUTANT_FUNC = mutant_func

    print(f"\n>>> 当前使用的函数: {func_name}")

    # 打印函数源码
    try:
        source = inspect.getsource(mutant_func)
        print("函数源码如下：")
        print(source)
    except OSError:
        print("⚠️ 无法获取源码")

    tests_dir = os.path.join(os.path.dirname(__file__), "mutants", "tests")
    # 运行 pytest，收集并执行 test_*.py 里的测试函数
    rc = pytest.main([tests_dir, "-q", "-s", "--tb=short"])
    if rc == 0:
        print(f"✅ {func_name} 所有测试通过")
    else:
        print(f"❌ {func_name} 存在失败 (退出码 {rc})")


def main():
    """
    主流程（直接在脚本中通过 DEFAULT_LOG_NAME 修改日志名）：
    - 在 logs/ 下创建 run_YYYYmmdd_HHMMSS/ 文件夹
    - 在该文件夹中创建单个日志文件（名字由 DEFAULT_LOG_NAME 指定，若重名自动编号）
    - 终端输出不变，同时写入日志文件
    """
    # 1) 创建运行目录与唯一日志文件路径
    base_logs_dir = ensure_logs_dir("logs")
    run_dir = make_run_dir(base_logs_dir, prefix="run")
    start_time = datetime.now().isoformat()

    # 写基本 run_info（不打印到终端）
    try:
        with open(os.path.join(run_dir, "run_info.txt"), "w", encoding="utf-8") as infof:
            infof.write(f"start_time: {start_time}\n")
            infof.write(f"run_dir: {run_dir}\n")
            infof.write(f"default_log_name: {DEFAULT_LOG_NAME}\n")
    except Exception:
        pass

    # 决定最终日志文件名（若重名则自动编号）
    run_log_path = make_unique_path(run_dir, DEFAULT_LOG_NAME)

    # 打开日志文件（覆盖写入，每次 run 保持干净；若想追加把 "w" 改为 "a"）
    log_f = open(run_log_path, "w", encoding="utf-8", buffering=1)

    # 2) 重定向 stdout/stderr 到 Tee(orig_terminal, log_file)
    orig_stdout = sys.__stdout__
    orig_stderr = sys.__stderr__
    sys.stdout = Tee(orig_stdout, log_f)
    sys.stderr = Tee(orig_stderr, log_f)

    try:
        # 3) 主逻辑：遍历 mutants/src 并运行（保持原有行为）
        mutants_dir = os.path.join(os.path.dirname(__file__), "mutants", "src")

        for mutant_file in sorted(os.listdir(mutants_dir)):
            if not mutant_file.endswith(".py") or mutant_file == "__init__.py":
                continue

            mutant_path = os.path.join(mutants_dir, mutant_file)
            # 这些 print 会同时出现在终端与 log（因为 stdout 被重定向）
            print(f"\n=== Running tests for {mutant_file} ===")

            spec = importlib.util.spec_from_file_location("mutant_module", mutant_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, func in inspect.getmembers(module, inspect.isfunction):
                if not name.startswith("x_add_values__mutmut"):
                    continue

                # 在 log 中写入不可见的分隔信息（不会影响终端）
                try:
                    log_f.write("\n" + "="*80 + "\n")
                    log_f.write(f"RUNNING {mutant_file} :: {name}  -  {datetime.now().isoformat()}\n")
                    log_f.write("="*80 + "\n")
                    log_f.flush()
                except Exception:
                    pass

                # 运行测试（内部 print/pytest 输出被 tee 捕获）
                run_tests_for_mutant(name, func)

    except Exception:
        # 若主流程抛出未捕获异常，也写入日志（stderr 已被重定向）
        print("UNEXPECTED ERROR IN MAIN:")
        traceback.print_exc()
    finally:
        # 4) 恢复 stdout/stderr 并关闭日志文件
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

        # 恢复到原始终端后打印日志位置（仅一行，不会改变测试输出）
        print(f"All logs for this run were saved to: {run_log_path}")

if __name__ == "__main__":
    main()
