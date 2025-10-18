import pytest
import pytest_check as check
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4

def applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1:数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2, begin, length)

    # MR2:数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2, begin, length)

    # MR3_1:加入单位元不变性（加法的单位元0）
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2, begin, length)

    # MR3_2:加入单位元不变性（乘法的单位元1）
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4, begin, length)

    # MR4:数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2, begin, length)

    # MR5:数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2, begin, length)

    # MR6:数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2, begin, length)

    # MR7_1:中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2, begin, length)

    # MR7_2:中立操作的恒等变换（所有元素加上0）
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4, begin, length)

    # MR8:重复输入数组
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2, begin, length)

    # MR9:复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2, begin, length)

    # MR10:单调性检验
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2, begin, length)

    # MR11:边界值替换(把最大值替换成0)
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2, begin, length)

    # MR12:数值取反变换
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2, begin, length)

    # MR13:微小增量调整
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2, begin, length)

    # MR14:移除元素的效果（移除最大值）
    transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2, begin, length)

    # MR15:类三角函数的周期性
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2, begin, length)

    # MR16:重复值稳健性(复制输入中的一个元素)
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2, begin, length)

    # MR19:输入重复（元素复制）
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2, begin, length)

    # MR20:边界值灵敏度（给最小值增加一个极小值）
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2, begin, length)

    # MR22:应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2, begin, length)

    # ---------------- Assertions ----------------
    check.is_true(originalResult <= transformResult2)
    check.is_true(originalResult <= transformResult3_1)
    check.is_true(originalResult <= transformResult3_2)
    check.is_true(originalResult <= transformResult5)
    check.equal(originalResult, transformResult7_1)
    check.equal(originalResult, transformResult7_2)
    check.is_true(originalResult <= transformResult8)
    check.is_true(originalResult <= transformResult10)
    check.is_true(originalResult <= transformResult16)
    check.is_true(originalResult <= transformResult19)
    check.equal(originalResult, transformResult7_1)


@pytest.mark.parametrize("originalInput1_1, originalInput1_2, begin, length", [
    ([1.2, 3.0, 0.8, 2.2], [2.0, 1.0, 1.0, 0.5], 0, 2),
    ([1.55, 2.55, 3.55], [4.12, 4.13, 4.14], 0, 2),
    ([5.55, 7.55, 9.55], [10.55, 12.55, 14.55], 0, 2),
    ([12.16, 12.17, 12.18], [12.19, 12.20, 12.21], 0, 2),
    ([2.5, 0.7, 3.3], [1.1, 2.2, 0.9], 0, 2),
    ([1.6, 2.2, 3.4, 0.7], [0.5, 1.5, 2.1, 1.0], 0, 3),
    ([0.9, 1.8, 2.2], [0.3, 1.0, 1.2], 0, 2),
    ([2.0, 1.5, 0.8, 3.1], [0.7, 1.2, 1.5, 0.3], 0, 2),
    ([1.1, 2.5, 0.4], [1.0, 0.9, 0.8], 1, 1),
    ([0.3, 2.2, 1.5, 2.9, 1.1], [1.1, 0.8, 2.0, 1.2, 0.6], 0, 4),
])
def test_evalWeightedProd_with_func(originalInput1_1, originalInput1_2, begin, length):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None
    originalResult = func(originalInput1_1, originalInput1_2, begin, length)
    applyMR_Assert(originalInput1_1, originalInput1_2, begin, length)
0