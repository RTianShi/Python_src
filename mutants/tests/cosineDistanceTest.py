from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check

def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 乘法单位元 1
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 所有元素加0
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14: 移除元素的效果
    transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15: 类三角函数的周期性
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16: 重复值稳健性
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19: 输入重复
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20: 边界值灵敏度
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    delta = 1e-9  # 浮点数比较精度
    # ---------------- Assertions ----------------
    # MR3_1
    check.is_true(abs(originalResult - transformResult3_1) < delta, "MR3_1 failed")
    # MR6
    check.is_true(abs(originalResult - transformResult6) < delta, "MR6 failed")
    # MR7_1
    check.is_true(abs(originalResult - transformResult7_1) < delta, "MR7_1 failed")
    # MR7_2
    check.is_true(abs(originalResult - transformResult7_2) < delta, "MR7_2 failed")
    # MR12
    check.is_true(abs(originalResult - transformResult12) < delta, "MR12 failed")
    # MR22
    check.is_true(abs(originalResult - transformResult22) < delta, "MR22 failed")
    # 其他 MR 的断言可根据需求启用

@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.25, -0.75, 3.55], [0.55, 1.20, -2.45]),
    ([-2.34, 3.67, 4.89], [-1.45, 0.56, 2.78]),
    ([1.12, -1.44, 1.67], [-1.78, 1.56, 1.89]),
    ([1.88, 2.53, 3.11], [2.11, 3.88, 4.53]),
    ([0.13, -0.25, 0.38], [-1.40, 1.55, -1.70]),
    ([-2.67, 2.88, 3.01], [2.22, -2.33, 2.44]),
    ([3.14, -5.25, 2.78], [1.35, -2.55, 1.65]),
    ([0.43, -0.56, 0.78], [-0.33, 0.67, -0.54]),
    ([2.55, 0.95, 1.85], [1.85, 2.10, 0.85]),
    ([5.23, -5.34, 5.45, -5.56], [1.15, -1.25, 1.35, -1.45]),
])
def test_cosineDistance_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
