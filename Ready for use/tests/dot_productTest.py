import copy
import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1

print("test_dot_product 执行了")


def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    """
    originalInput1_1, originalInput1_2: List[int]
    originalResult: int
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序） -- no assertion in Java
    transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)
    check.is_true(originalResult <= transformResult2, "MR2 failed")

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")

    # MR3_2: 乘法单位元1
    transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)
    check.is_true(originalResult <= transformResult3_2, "MR3_2 failed")

    # MR4: 数组元素取倒数 (Double -> int)
    transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput1_2)
    transformInput4_3 = [int(x) for x in transformInput4_1]
    transformInput4_4 = [int(x) for x in transformInput4_2]
    transformResult4 = func(transformInput4_3, transformInput4_4)
    check.is_true(originalResult >= transformResult4, "MR4 failed")

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)
    check.is_true(originalResult <= transformResult5, "MR5 failed")

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)
    check.equal(originalResult, transformResult6, "MR6 failed")

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")

    # MR7_2: 所有元素加0
    transformInput7_3 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator1.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator1.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)
    check.is_true(originalResult <= transformResult8, "MR8 failed")

    # MR9: 复合转换一致性 (constant 1)
    transformInput9_1 = MetamorphicTestGenerator1.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator1.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)
    # Java 注释 OR9；在原 Java 中未启用断言 -> 不断言 here

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator1.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator1.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)
    check.is_true(originalResult <= transformResult10, "MR10 failed")

    # MR11: 边界值替换 -- Java 注释 OR11 (无断言)

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)
    check.equal(originalResult, transformResult12, "MR12 failed")

    # MR13: 微小增量调整 (Double -> int)
    transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput1_2)
    transformInput13_3 = [int(x) for x in transformInput13_1]
    transformInput13_4 = [int(x) for x in transformInput13_2]
    transformResult13 = func(transformInput13_3, transformInput13_4)
    # Java 注释 OR13 (无断言)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)
    check.is_true(originalResult >= transformResult14, "MR14 failed")

    # MR15: 类三角函数的周期性 (Double -> int)
    transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput1_2)
    transformInput15_3 = [int(x) for x in transformInput15_1]
    transformInput15_4 = [int(x) for x in transformInput15_2]
    transformResult15 = func(transformInput15_3, transformInput15_4)
    # Java 注释 OR15 (无 assertion)

    # MR16: 重复值稳健性 (复制第一个元素)
    transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)
    # Java 注释 OR16 (无 assertion)

    # MR19: 输入重复（元素复制）
    transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)
    # Java 注释 OR19 (无 assertion)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput1_2)
    transformInput20_3 = [int(x) for x in transformInput20_1]
    transformInput20_4 = [int(x) for x in transformInput20_2]
    transformResult20 = func(transformInput20_3, transformInput20_4)
    check.is_true(originalResult <= transformResult20, "MR20 failed")

    # MR22: 恒等变换
    transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("input1,input2", [
    ([1, 2, 3, 4], [18, 19, 20, 21]),
    ([8, 9, 9, 9, 8], [10, 6, 5, 6, 10]),
    ([-2, 3, 4, -1, 0], [2, -1, 3, 4, -5]),
    ([2, 4, 6, 8], [8, 6, 4, 3]),
    ([5, 5, 5, 5], [7, 7, 7, 7]),
    ([0, 0, 0, 0], [1, 1, 1, 1]),
    ([0, 1, 4, 1, 0], [1, 0, 4, 0, 1]),
    ([2, 5, 8, 11, 14], [3, 6, 9, 12, 15]),
    ([-1, 1, 3, 5, 7], [0, 1, 2, 3, 4]),
    ([7, -5, 4, -3, 2], [1, 2, 3, 4, 5]),
])
def test_dot_product_with_func(input1, input2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalInput1 = copy.deepcopy(input1)
    originalInput2 = copy.deepcopy(input2)
    originalResult = func(originalInput1, originalInput2)
    applyMR_Assert(originalInput1, originalInput2, originalResult)
