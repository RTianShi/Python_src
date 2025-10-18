# mutants/tests/test_entropy_py2_style.py
import copy
from typing import List

import pytest
import pytest_check as check
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4

print("test_entropy_py2_style 执行中")

# tolerance for float comparisons to mimic Java's assertEquals with delta
TOL = 1e-4


def almost_equal(a: float, b: float, tol: float = TOL) -> bool:
    if a is None or b is None:
        return False
    return abs(a - b) <= tol


def applyMR_Assert(originalInput: List[float], originalResult: float):
    """
    按照 Java 测试中启用的 OR 断言，用 pytest-check 做断言收集。
    这里只实现 Java 中未被注释掉（启用）的那些断言：
      OR1 (MR1), OR3_1 (MR3_1), OR3_2 (MR3_2), OR5 (MR5),
      OR6 (MR6), OR7_1/MR7_2, OR8 (MR8), OR13 (MR13), OR22 (MR22)
    """
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected into runner.CURRENT_MUTANT_FUNC")
    if func is None:
        return

    # MR1: 元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput)
    transformResult1 = func(copy.deepcopy(transformInput1))

    # MR2: 元素常数加法
    transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput)
    transformResult2 = func(copy.deepcopy(transformInput2))

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = func(copy.deepcopy(transformInput3_1))

    # MR3_2: 乘法单位元1
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput)
    transformResult3_2 = func(copy.deepcopy(transformInput3_2))

    # MR4: 取倒数
    transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput)
    transformResult4 = func(copy.deepcopy(transformInput4))

    # MR5: 缩放（scale=2）
    transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2)
    transformResult5 = func(copy.deepcopy(transformInput5))

    # MR6: 反转
    transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput)
    transformResult6 = func(copy.deepcopy(transformInput6))

    # MR7_1: 乘以1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(copy.deepcopy(transformInput7_1))

    # MR7_2: 加0
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = func(copy.deepcopy(transformInput7_2))

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput)
    transformResult8 = func(copy.deepcopy(transformInput8))

    # MR9: 复合转换一致性 (生成但 Java 未对 MR9 断言启用)
    transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3)
    transformResult9 = func(copy.deepcopy(transformInput9))

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput)
    transformResult10 = func(copy.deepcopy(transformInput10))

    # MR11: 边界值替换（把最大值替换为0）
    transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput)
    transformResult11 = func(copy.deepcopy(transformInput11))

    # MR12: 取反
    transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput)
    transformResult12 = func(copy.deepcopy(transformInput12))

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput)
    transformResult13 = func(copy.deepcopy(transformInput13))

    # MR14: 移除元素（移除最大值）
    transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput)
    transformResult14 = func(copy.deepcopy(transformInput14))

    # MR16: 复制某个元素
    transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput)
    transformResult16 = func(copy.deepcopy(transformInput16))

    # MR19: 插入重复元素
    transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2)
    transformResult19 = func(copy.deepcopy(transformInput19))

    # MR20: 给最小值增加极小值
    transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput)
    transformResult20 = func(copy.deepcopy(transformInput20))

    # MR22: 恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(copy.deepcopy(transformInput22))

    # ---------------- Assertions (对应 Java 中启用的断言) ----------------
    # OR1: MR1 应该保持不变（使用近似比较）
    check.is_true(almost_equal(originalResult, transformResult1),
                  f"OR1 failed: original={originalResult}, MR1={transformResult1}")

    # OR3_1: MR3_1: Java 里写的是 originalResult <= transformResult3_1
    check.is_true(originalResult <= transformResult3_1,
                  f"OR3_1 failed: original={originalResult}, MR3_1={transformResult3_1}")

    # OR3_2: MR3_2: Java 里写的是 originalResult <= transformResult3_2
    check.is_true(originalResult <= transformResult3_2,
                  f"OR3_2 failed: original={originalResult}, MR3_2={transformResult3_2}")

    # OR5: MR5: Java 里写的是 originalResult <= transformResult5
    check.is_true(originalResult <= transformResult5,
                  f"OR5 failed: original={originalResult}, MR5={transformResult5}")

    # OR6: MR6: equals
    check.is_true(almost_equal(originalResult, transformResult6),
                  f"OR6 failed: original={originalResult}, MR6={transformResult6}")

    # OR7_1 / OR7_2: equals
    check.is_true(almost_equal(originalResult, transformResult7_1),
                  f"OR7_1 failed: original={originalResult}, MR7_1={transformResult7_1}")
    check.is_true(almost_equal(originalResult, transformResult7_2),
                  f"OR7_2 failed: original={originalResult}, MR7_2={transformResult7_2}")

    # OR8: originalResult <= transformResult8
    check.is_true(originalResult <= transformResult8,
                  f"OR8 failed: original={originalResult}, MR8={transformResult8}")

    # OR13: originalResult <= transformResult13
    check.is_true(originalResult <= transformResult13,
                  f"OR13 failed: original={originalResult}, MR13={transformResult13}")

    # OR22: equality
    check.is_true(almost_equal(originalResult, transformResult22),
                  f"OR22 failed: original={originalResult}, MR22={transformResult22}")

    # 注：Java 测试中其它 OR（例如 OR2、OR4、OR9、OR10、OR11、OR12、OR14、OR16、OR19、OR20）
    # 在 Java 源中被注释掉或没有启用断言，因此这里不把它们作为必须断言。
    # 如果你希望把这些也全部启用并用更精确的关系映射（例如按元素或其它数学关系），告诉我我会加上。


# 参数化测试用例（与 Java 中的 10 个 testCase 对应）
@pytest.mark.parametrize("originalInput", [
    [1.2, 3.45, 6.789],
    [7.38, 6.59, 4.44],
    [0.25, 1.69, 4.38, 5.12],
    [7.001, 3.14, 2.22],
    [5.04, 7.23, 6.14, 5.55],
    [7.66, 2.13, 4.06, 8.15],
    [5.65, 9.86],
    [100.56, 200.34, 400.56],
    [5.69, 7.69, 8.69],
    [5.16, 7.95, 7.33],
])
def test_entropy_with_func(originalInput):
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected")
    if func is None:
        return

    in_copy = copy.deepcopy(originalInput)
    # 调用被测函数，得到原始输出
    originalResult = func(in_copy)
    applyMR_Assert(in_copy, originalResult)
