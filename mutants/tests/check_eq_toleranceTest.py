# test_check_eq_tolerance.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check
from typing import List

TOL = 1e-9

def applyMR_Assert(originalInput1_1: List[float], originalInput1_2: List[float], originalResult: bool):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2, TOL)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2, TOL)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2, TOL)

    # MR3_2: 乘法单位元 1
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4, TOL)

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2, TOL)

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2, TOL)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2, TOL)

    # MR7_1: 中立操作（乘1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2, TOL)

    # MR7_2: 中立操作（加0）
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4, TOL)

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2, TOL)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2, TOL)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2, TOL)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2, TOL)

    # MR12: 数值取反
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2, TOL)

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2, TOL)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2, TOL)

    # MR15: 类三角函数的周期性
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2, TOL)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2, TOL)

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2, TOL)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2, TOL)

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2, TOL)

    # ---------------- Assertions (strict equality as in Java source) ----------------
    # OR2: 源输出等于后续输出
    check.equal(originalResult, transformResult2, "OR2 failed (MR2)")
    # OR3_1
    check.equal(originalResult, transformResult3_1, "OR3_1 failed (MR3_1)")
    # OR3_2
    check.equal(originalResult, transformResult3_2, "OR3_2 failed (MR3_2)")
    # OR4
    check.equal(originalResult, transformResult4, "OR4 failed (MR4)")
    # OR5
    check.equal(originalResult, transformResult5, "OR5 failed (MR5)")
    # OR6
    check.equal(originalResult, transformResult6, "OR6 failed (MR6)")
    # OR7_1
    check.equal(originalResult, transformResult7_1, "OR7_1 failed (MR7_1)")
    # OR7_2
    check.equal(originalResult, transformResult7_2, "OR7_2 failed (MR7_2)")
    # OR8
    check.equal(originalResult, transformResult8, "OR8 failed (MR8)")
    # OR9
    check.equal(originalResult, transformResult9, "OR9 failed (MR9)")
    # OR10
    check.equal(originalResult, transformResult10, "OR10 failed (MR10)")
    # OR11
    check.equal(originalResult, transformResult11, "OR11 failed (MR11)")
    # OR12
    check.equal(originalResult, transformResult12, "OR12 failed (MR12)")
    # OR13
    check.equal(originalResult, transformResult13, "OR13 failed (MR13)")
    # OR14
    check.equal(originalResult, transformResult14, "OR14 failed (MR14)")
    # OR15
    check.equal(originalResult, transformResult15, "OR15 failed (MR15)")
    # OR16
    check.equal(originalResult, transformResult16, "OR16 failed (MR16)")
    # OR19
    check.equal(originalResult, transformResult19, "OR19 failed (MR19)")
    # OR20
    check.equal(originalResult, transformResult20, "OR20 failed (MR20)")
    # OR22
    check.equal(originalResult, transformResult22, "OR22 failed (MR22)")


@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]),
    ([0.0, 2.0, 4.0], [0.0, 2.0, 4.0]),
    ([-1.0, 0.0, 1.0], [-1.0, 0.0, 1.0]),
    ([5.0, 7.0], [5.0, 7.0]),
    ([-2.0, -4.0, -6.0], [-2.0, -4.0, -6.0]),
    ([0.5, 1.5, 2.5], [0.5, 1.5, 2.5]),
    ([3.0, 6.0], [3.0, 6.0]),
    ([-1.0, 1.0, 0.0], [-1.0, 1.0, 0.0]),
    ([2.0, 3.0, 4.0, 5.0], [2.0, 3.0, 4.0, 5.0]),
    ([10.0, 20.0, 30.0], [10.0, 20.0, 30.0]),
])
def test_check_eq_tolerance_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2, TOL)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
