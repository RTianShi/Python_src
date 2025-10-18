import copy
import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator2 import MetamorphicTestGenerator2

print("test_dec 执行了")


def sum_array(arr):
    """计算整数列表的和（与 Java 的 sum(int[]) 行为一致）"""
    if arr is None:
        return 0
    return sum(int(x) for x in arr)


def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    # 保持与 Java 版一致的行为：直接计算每个 MR 的变换并断言（无 try/except）
    print("\n")  # 输出 mutant 名称 + 换行（与 Java 程序一致的输出位置）

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator2.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator2.applyMR1(originalInput1_2)
    transformResult1 = runner.CURRENT_MUTANT_FUNC(transformInput1_1, transformInput1_2)
    # OR1: 不做断言 (Java 中无断言)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator2.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator2.applyMR2(originalInput1_2)
    transformResult2 = runner.CURRENT_MUTANT_FUNC(transformInput2_1, transformInput2_2)
    # Java: assertTrue(Arrays.equals(originalResult, transformResult2));
    check.equal(originalResult, transformResult2, "MR2 failed")

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator2.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator2.applyMR3_1(originalInput1_2)
    transformResult3_1 = runner.CURRENT_MUTANT_FUNC(transformInput3_1, transformInput3_2)
    # Java: assertArraySumEqual(originalResult, transformResult3_1);
    check.equal(sum_array(transformResult3_1), sum_array(originalResult), "MR3_1 failed")

    # MR3_2: 乘法单位元1
    transformInput3_3 = MetamorphicTestGenerator2.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator2.applyMR3_2(originalInput1_2)
    transformResult3_2 = runner.CURRENT_MUTANT_FUNC(transformInput3_3, transformInput3_4)
    check.equal(sum_array(transformResult3_2), sum_array(originalResult), "MR3_2 failed")

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator2.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator2.applyMR4(originalInput1_2)
    transformInput4_3 = [int(x) for x in transformInput4_1]
    transformInput4_4 = [int(x) for x in transformInput4_2]
    transformResult4 = runner.CURRENT_MUTANT_FUNC(transformInput4_3, transformInput4_4)
    # OR4: 不做断言

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator2.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator2.applyMR5(originalInput1_2, 2)
    transformResult5 = runner.CURRENT_MUTANT_FUNC(transformInput5_1, transformInput5_2)
    # OR5: 不做断言

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator2.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator2.applyMR6(originalInput1_2)
    transformResult6 = runner.CURRENT_MUTANT_FUNC(transformInput6_1, transformInput6_2)
    # Java: assertArraySumEqual(originalResult, transformResult6);
    check.equal(sum_array(transformResult6), sum_array(originalResult), "MR6 failed")

    # MR7_1: 中立操作（乘1）
    transformInput7_1 = MetamorphicTestGenerator2.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator2.applyMR7_1(originalInput1_2)
    transformResult7_1 = runner.CURRENT_MUTANT_FUNC(transformInput7_1, transformInput7_2)
    check.equal(sum_array(transformResult7_1), sum_array(originalResult), "MR7_1 failed")

    # MR7_2: 中立操作（加0）
    transformInput7_3 = MetamorphicTestGenerator2.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator2.applyMR7_2(originalInput1_2)
    transformResult7_2 = runner.CURRENT_MUTANT_FUNC(transformInput7_3, transformInput7_4)
    check.equal(sum_array(transformResult7_2), sum_array(originalResult), "MR7_2 failed")

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator2.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator2.applyMR8(originalInput1_2)
    transformResult8 = runner.CURRENT_MUTANT_FUNC(transformInput8_1, transformInput8_2)
    # OR8: 不做断言

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator2.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator2.applyMR9(originalInput1_2, 1)
    transformResult9 = runner.CURRENT_MUTANT_FUNC(transformInput9_1, transformInput9_2)
    # OR9: 不做断言

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator2.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator2.applyMR10(originalInput1_2)
    transformResult10 = runner.CURRENT_MUTANT_FUNC(transformInput10_1, transformInput10_2)
    check.equal(sum_array(transformResult10), sum_array(originalResult), "MR10 failed")

    # MR11: 边界值替换
    transformInput11_1 = MetamorphicTestGenerator2.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator2.applyMR11(originalInput1_2)
    transformResult11 = runner.CURRENT_MUTANT_FUNC(transformInput11_1, transformInput11_2)
    # OR11: 不做断言

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator2.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator2.applyMR12(originalInput1_2)
    transformResult12 = runner.CURRENT_MUTANT_FUNC(transformInput12_1, transformInput12_2)
    # OR12: 不做断言

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator2.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator2.applyMR13(originalInput1_2)
    transformInput13_3 = [int(x) for x in transformInput13_1]
    transformInput13_4 = [int(x) for x in transformInput13_2]
    transformResult13 = runner.CURRENT_MUTANT_FUNC(transformInput13_3, transformInput13_4)
    # OR13: 不做断言

    # MR15: 类三角函数的周期性
    transformInput15_1 = MetamorphicTestGenerator2.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator2.applyMR15(originalInput1_2)
    transformInput15_3 = [int(x) for x in transformInput15_1]
    transformInput15_4 = [int(x) for x in transformInput15_2]
    transformResult15 = runner.CURRENT_MUTANT_FUNC(transformInput15_3, transformInput15_4)
    # OR15: 不做断言

    # MR16: 重复值稳健性
    transformInput16_1 = MetamorphicTestGenerator2.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator2.applyMR16(originalInput1_2)
    transformResult16 = runner.CURRENT_MUTANT_FUNC(transformInput16_1, transformInput16_2)
    # OR16: 不做断言

    # MR19: 输入重复
    transformInput19_1 = MetamorphicTestGenerator2.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator2.applyMR19(originalInput1_2, 2)
    transformResult19 = runner.CURRENT_MUTANT_FUNC(transformInput19_1, transformInput19_2)
    # OR19: 不做断言

    # MR20: 边界值灵敏度
    transformInput20_1 = MetamorphicTestGenerator2.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator2.applyMR20(originalInput1_2)
    transformInput20_3 = [int(x) for x in transformInput20_1]
    transformInput20_4 = [int(x) for x in transformInput20_2]
    transformResult20 = runner.CURRENT_MUTANT_FUNC(transformInput20_3, transformInput20_4)
    # OR20: 不做断言

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator2.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator2.applyMR22(originalInput1_2)
    transformResult22 = runner.CURRENT_MUTANT_FUNC(transformInput22_1, transformInput22_2)
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("input1,input2", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1]),
    ([5, 5, 5, 5, 5], [1, 2, 3, 4, 5]),
    ([10, 20, 30, 40, 50], [50, 40, 30, 20, 10]),
    ([-1, -2, -3, -4, -5], [1, 2, 3, 4, 5]),
    ([1000, 2000, 3000, 4000, 5000], [5000, 4000, 3000, 2000, 1000]),
    ([1, 2, 3, 4, 5], [5, 5, 5, 5, 5]),
    ([1, -1, 2, -2, 3, -3], [1, 1, 2, 2, 3, 3]),
])
def test_dec_with_func(input1, input2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    # 保持与 Java 版相同的 input copy 语义
    originalInput1 = copy.deepcopy(input1)
    originalInput2 = copy.deepcopy(input2)
    originalResult = func(originalInput1, originalInput2)
    applyMR_Assert(originalInput1, originalInput2, originalResult)
