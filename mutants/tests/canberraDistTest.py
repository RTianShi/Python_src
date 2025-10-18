# test_canberraDist.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check
import math
from typing import List

delta = 1e-9  # floating-point tolerance (matches Java delta)

def is_close(a: float, b: float, tol: float = delta) -> bool:
    return math.isclose(a, b, abs_tol=tol)

def applyMR_Assert(originalInput1_1: List[float], originalInput1_2: List[float], originalResult: float):
    """
    originalInput1_1, originalInput1_2: list[float]
    originalResult: float (output of func)
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14
    transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # ---------------- Assertions ----------------
    # Use math.isclose for equal-with-delta, and check.is_true for relational asserts.

    # OR3_1: 和应该保持不变
    check.is_true(is_close(originalResult, transformResult3_1), "OR3_1 failed (MR3_1)")

    # OR3_2: 和应该保持不变
    check.is_true(is_close(originalResult, transformResult3_2), "OR3_2 failed (MR3_2)")

    # OR5: 源输出和等于后续输出
    check.is_true(is_close(originalResult, transformResult5), "OR5 failed (MR5)")

    # OR6: 用 delta 比较 transformResult6
    check.is_true(is_close(originalResult, transformResult6), "OR6 failed (MR6)")

    # OR7_1
    check.is_true(is_close(originalResult, transformResult7_1), "OR7_1 failed (MR7_1)")

    # OR7_2
    check.is_true(is_close(originalResult, transformResult7_2), "OR7_2 failed (MR7_2)")

    # OR8: 源输出小于后续输出
    check.is_true(originalResult <= transformResult8, "OR8 failed (MR8)")

    # OR11: 源输出大于等于后续输出
    check.is_true(originalResult >= transformResult11, "OR11 failed (MR11)")

    # OR12: 数组等价（这里为标量相等）
    check.is_true(is_close(originalResult, transformResult12), "OR12 failed (MR12)")

    # OR13
    check.is_true(originalResult >= transformResult13, "OR13 failed (MR13)")

    # OR14
    check.is_true(originalResult >= transformResult14, "OR14 failed (MR14)")

    # OR16
    check.is_true(originalResult <= transformResult16, "OR16 failed (MR16)")

    # OR19
    check.is_true(originalResult <= transformResult19, "OR19 failed (MR19)")

    # OR22
    check.is_true(is_close(originalResult, transformResult22), "OR22 failed (MR22)")

@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.0, 2.0, 3.0], [1.0, 4.0, 9.0]),
    ([0.0, 1.0, 2.0, 3.0], [0.0, 1.0, 4.0, 9.0]),
    ([-1.0, 0.0, 1.0], [1.0, 0.0, 2.0]),
    ([2.5, 4.0, 6.0], [-8.0, -16.0, -24.0]),
    ([-2.0, 0.0, 2.0], [-4.0, 0.0, 4.0]),
    ([1.0, 3.0, 5.0, 7.0], [2.0, 6.0, 10.0, 14.0]),
    ([-3.0, -2.0, -1.0, 0.0], [9.0, 4.0, 1.0, 0.0]),
    ([0.5, 1.5, 2.5], [2.0, 3.5, 5.0]),
    ([-1.0, 0.5, 1.5], [0.0, 1.0, 4.0]),
    ([3.0, 6.0, 9.0], [7.0, 13.0, 21.0]),
])
def test_canberraDist_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
