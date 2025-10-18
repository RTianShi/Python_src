import copy
import math
from typing import List

import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4

print("test_ebeDivide 执行了")


def sum_array(arr: List[float]) -> float:
    return sum(arr) if arr is not None else 0.0


def almost_equal(a: float, b: float, delta: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=0.0, abs_tol=delta)


def applyMR_Assert(originalInput1_1: List[float], originalInput1_2: List[float], originalResult: List[float]):
    """
    originalInput1_1, originalInput1_2: List[float]
    originalResult: List[float] (element-wise result from the function)
    Assertions follow the OR rules enabled in your Java test (comparing sums).
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 乘法单位元 1
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 所有元素加0
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

    # MR19: 输入重复（元素复制）将元素 a 重复多次插入序列中
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

    # ---------------- Assertions (对应 Java 中启用的 OR 断言) ----------------
    orig_sum = sum_array(originalResult)

    # OR3_2: 源输出和保持或增加
    check.is_true(sum_array(transformResult3_2) >= orig_sum, "MR3_2 failed")

    # OR5: 和应该增加或保持不变
    check.is_true(sum_array(transformResult5) >= orig_sum, "MR5 failed")

    # OR7_1: 源输出数组和后续输出数组保持不变
    check.is_true(almost_equal(sum_array(transformResult7_1), orig_sum), "MR7_1 failed")

    # OR7_2:
    check.is_true(almost_equal(sum_array(transformResult7_2), orig_sum), "MR7_2 failed")

    # OR8: 源输出*? -> 在 Java 中使用 increased, 用 >=
    check.is_true(sum_array(transformResult8) >= orig_sum, "MR8 failed")

    # OR10: 和应该增加或保持不变
    check.is_true(sum_array(transformResult10) >= orig_sum, "MR10 failed")

    # OR11: 源输出大于等于后续输出 (sum decreased or equal)
    check.is_true(sum_array(transformResult11) <= orig_sum, "MR11 failed")

    # OR12: 源输出大于等于后续输出
    check.is_true(sum_array(transformResult12) <= orig_sum, "MR12 failed")

    # OR22: 源输出等于后续输出
    check.is_true(almost_equal(sum_array(transformResult22), orig_sum), "MR22 failed")


@pytest.mark.parametrize("a,b", [
    ([1.5, -2.3, 3.7], [2.0, 1.1, -0.5]),
    ([-6.5, 7.5, -8.5, 9.5], [2.4, 2.6, 2.7, 2.9]),
    ([3.14, -2.71, 1.61], [-1.23, 2.34, -0.45]),
    ([-2.5, 2.5, -3.5, 4.5], [1.5, -1.0, 1.0, -0.5]),
    ([0.0, 0.0, 0.0, 0.0], [1.1, 2.2, 3.3, 4.4]),
    ([5.55, -1.55, 2.25], [-0.55, 1.55, -2.25]),
    ([4.4, 3.3], [1.1, 2.2]),
    ([3.25, -7.69, 5.48, -1.32, 6.55], [-7.29, 8.12, -9.13, 4.68, 7.23]),
    ([6.57, 4.32, 4.98], [6.70, 8.25, 9.47]),
    ([5.13, -1.25, 0.0, 4.36], [-6.21, 7.31, 4.55, 2.12]),
])
def test_ebeDivide_with_func(a, b):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    in1 = copy.deepcopy(a)
    in2 = copy.deepcopy(b)
    originalResult = func(in1, in2)
    applyMR_Assert(in1, in2, originalResult)
