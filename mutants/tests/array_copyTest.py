# test_array_copy.py
from mutants import runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, originalResult):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # -------------------------------------------------
    # 与 Java 源文件中注释状态保持一致：那些在 Java 中被注释的 MR 仍然保持注释状态
    # MR1: 数组元素置换（打乱顺序）
    # transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput)
    # transformResult1 = func(transformInput1)

    # MR2: 数组元素常数加法
    # transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput)
    # transformResult2 = func(transformInput2)

    # MR3_1: 加法单位元 0
    # transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    # transformResult3_1 = func(transformInput3_1)

    # MR3_2: 乘法单位元 1
    # transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    # transformResult3_2 = func(transformInput3_2)

    # MR4: 数组元素取倒数（Java 中有 Double->int 的转换）
    # transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput)
    # transformInput4_1 = [int(x) for x in transformInput4]
    # transformResult4 = func(transformInput4_1)

    # MR5: 数组缩放变换
    # transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    # transformResult5 = func(transformInput5)

    # MR6: 数组反转变换
    # transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    # transformResult6 = func(transformInput6)

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1)

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2)

    # MR8: 重复输入数组
    # transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput)
    # transformResult8 = func(transformInput8)

    # MR9: 复合转换一致性
    # transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3)
    # transformResult9 = func(transformInput9)

    # MR10: 单调性检验
    # transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput)
    # transformResult10 = func(transformInput10)

    # MR11: 边界值替换(把最大值替换成0)
    # transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput)
    # transformResult11 = func(transformInput11)

    # MR12: 数值取反变换
    # transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput)
    # transformResult12 = func(transformInput12)

    # MR13: 微小增量调整
    # transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput)
    # transformInput13_1 = [int(x) for x in transformInput13]
    # transformResult13 = func(transformInput13_1)

    # MR14: 移除元素的效果（移除最大值）
    # transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    # transformResult14 = func(transformInput14)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    # transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    # transformResult16 = func(transformInput16)

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    # transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2)
    # transformResult19 = func(transformInput19)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    # transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    # transformInput20_1 = [int(x) for x in transformInput20]
    # transformResult20 = func(transformInput20_1)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = func(transformInput22)
    # -------------------------------------------------

    # ---------------- Assertions ----------------
    # 与 Java 里相同：对启用的 MR 进行相同的断言（数组等价）
    check.equal(originalResult, transformResult7_1, "OR7_1 failed (MR7_1)")
    check.equal(originalResult, transformResult7_2, "OR7_2 failed (MR7_2)")
    check.equal(originalResult, transformResult22, "OR22 failed (MR22)")

    # 注：其它 MR 的断言在 Java 中被注释掉，这里也保持注释状态以便日后开启
    # e.g.
    # check.equal(originalResult, transformResult1, "OR1 failed (MR1)")
    # check.equal(originalResult, transformResult2, "OR2 failed (MR2)")

@pytest.mark.parametrize("originalInput", [
    [1, 3, 2, 6, 9],
    [2, 1, 4, 4, 2],
    [4, -2, 4, 6, 2],
    [9, 2, 1, 5, 3, 2],
    [-1, 9, 1, -3, -3],
    [8, 3, 2, 6, 2, 3],
    [1, 2, 3, 4, -5, 6],
    [1, 2, 4, 2, 7, 5],
    [1, 1, 2, 4, 1, 2],
    [-2, 3, 1, 4, 7],
])
def test_array_copy_with_func(originalInput):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput)
    applyMR_Assert(originalInput, originalResult)
