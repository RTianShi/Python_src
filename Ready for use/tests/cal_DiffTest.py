# test_cal_Diff.py
from mutants import runner
from MetamorphicTestGenerator5 import MetamorphicTestGenerator5
import pytest
import pytest_check as check
import math
from typing import List

def format_array(arr: List[float], places: int) -> List[float]:
    """Round each element to `places` decimal places (like Java formatArray)."""
    if arr is None:
        return []
    factor = 10 ** places
    return [round(x * factor) / factor for x in arr]

def array_negation(arr1: List[float], arr2: List[float]) -> bool:
    """Return True if arrays have same length and there exists i with arr1[i] == -arr2[i]."""
    if not arr1 or not arr2 or len(arr1) != len(arr2):
        return False
    for a, b in zip(arr1, arr2):
        # compare with exact equality on rounded values (they already rounded before calling)
        if a == -b:
            return True
    return False

def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    """
    originalInput1_1: list[float]
    originalInput1_2: list[float]
    originalResult: list[float] (output of func)
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator5.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator5.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator5.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator5.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加法单位元不变性（加0）
    transformInput3_1 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 乘法单位元不变性（乘1）
    transformInput3_3 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 元素取倒数
    transformInput4_1 = MetamorphicTestGenerator5.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator5.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5: 缩放变换
    transformInput5_1 = MetamorphicTestGenerator5.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator5.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 反转变换
    transformInput6_1 = MetamorphicTestGenerator5.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator5.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 乘1 不变
    transformInput7_1 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 加0 不变
    transformInput7_3 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8: 重复输入
    transformInput8_1 = MetamorphicTestGenerator5.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator5.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator5.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator5.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator5.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator5.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11: 边界值替换
    transformInput11_1 = MetamorphicTestGenerator5.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator5.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12: 数值取反
    transformInput12_1 = MetamorphicTestGenerator5.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator5.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator5.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator5.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14: 移除元素
    transformInput14_1 = MetamorphicTestGenerator5.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator5.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15: 周期性（三角类）
    transformInput15_1 = MetamorphicTestGenerator5.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator5.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16: 重复值稳健性
    transformInput16_1 = MetamorphicTestGenerator5.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator5.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19: 输入重复（元素复制）
    transformInput19_1 = MetamorphicTestGenerator5.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator5.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20: 边界值灵敏度
    transformInput20_1 = MetamorphicTestGenerator5.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator5.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22: 恒等变换
    transformInput22_1 = MetamorphicTestGenerator5.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator5.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # ---------------- Assertions ----------------
    # Java 中对数组先 format 再比较（保留到 2 位小数），这里用 format_array(..., 2)
    check.equal(format_array(originalResult, 2), format_array(transformResult1, 2), "OR1 failed (MR1)")
    check.equal(format_array(originalResult, 2), format_array(transformResult2, 2), "OR2 failed (MR2)")
    # OR3_1 注释（Java 中注释）
    # OR3_2 注释
    # OR4 等注释保留
    # OR5 注释
    # OR6 注释
    check.equal(format_array(originalResult, 2), format_array(transformResult7_1, 2), "OR7_1 failed (MR7_1)")
    check.equal(format_array(originalResult, 2), format_array(transformResult7_2, 2), "OR7_2 failed (MR7_2)")
    check.equal(format_array(originalResult, 2), format_array(transformResult10, 2), "OR10 failed (MR10)")
    # OR11..OR12..OR13..OR14.. 注释保持
    # OR15: special negation check (Java used assertArrayNegation)
    check.is_true(array_negation(format_array(originalResult, 2), format_array(transformResult15, 2)),
                  "OR15 failed (MR15)")
    # OR22
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
def test_cal_Diff_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
