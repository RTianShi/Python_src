import os
import sys
import importlib.util
import inspect
import traceback

# 供 tests 手动导入使用
CURRENT_MUTANT_FUNC = None

def load_function_from_file(file_path, prefix="x_add_values__mutmut_"):
    """动态加载文件里的所有 mutant 函数"""
    spec = importlib.util.spec_from_file_location("mutant_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    funcs = {}
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith(prefix):
            funcs[name] = obj
    return funcs   # 返回字典 {函数名: 函数对象}


def run_tests_for_mutant(func_name,mutant_func):
    """运行 tests 目录下的所有测试"""
    global CURRENT_MUTANT_FUNC
    CURRENT_MUTANT_FUNC = mutant_func  # 注入给 tests 使用

    print(f"\n>>> 当前使用的函数: {func_name}")

    # 打印函数源码
    try:
        source = inspect.getsource(mutant_func)
        print("函数源码如下：")
        print(source)
    except OSError:
        print("⚠️ 无法获取源码")

    tests_dir = os.path.join(os.path.dirname(__file__), "mutants", "tests")
    for test_file in os.listdir(tests_dir):
        if test_file.startswith("test_") and test_file.endswith(".py"):
            test_path = os.path.join(tests_dir, test_file)
            spec = importlib.util.spec_from_file_location(
                test_file[:-3], test_path
            )
            module = importlib.util.module_from_spec(spec)

            try:
                spec.loader.exec_module(module)
                print(f"✅ {func_name} 在 {test_file} 通过")
            except AssertionError as e:
                print(f"❌ {func_name} 在 {test_file} 失败: {e}")
            except Exception as e:
                print(f"💥 {func_name} 在 {test_file} 报错: {e}")

def main():
    # mutants/src 目录下的所有 mutant 文件
    mutants_dir = os.path.join(os.path.dirname(__file__), "mutants", "src")

    for mutant_file in os.listdir(mutants_dir):
        if mutant_file.endswith(".py") and mutant_file != "__init__.py":
            mutant_path = os.path.join(mutants_dir, mutant_file)
            print(f"\n=== Running tests for {mutant_file} ===")

            # 动态加载模块
            spec = importlib.util.spec_from_file_location("mutant_module", mutant_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 遍历所有 mutant 函数
            for name, func in inspect.getmembers(module, inspect.isfunction):
                if name.startswith("x_add_values__mutmut"):
                    print(f"\n--- Running tests for {name} ---")
                    run_tests_for_mutant(name, func)

if __name__ == "__main__":
    main()
