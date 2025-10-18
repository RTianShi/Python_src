# 不需要 fixture 注入
from textual.events import Print
from mutants import runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1
import pytest
import pytest_check as check

from src.check_equal import check_equal

print("test_check_equal 执行了")

def applyMR_Assert(originalInput1_1, originalInput1_2, originalResult):
    func = check_equal
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 乘法单位元 1
    transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 数组元素取倒数（结果为 Double[]，转 int 列表）
    transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput1_2)
    transformInput4_3 = [int(x) for x in transformInput4_1]
    transformInput4_4 = [int(x) for x in transformInput4_2]
    transformResult4 = func(transformInput4_3, transformInput4_4)

    # MR5: 数组缩放变换
    transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 数组反转变换
    transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 所有元素加0
    transformInput7_3 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(transformInput7_3, transformInput7_4)

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator1.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator1.applyMR8(originalInput1_2)
    transformResult8 = func(transformInput8_1, transformInput8_2)

    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator1.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator1.applyMR9(originalInput1_2, 1)
    transformResult9 = func(transformInput9_1, transformInput9_2)

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator1.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator1.applyMR10(originalInput1_2)
    transformResult10 = func(transformInput10_1, transformInput10_2)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11_1 = MetamorphicTestGenerator1.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator1.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13: 微小增量调整（Double[] -> int 列表）
    transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput1_2)
    transformInput13_3 = [int(x) for x in transformInput13_1]
    transformInput13_4 = [int(x) for x in transformInput13_2]
    transformResult13 = func(transformInput13_3, transformInput13_4)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15: 类三角函数的周期性（Double[] -> int 列表）
    transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput1_2)
    transformInput15_3 = [int(x) for x in transformInput15_1]
    transformInput15_4 = [int(x) for x in transformInput15_2]
    transformResult15 = func(transformInput15_3, transformInput15_4)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput1_2)
    transformInput20_3 = [int(x) for x in transformInput20_1]
    transformInput20_4 = [int(x) for x in transformInput20_2]
    transformResult20 = func(transformInput20_3, transformInput20_4)

    # MR22: 应用恒等变换
    transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # ---------------- Assertions ----------------
    check.equal(originalResult, transformResult2, "MR2 failed")
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")
    check.equal(originalResult, transformResult3_2, "MR3_2 failed")
    check.equal(originalResult, transformResult4, "MR4 failed")
    check.equal(originalResult, transformResult5, "MR5 failed")
    check.equal(originalResult, transformResult6, "MR6 failed")
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")
    check.equal(originalResult, transformResult8, "MR8 failed")
    check.equal(originalResult, transformResult9, "MR9 failed")
    check.equal(originalResult, transformResult10, "MR10 failed")
    check.equal(originalResult, transformResult11, "MR11 failed")
    check.equal(originalResult, transformResult12, "MR12 failed")
    check.equal(originalResult, transformResult13, "MR13 failed")
    check.equal(originalResult, transformResult14, "MR14 failed")
    check.equal(originalResult, transformResult15, "MR15 failed")
    check.equal(originalResult, transformResult16, "MR16 failed")
    check.equal(originalResult, transformResult19, "MR19 failed")
    check.equal(originalResult, transformResult20, "MR20 failed")
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1, 3, 2, 6, 9], [1, 3, 2, 6, 9]),
    ([2, 1, 4, 4, 2], [2, 1, 4, 4, 2]),
    ([4, -2, 4, 6, 2], [4, -2, 4, 6, 2]),
    ([9, 2, 1, 5, 3, 2], [9, 2, 1, 5, 3, 2]),
    ([-1, 9, 1, -3, -3], [-1, 9, 1, -3, -3]),
    ([8, 3, 2, 6, 2, 3], [8, 3, 2, 6, 2, 3]),
    ([1, 2, 3, 4, -5, 6], [1, 2, 3, 4, -5, 6]),
    ([1, 2, 4, 2, 7, 5], [1, 2, 4, 2, 7, 5]),
    ([1, 1, 2, 4, 1, 2], [1, 1, 2, 4, 1, 2]),
    ([-2, 3, 1, 4, 7], [-2, 3, 1, 4, 7]),
])
def test_check_equal_with_func(originalInput1_1, originalInput1_2):
    func = check_equal
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput1_1, originalInput1_2)
    applyMR_Assert(originalInput1_1, originalInput1_2, originalResult)
