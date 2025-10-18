from mutants import runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput)
    transformResult1 = func(transformInput1)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1)

    # MR3_2: 乘法单位元 1
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2)

    # MR4: 数组元素取倒数
    transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput)
    transformInput4_1 = [int(x) for x in transformInput4]
    transformResult4 = func(transformInput4_1)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    transformResult6 = func(transformInput6)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1)

    # MR7_2: 所有元素加0
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput)
    transformResult8 = func(transformInput8)

    # MR9: 复合转换一致性
    transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3)
    transformResult9 = func(transformInput9)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput)
    transformResult11 = func(transformInput11)

    # MR12: 数值取反变换
    transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput)
    transformResult12 = func(transformInput12)

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput)
    transformInput13_1 = [int(x) for x in transformInput13]
    transformResult13 = func(transformInput13_1)

    # MR14: 移除元素的效果
    transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    transformResult14 = func(transformInput14)

    # MR16: 重复值稳健性
    transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    transformResult16 = func(transformInput16)

    # MR20: 边界值灵敏度
    transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    transformInput20_1 = [int(x) for x in transformInput20]
    transformResult20 = func(transformInput20_1)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = func(transformInput22)

    # ---------------- Assertions ----------------
    check.equal(originalResult, transformResult1, "MR1 failed")
    check.equal(originalResult + 1, transformResult3_1, "MR3_1 failed")
    check.equal(originalResult, transformResult3_2, "MR3_2 failed")
    check.is_true(originalResult <= transformResult4, "MR4 failed")
    check.equal(originalResult, transformResult5, "MR5 failed")
    check.equal(originalResult, transformResult6, "MR6 failed")
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    check.equal(originalResult * 2, transformResult8, "MR8 failed")
    check.equal(originalResult, transformResult9, "MR9 failed")
    check.is_true(originalResult <= transformResult11, "MR11 failed")
    check.equal(originalResult, transformResult12, "MR12 failed")
    # MR13 的断言可根据需求启用
    # check.is_true(originalResult >= transformResult13, "MR13 failed")
    check.is_true(originalResult >= transformResult14, "MR14 failed")
    check.is_true(originalResult <= transformResult16, "MR16 failed")
    # MR20 的断言可根据需求启用
    # check.is_true(originalResult <= transformResult20, "MR20 failed")
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("originalInput", [
    [0, 1, 2, 0, 3],
    [1, 2, 3, 4, 5],
    [0, 0, 0, 0],
    [-1, 0, 1, 0, 0],
    [7, 8, 9],
    [0, 0, 1, 2, 0, 3, 0],
    [4, 5, 6, 7, 0],
    [-1, -2, -3, -4],
    [0, 1, 0, 2, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0],
])
def test_cnt_zeroes_with_func(originalInput):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput)
    applyMR_Assert(originalInput, originalResult)
