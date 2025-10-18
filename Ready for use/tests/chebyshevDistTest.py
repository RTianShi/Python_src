# test_chebyshevDist.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check
import math
from typing import List, Sequence

DELTA = 1e-9

def is_close(a: float, b: float, tol: float = DELTA) -> bool:
    """Approximate equality (absolute tolerance)."""
    return math.isclose(a, b, abs_tol=tol)

def arrays_close(a: Sequence[float], b: Sequence[float], tol: float = DELTA) -> bool:
    """Element-wise approximate equality; lengths must match."""
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if not is_close(x, y, tol):
            return False
    return True

def arrays_equal_strict(a: Sequence[float], b: Sequence[float]) -> bool:
    """Element-wise strict equality (==)."""
    if a is None or b is None:
        return False
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x != y:
            return False
    return True

def applyMR_Assert(originalInput1_1: List[float], originalInput1_2: List[float], originalResult: float):
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

    # ---------------- Assertions (strict mapping from Java semantics) ----------------

    # OR2: Java used assertEquals(originalResult, transformResult6, delta)
    check.is_true(is_close(originalResult, transformResult6), "OR2 failed (MR6)")

    # OR3_1 and OR3_2: Java used 'assertTrue(originalResult == transformResult3_x)' -> strict equality
    check.equal(originalResult, transformResult3_1, "OR3_1 failed (MR3_1)")
    check.equal(originalResult, transformResult3_2, "OR3_2 failed (MR3_2)")

    # OR5: Java used 'originalResult <= transformResult5'
    check.is_true(originalResult <= transformResult5, "OR5 failed (MR5)")

    # OR6: Java used assertEquals(originalResult, transformResult6, delta) again
    check.is_true(is_close(originalResult, transformResult6), "OR6 failed (MR6)")

    # OR7_1, OR7_2: Java used strict '=='
    check.equal(originalResult, transformResult7_1, "OR7_1 failed (MR7_1)")
    check.equal(originalResult, transformResult7_2, "OR7_2 failed (MR7_2)")

    # OR8: Java used strict '=='
    check.equal(originalResult, transformResult8, "OR8 failed (MR8)")

    # OR10: Java used strict '=='
    check.equal(originalResult, transformResult10, "OR10 failed (MR10)")

    # OR11: commented out in Java -> keep no assertion

    # OR12: Java used strict '=='
    check.equal(originalResult, transformResult12, "OR12 failed (MR12)")

    # OR13: Java used assertEquals(originalResult, transformResult13, delta)
    check.is_true(is_close(originalResult, transformResult13), "OR13 failed (MR13)")

    # OR15: Java used assertEquals(originalResult, transformResult15, delta)
    check.is_true(is_close(originalResult, transformResult15), "OR15 failed (MR15)")

    # OR16: Java used strict '=='
    check.equal(originalResult, transformResult16, "OR16 failed (MR16)")

    # OR19: Java used strict '=='
    check.equal(originalResult, transformResult19, "OR19 failed (MR19)")

    # OR20: commented out in Java (no assertion)

    # OR22: Java used strict '=='
    check.equal(originalResult, transformResult22, "OR22 failed (MR22)")

@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]),
    ([0.0, 2.0, 4.0], [1.0, 2.0, 3.0]),
    ([-1.0, 0.0, 1.0], [1.0, 0.0, -1.0]),
    ([5.0, 7.0], [3.0, 5.0]),
    ([-2.0, -4.0, -6.0], [-1.0, -2.0, -3.0]),
    ([0.5, 1.5, 2.5], [0.5, 1.0, 2.0]),
    ([3.0, 6.0], [6.0, 12.0]),
    ([-1.0, 1.0, 0.0], [1.0, -1.0, 0.0]),
    ([2.0, 3.0, 4.0, 5.0], [1.0, 3.0, 5.0, 7.0]),
    ([10.0, 20.0, 30.0], [5.0, 10.0, 15.0]),
])
def test_chebyshevDist_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
