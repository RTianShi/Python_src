# 不需要 fixture 注入
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check

def applyMR_Assert(originalInput1_1, originalInput1_2, z, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2, z)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2, z)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2, z)

    # MR3_2: 乘法单位元 1
    transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4, z)

    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2)
    transformResult4 = func(transformInput4_1, transformInput4_2, z)

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2, z)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2, z)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2, z)

    # MR7_2: 所有元素加0
    transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4, z)

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2, z)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2, z)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2, z)

    # MR11: 边界值替换
    transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2, z)

    # MR12: 数值取反
    transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2, z)

    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2, z)

    # MR15: 类三角函数周期性
    transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2, z)

    # MR16: 重复值稳健性
    transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2, z)

    # MR19: 输入重复
    transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2, z)

    # MR20: 边界值灵敏度
    transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2, z)

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2, z)

    # ---------------- Assertions ----------------
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    check.equal(originalResult, transformResult22, "MR22 failed")
    # 其他 MR 可按需添加 check.assert

@pytest.mark.parametrize("originalInput1_1, originalInput1_2, z", [
    ([1.1, 2.22, 3.333], [2.5, -1.234, 4.567], 1.5),
    ([4.65, 8.22, 9.33, 10.26], [7.77, 6.86, 9.13, 10.25], -1.8),
    ([5.41, 8.26, 4.61], [-2.03, 4.06, 7.09], 2.222),
    ([2.718, 3.141, -1.0], [4.567, -2.345, 0.001], 0.0),
    ([0.001, -1.001, 1.234, 3.141], [4.0, 5.0, 7.0, 8.0], -5.0),
    ([-1.1, -2.2, -3.3], [2.25, -3.45, 5.55], 2.222),
    ([0.001, 0.002, 0.003], [7.363, 4.555, 1.545], 1.999),
    ([-9.876, 4.321, 0.0], [3.142, 2.222, -1.001], 0.321),
    ([5.123, -1.234, 2.456], [-1.00, -2.36, -4.15], 3.333),
    ([0.777, 1.888, -9.999], [5.123, -1.234, 2.456], -0.555),
])
def test_evalNewton_with_func(originalInput1_1, originalInput1_2, z):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2, z)
    applyMR_Assert(originalInput1_1, originalInput1_2, z, originalResult)
