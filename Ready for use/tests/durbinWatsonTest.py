import copy
import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4

print("test_durbinWatson 执行了")


def almost_equal(a: float, b: float, delta: float = 1e-9) -> bool:
    try:
        return abs(a - b) <= delta
    except Exception:
        return False


def applyMR_Assert(originalInput, originalResult):
    """
    originalInput: List[float]
    originalResult: float
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput)
    transformResult1 = func(transformInput1)

    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput)
    transformResult2 = func(transformInput2)

    # MR3_1: 加入单位元不变性（加法的单位元0）
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1)

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2)

    # MR4: 数组元素取倒数
    transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput)
    transformResult4 = func(transformInput4)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput)
    transformResult6 = func(transformInput6)

    # MR7_1: 中立操作（乘1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1)

    # MR7_2: 中立操作（加0）
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput)
    transformResult8 = func(transformInput8)

    # MR9: 复合转换一致性
    transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3)
    transformResult9 = func(transformInput9)

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput)
    transformResult10 = func(transformInput10)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput)
    transformResult11 = func(transformInput11)

    # MR12: 数值取反变换
    transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput)
    transformResult12 = func(transformInput12)

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput)
    transformResult13 = func(transformInput13)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput)
    transformResult14 = func(transformInput14)

    # MR15: 类三角函数的周期性 (在 Java 中为注释，保留变换但不做断言)
    # transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput)
    # transformResult15 = func(transformInput15)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput)
    transformResult16 = func(transformInput16)

    # MR19: 输入重复（元素复制）
    transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2)
    transformResult19 = func(transformInput19)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput)
    transformResult20 = func(transformInput20)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(transformInput22)

    # ---------------- Assertions (对应 Java 的 OR 规则) ----------------
    delta = 1e-9

    # OR5: 源输出和乘以2等于后续输出 -> Java used originalResult <= transformResult5
    check.is_true(originalResult <= transformResult5, "MR5 failed")

    # OR7_1: 源输出数组等于后续输出数组
    check.is_true(almost_equal(originalResult, transformResult7_1, delta), "MR7_1 failed")

    # OR7_2:
    check.is_true(almost_equal(originalResult, transformResult7_2, delta), "MR7_2 failed")

    # OR8:
    check.is_true(originalResult <= transformResult8, "MR8 failed")

    # OR14: 源输出大于等于后续输出
    check.is_true(originalResult >= transformResult14, "MR14 failed")

    # OR16: 源输出小于等于后续输出
    check.is_true(originalResult <= transformResult16, "MR16 failed")

    # OR19:
    check.is_true(originalResult <= transformResult19, "MR19 failed")

    # OR22: 源输出等于后续输出 (Java used transformResult7_1 in last line — likely a copy; use transformResult22)
    check.is_true(almost_equal(originalResult, transformResult22, delta), "MR22 failed")


@pytest.mark.parametrize("input_arr", [
    ([1.2, 2.3, 3.5, 4.7]),
    ([-1.1, 0.5, -0.3, 2.0, 3.7]),
    ([3.14, -2.71, 1.61, 0.57, -3.14]),
    ([0.0, 0.0, 0.0, 0.0]),
    ([-2.5, 2.5, -2.5, 2.5, -2.5]),
    ([1.11, 2.22, 3.33]),
    ([4.4, -5.5, 6.6, -7.7]),
    ([-1.2, -2.3, -1.5, -2.7]),
    ([5.5, 3.2, 4.1, 2.8, 1.9]),
    ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5]),
])
def test_durbinWatson_with_func(input_arr):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalInput = copy.deepcopy(input_arr)
    originalResult = func(originalInput)
    applyMR_Assert(originalInput, originalResult)
