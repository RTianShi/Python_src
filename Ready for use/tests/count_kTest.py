# 不需要 fixture 注入
from mutants import runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, k, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput)
    transformResult1 = func(transformInput1, k)

    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput)
    transformResult2 = func(transformInput2, k)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1, k)

    # MR3_2: 乘法单位元 1
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2, k)

    # MR4: 数组元素取倒数
    transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput)
    transformInput4_1 = [int(x) for x in transformInput4]
    transformResult4 = func(transformInput4_1, k)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5, k)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    transformResult6 = func(transformInput6, k)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, k)

    # MR7_2: 所有元素加0
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, k)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput)
    transformResult8 = func(transformInput8, k)

    # MR9: 复合转换一致性
    transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3)
    transformResult9 = func(transformInput9, k)

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput)
    transformResult10 = func(transformInput10, k)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput)
    transformResult11 = func(transformInput11, k)

    # MR12: 数值取反变换
    transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput)
    transformResult12 = func(transformInput12, k)

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput)
    transformInput13_1 = [int(x) for x in transformInput13]
    transformResult13 = func(transformInput13_1, k)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    transformResult14 = func(transformInput14, k)

    # MR16: 重复值稳健性
    transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    transformResult16 = func(transformInput16, k)

    # MR20: 边界值灵敏度
    transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    transformInput20_1 = [int(x) for x in transformInput20]
    transformResult20 = func(transformInput20_1, k)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = func(transformInput22, k)

    # ---------------- Assertions ----------------
    check.equal(originalResult, transformResult1, "MR1 failed")
    # check.equal(originalResult + len(originalInput) * 3, transformResult2, "MR2 failed")
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")
    check.equal(originalResult, transformResult3_2, "MR3_2 failed")
    # check.is_true(originalResult >= transformResult4, "MR4 failed")
    # check.equal(originalResult * 2, transformResult5, "MR5 failed")
    check.equal(originalResult, transformResult6, "MR6 failed")
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    # check.equal(originalResult * 2, transformResult8, "MR8 failed")
    # check.equal(originalResult * 3, transformResult9, "MR9 failed")
    # check.is_true(originalResult <= transformResult10, "MR10 failed")
    # check.is_true(originalResult >= transformResult11, "MR11 failed")
    # check.equal(-originalResult, transformResult12, "MR12 failed")
    # check.is_true(originalResult <= transformResult13, "MR13 failed")
    # check.is_true(originalResult >= transformResult14, "MR14 failed")
    # check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("originalInput,k", [
    ([1, 2, 3, 4, 2], 2),
    ([20, -20, 0, -20, 20], 0),
    ([-1, 0, 1, -1, 0], 0),
    ([36, -36, 36, -36], 0),
    ([20, -20, 20, -20, 20], 0),
    ([-35, -35, 35, 35, 35], 0),
    ([3000, 2000, 1000, 0], 1),
    ([0, 0, -1, 1, -1], 0),
    ([2, -2, 2, -2, -2], 2),
    ([5, 4, 3, 2, 1], 1),
])
def test_count_k_with_func(originalInput, k):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, k)
    applyMR_Assert(originalInput, k, originalResult)
