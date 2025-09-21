import sys
from pathlib import Path

# 添加 src 路径
ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "mutants/src"
TESTS_DIR = ROOT / "mutants/tests"
sys.path.insert(0, str(SRC_DIR))
sys.path.insert(0, str(TESTS_DIR))

from add_values import x_add_values__mutmut_orig
from test_add_values import test_add_values


def main():
    print("开始调用 add_values 函数...")

    # 手动调用一次
    """data = [1, 2, 3]
    result = x_add_values__mutmut_orig(data)
    print(f"调用 add_values({data}) = {result}")

    # 简单断言测试
    assert result == 6, f"预期 6，但得到 {result}"
    print("✅ 测试通过！")
"""
    try:
        test_add_values([1, 2, 3])
        print("✅ applyMR_Assert 测试通过！")
    except AssertionError as e:
        print(f"❌ applyMR_Assert 测试失败: {e}")


if __name__ == "__main__":
    main()
