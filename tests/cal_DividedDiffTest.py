# test_cal_DividedDiff.py
from mutants import runner
from MetamorphicTestGenerator5 import MetamorphicTestGenerator5
import pytest
import pytest_check as check
from typing import List

from src.cal_DividedDiff import cal_DividedDiff


def format_array(arr: List[float], places: int) -> List[float]:
    """Round each element to `places` decimal places (mimic Java formatArray)."""
    if arr is None:
        return []
    factor = 10 ** places
    return [round(x * factor) / factor for x in arr]

def array_negation(arr1: List[float], arr2: List[float]) -> bool:
    """Return True if arrays have same length and there exists i with arr1[i] == -arr2[i]."""
    if not arr1 or not arr2 or len(arr1) != len(arr2):
        return False
    for a, b in zip(arr1, arr2):
        if a == -b:
            return True
    return False

def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    """
    originalInput1_1: list[float]
    originalInput1_2: list[float]
    originalResult: list[float] (output of func)
    """
    func = cal_DividedDiff
    assert func is not None, "mutant_func 没有被注入"

    # MR1
    transformInput1_1 = MetamorphicTestGenerator5.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator5.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2
    transformInput2_1 = MetamorphicTestGenerator5.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator5.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1
    transformInput3_1 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2
    transformInput3_3 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4
    transformInput4_1 = MetamorphicTestGenerator5.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator5.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5
    transformInput5_1 = MetamorphicTestGenerator5.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator5.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6
    transformInput6_1 = MetamorphicTestGenerator5.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator5.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1
    transformInput7_1 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2
    transformInput7_3 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8
    transformInput8_1 = MetamorphicTestGenerator5.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator5.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9
    transformInput9_1 = MetamorphicTestGenerator5.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator5.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10
    transformInput10_1 = MetamorphicTestGenerator5.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator5.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11
    transformInput11_1 = MetamorphicTestGenerator5.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator5.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12
    transformInput12_1 = MetamorphicTestGenerator5.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator5.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13
    transformInput13_1 = MetamorphicTestGenerator5.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator5.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14
    transformInput14_1 = MetamorphicTestGenerator5.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator5.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15
    transformInput15_1 = MetamorphicTestGenerator5.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator5.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16
    transformInput16_1 = MetamorphicTestGenerator5.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator5.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19
    transformInput19_1 = MetamorphicTestGenerator5.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator5.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20
    transformInput20_1 = MetamorphicTestGenerator5.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator5.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22
    transformInput22_1 = MetamorphicTestGenerator5.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator5.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # ---------------- Assertions ----------------
    # Many Java assertions were commented — keep same enabled assertions as Java:
    # OR7_1, OR7_2, OR10, OR22 are active in Java version.
    check.equal(format_array(originalResult, 2), format_array(transformResult7_1, 2), "OR7_1 failed (MR7_1)")
    check.equal(format_array(originalResult, 2), format_array(transformResult7_2, 2), "OR7_2 failed (MR7_2)")
    check.equal(format_array(originalResult, 2), format_array(transformResult10, 2), "OR10 failed (MR10)")
    check.equal(format_array(originalResult, 2), format_array(transformResult22, 2), "OR22 failed (MR22)")

@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.5, 2.5, 3.5, 4.5, 5.5], [3.8, 4.8, 5.8, 6.8, 7.8]),
    ([10.2, 20.2, 30.2, 40.2], [5.6, 6.6, 7.6, 8.6]),
    ([5.56, 10.83, 15.21, 20.55], [2.61, 7.25, 8.36, 4.55]),
    ([1.62, 3.56, 5.74, 7.89, 9.96], [6.55, 6.33, 7.53, 8.12, 9.13]),
    ([1.62, 3.56, 5.74, 7.89], [2.61, 7.25, 8.36, 4.55]),
    ([10.2, 20.2, 30.2, 40.2], [2.61, 7.25, 8.36, 4.55]),
    ([3.8, 4.8, 5.8, 6.8, 7.8], [1.62, 3.56, 5.74, 7.89, 9.96]),
    ([5.56, 2.56, 7.56], [3.8, 4.8, 5.8]),
    ([99.86, 100.23, 101.43, 102.55], [2.61, 7.25, 8.36, 4.55]),
    ([3.8, 4.8, 5.8], [5.56, 2.56, 7.56]),
])
def test_cal_DividedDiff_with_func(originalInput1_1, originalInput1_2):
    func = cal_DividedDiff
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
