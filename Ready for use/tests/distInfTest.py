import copy
import math
import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4

print("test_distInf 执行了")


def almost_equal(a: float, b: float, delta: float = 1e-9) -> bool:
    """浮点近似相等（允许 NaN/inf 行为按 Python 默认）"""
    try:
        return abs(a - b) <= delta
    except Exception:
        return False


def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    """
    originalInput1_1, originalInput1_2: List[float]
    originalResult: float
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)
    # OR1: Java 中被注释 — 不断言

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    print("转换后的数组应该是：", transformInput2_1)
    print("转换后的数组应该是：", transformInput2_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加入单位元不变性（加法的单位元0）
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)
    # OR4: Java 中注释 — 不断言

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 中立操作（乘1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 中立操作（加0）
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)
    # OR11: Java 中注释 — 不断言

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15: 类三角函数的周期性
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # ---------------- Assertions (按照 Java 的 OR 规则) ----------------
    delta = 1e-9
    # OR2: 源输出等于后续输出（使用 delta 比较）
    check.is_true(almost_equal(originalResult, transformResult2, delta), "MR2 failed")

    # OR3_1: 和应该保持不变 (Java 用 == 对 double，保守用 delta)
    check.is_true(almost_equal(originalResult, transformResult3_1, delta), "MR3_1 failed")

    # OR3_2:
    check.is_true(almost_equal(originalResult, transformResult3_2, delta), "MR3_2 failed")

    # OR5: 源输出和小于等于后续输出
    check.is_true(originalResult <= transformResult5, "MR5 failed")

    # OR6:
    check.is_true(almost_equal(originalResult, transformResult6, delta), "MR6 failed")

    # OR7_1:
    check.is_true(almost_equal(originalResult, transformResult7_1, delta), "MR7_1 failed")

    # OR7_2:
    check.is_true(almost_equal(originalResult, transformResult7_2, delta), "MR7_2 failed")

    # OR8:
    check.is_true(almost_equal(originalResult, transformResult8, delta), "MR8 failed")

    # OR10:
    check.is_true(almost_equal(originalResult, transformResult10, delta), "MR10 failed")

    # OR12:
    check.is_true(almost_equal(originalResult, transformResult12, delta), "MR12 failed")

    # OR13:
    check.is_true(almost_equal(originalResult, transformResult13, delta), "MR13 failed")

    # OR16:
    check.is_true(almost_equal(originalResult, transformResult16, delta), "MR16 failed")

    # OR19:
    check.is_true(almost_equal(originalResult, transformResult19, delta), "MR19 failed")

    # OR20:
    check.is_true(almost_equal(originalResult, transformResult20, delta), "MR20 failed")

    # OR22:
    check.is_true(almost_equal(originalResult, transformResult22, delta), "MR22 failed")


@pytest.mark.parametrize("input1,input2", [
    ([1.2, 5.67, -3.456], [1.1, 5.70, -3.45]),
    ([-1.25, 6.01, 7.85, 9.87], [2.41, 5.06, 6.66, 7.87]),
    ([3.14, -2.718], [3.140, -2.72]),
    ([-7.89, 1.234, 0.567], [-7.90, 1.230, 0.570]),
    ([2.3, 6.6, -5.5, 7.2], [3.4, 6.6, 7.5, 8.2]),
    ([4.5678, -3.4567, 2.3456], [4.560, -3.450, 2.340]),
    ([-1.234, 2.345, -3.456, 4.567], [-1.23, 2.34, -3.46, 4.56]),
    ([5.34, 6.78, 4.56], [5.12, 6.79, 0.46]),
    ([-3.1415, 2.71828], [-3.14, 2.72]),
    ([5.0001, 6.001, 7.01, 8.1], [8.0002, 7.002, 6.02, 5.2]),
])
def test_distInf_with_func(input1, input2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalInput1 = copy.deepcopy(input1)
    originalInput2 = copy.deepcopy(input2)
    originalResult = func(originalInput1, originalInput2)
    applyMR_Assert(originalInput1, originalInput2, originalResult)
