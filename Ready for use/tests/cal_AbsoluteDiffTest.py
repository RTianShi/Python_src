# test_cal_AbsoluteDiff.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, originalResult):
    """
    originalInput: list[float]
    originalResult: list[float]
    """

    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput)
    transformResult1 = func(transformInput1)

    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput)
    transformResult2 = func(transformInput2)

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1)

    # MR3_2: 乘法单位元1
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

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1)

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
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

    # MR15: 类三角函数的周期性（Java 中注释，保持注释）
    # transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput)
    # transformResult15 = func(transformInput15)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput)
    transformResult16 = func(transformInput16)

    # MR19: 输入重复（元素复制） — Java 中注释，保持注释
    # transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2)
    # transformResult19 = func(transformInput19)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput)
    transformResult20 = func(transformInput20)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(transformInput22)

    # ---------------- Assertions ----------------
    # Java 中使用 Arrays.equals 比较数组等价，这里直接用 check.equal 进行列表等价检查。
    # 保留原 Java 注释状态：被注释的断言在 Python 也注释掉。

    # OR1: （Java 注释掉的原断言部分未启用 — 如果需要可取消注释）
    # check.equal(originalResult, transformResult1, "OR1 failed (MR1)")

    # OR2: 注释（Java 中用 assertEquals with delta，保留注释）
    # check.equal(originalResult_plus3, transformResult2, "OR2 failed (MR2)")

    # OR3_1
    # check.equal(originalResult, transformResult3_1, "OR3_1 failed (MR3_1)")

    # OR3_2 (Java 注释)
    # check.is_true(originalResult >= transformResult3_2, "OR3_2 failed (MR3_2)")

    # OR4 (Java 注释)
    # check.equal(originalResult, transformResult4, "OR4 failed (MR4)")

    # OR5 (Java 注释)
    # check.equal(originalResult, transformResult5, "OR5 failed (MR5)")

    # OR6: 源输出和等于后续输出和
    check.equal(originalResult, transformResult6, "OR6 failed (MR6)")

    # OR7_1: 源输出数组等于后续输出数组
    check.equal(originalResult, transformResult7_1, "OR7_1 failed (MR7_1)")

    # OR7_2: 源输出数组等于后续输出数组
    check.equal(originalResult, transformResult7_2, "OR7_2 failed (MR7_2)")

    # OR8: 注释（Java 注释）
    # check.equal(originalResult, transformResult8, "OR8 failed (MR8)")

    # OR9: 注释（Java 注释）
    # check.equal(originalResult_times3, transformResult9, "OR9 failed (MR9)")

    # OR10..OR11..OR13..OR14..OR15..OR16 等 Java 注释保持注释

    # OR12: 源输出数组等于后续数组
    check.equal(originalResult, transformResult12, "OR12 failed (MR12)")

    # OR22: 源输出等于后续输出
    check.equal(originalResult, transformResult22, "OR22 failed (MR22)")


@pytest.mark.parametrize("originalInput", [
    [-1.0, 3.3, 2.0, 6.0, 9.0],
    [2.0, 1.0, 4.6, 4.0, 2.0],
    [4.0, -2.0, 4.0, 6.0, 2.0],
    [9.0, 2.0, 1.0, 5.8, 3.5, 2.3],
    [-1.2, 9.4, 1.0, -3.0, -3.0],
    [8.0, 3.4, 2.5, 6.9, 2.0, 3.0],
    [1.0, 2.0, 3.3, 4.1, -5.0, 6.0],
    [1.0, 2.0, 4.9, 2.4, 7.0, 5.0],
    [1.3, 1.9, 2.0, 4.8, 1.0, 2.0],
    [-2.4, 3.0, 1.0, 4.0, 7.0],
])
def test_cal_AbsoluteDiff_with_func(originalInput):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput)
    applyMR_Assert(originalInput, originalResult)
