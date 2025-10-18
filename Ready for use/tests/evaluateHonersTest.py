# 不需要 fixture 注入
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, argument, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1:数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput)
    transformResult1 = func(transformInput1, argument)

    # MR2:数组元素常数加法
    transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput)
    transformResult2 = func(transformInput2, argument)

    # MR3_1:加入单位元不变性（加法的单位元0）
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1, argument)

    # MR3_2:加入单位元不变性（乘法的单位元1）
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2, argument)

    # MR4:数组元素取倒数
    transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput)
    transformResult4 = func(transformInput4, argument)

    # MR5:数组缩放变换
    transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5, argument)

    # MR6:数组反转变换
    transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput)
    transformResult6 = func(transformInput6, argument)

    # MR7_1:中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, argument)

    # MR7_2:中立操作的恒等变换（所有元素加上0）
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, argument)

    # MR8:重复输入数组
    transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput)
    transformResult8 = func(transformInput8, argument)

    # MR9:复合转换一致性
    transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3)
    transformResult9 = func(transformInput9, argument)

    # MR10:单调性检验
    transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput)
    transformResult10 = func(transformInput10, argument)

    # MR11:边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput)
    transformResult11 = func(transformInput11, argument)

    # MR12:数值取反变换
    transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput)
    transformResult12 = func(transformInput12, argument)

    # MR13:微小增量调整
    transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput)
    transformResult13 = func(transformInput13, argument)

    # MR14:移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput)
    transformResult14 = func(transformInput14, argument)

    # MR16:重复值稳健性(复制输入中的一个元素)
    transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput)
    transformResult16 = func(transformInput16, argument)

    # MR19:输入重复（元素复制）
    transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2)
    transformResult19 = func(transformInput19, argument)

    # MR20:边界值灵敏度（给最小值增加一个极小值）
    transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput)
    transformResult20 = func(transformInput20, argument)

    # MR22:应用恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(transformInput22, argument)

    # ---------------- Assertions ----------------
    check.is_true(originalResult <= transformResult2)
    check.is_true(originalResult <= transformResult3_1)
    check.is_true(originalResult <= transformResult3_2)
    check.is_true(originalResult <= transformResult5)
    check.equal(originalResult, transformResult7_1)
    check.equal(originalResult, transformResult7_2)
    check.is_true(originalResult <= transformResult8)
    check.is_true(originalResult <= transformResult10)
    check.is_true(originalResult >= transformResult14)
    check.equal(originalResult, transformResult22)


@pytest.mark.parametrize("originalInput, argument", [
    ([1.1, -2.22, 3.333], 2.5),
    ([4.56, 4.57, 4.58], 2.6),
    ([1.35, 1.46, 1.58, 1.96], 0.85),
    ([7.85, 6.33, 4.25], 2.55),
    ([1.56, 2.57, 3.58], 2.0),
    ([-0.123, 2.456, 4.567], 3.3),
    ([-1.85, 6.31, 4.66], 2.25),
    ([2.718, 3.141, 0.567], 0.001),
    ([4.65, 7.03, 6.08], 5.0),
    ([1.29, 0.36, 4.22], 0.58),
])
def test_evaluateHoners_with_func(originalInput, argument):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, argument)
    applyMR_Assert(originalInput, argument, originalResult)
