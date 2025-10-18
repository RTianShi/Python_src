import copy
import pytest
import pytest_check as check
import mutants.runner as runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1

print("test_dec_array 执行了")


def sum_array(arr):
    """计算整数列表的和（与 Java 的 sum(Integer[]) 行为一致）"""
    if arr is None:
        return 0
    return sum(int(x) for x in arr)


def applyMR_Assert(originalInput, k, originalResult):
    """
    originalInput: List[int] - a COPY of the original input (so transforms can mutate safely)
    k: int
    originalResult: List[int] - result from func(originalInput_original, k)
    """
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput)
    transformResult1 = func(transformInput1, k)

    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput)
    transformResult2 = func(transformInput2, k)

    # MR3_1: 加入单位元不变性（加法的单位元0）
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1, k)

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2, k)

    # MR4: 数组元素取倒数 (返回 float list -> 转为 int list)
    transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput)
    transformInput4_1 = [int(x) for x in transformInput4]
    transformResult4 = func(transformInput4_1, k)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5, k)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    transformResult6 = func(transformInput6, k)

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, k)

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
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

    # MR13: 微小增量调整 (float -> int)
    transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput)
    transformInput13_1 = [int(x) for x in transformInput13]
    transformResult13 = func(transformInput13_1, k)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    transformResult14 = func(transformInput14, k)

    # MR15: 类三角函数的周期性 (被注释于 Java 版)
    # transformInput15 = MetamorphicTestGenerator1.applyMR15(originalInput)
    # transformResult15 = func(transformInput15, k)

    # MR16: 重复值稳健性(复制输入中的一个元素)
    transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    transformResult16 = func(transformInput16, k)

    # MR19: 输入重复（元素复制）(被注释于 Java 版)
    # transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2)
    # transformResult19 = func(transformInput19, k)

    # MR20: 边界值灵敏度（给最小值增加一个极小值）（float -> int）
    transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    transformInput20_1 = [int(x) for x in transformInput20]
    transformResult20 = func(transformInput20_1, k)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = func(transformInput22, k)

    # ---------------- Assertions ----------------
    # OR1: 和应该保持不变
    check.equal(sum_array(transformResult1), sum_array(originalResult), "MR1 failed")

    # OR2: 和应该增加或保持不变
    check.is_true(sum_array(transformResult2) >= sum_array(originalResult), "MR2 failed")

    # OR3_1: 数组应该保持不变 (注释)
    # check.equal(sum_array(transformResult3_1), sum_array(originalResult), "MR3_1 failed")

    # OR3_2: 数组应该保持不变 (注释)
    # check.equal(sum_array(transformResult3_2), sum_array(originalResult), "MR3_2 failed")

    # OR4: 和应该减少或保持不变
    check.is_true(sum_array(transformResult4) <= sum_array(originalResult), "MR4 failed")

    # OR5: 和应该增加或保持不变
    check.is_true(sum_array(transformResult5) >= sum_array(originalResult), "MR5 failed")

    # OR6: 源输出和等于后续输出和
    check.equal(sum_array(transformResult6), sum_array(originalResult), "MR6 failed")

    # OR7_1: 源输出数组和后续输出数组保持不变
    check.equal(sum_array(transformResult7_1), sum_array(originalResult), "MR7_1 failed")

    # OR7_2: 源输出数组和后续输出数组保持不变
    check.equal(sum_array(transformResult7_2), sum_array(originalResult), "MR7_2 failed")

    # OR8: 注释（Java 中注释）
    # check.equal(sum_array(transformResult8), sum_array(originalResult), "MR8 failed")

    # OR9: 和应该增加或保持不变
    check.is_true(sum_array(transformResult9) >= sum_array(originalResult), "MR9 failed")

    # OR10: 和应该增加或保持不变
    check.is_true(sum_array(transformResult10) >= sum_array(originalResult), "MR10 failed")

    # OR11: 注释
    # check.equal(sum_array(transformResult11), sum_array(originalResult), "MR11 failed")

    # OR12: 注释
    # check.equal(sum_array(transformResult12), sum_array(originalResult), "MR12 failed")

    # OR13: 注释
    # check.equal(sum_array(transformResult13), sum_array(originalResult), "MR13 failed")

    # OR14: 注释
    # check.equal(sum_array(transformResult14), sum_array(originalResult), "MR14 failed")

    # OR15: 注释 (Java 中注释)
    # check.is_true(sum_array(transformResult15) <= sum_array(originalResult))

    # OR16: 注释 (Java 中注释)
    # check.is_true(sum_array(transformResult16) >= sum_array(originalResult))

    # OR19: 注释
    # check.is_true(sum_array(transformResult16) >= sum_array(originalResult))

    # OR20: 注释
    # check.is_true(sum_array(transformResult20) >= sum_array(originalResult))

    # OR22: 源输出等于后续输出（数组完全相等在 Java 中用 Arrays.equals；这里用和比较）
    check.equal(sum_array(transformResult22), sum_array(originalResult), "MR22 failed")


@pytest.mark.parametrize("originalInput,k", [
    ([1, 2, 3, 4, 5], -5),
    ([7, 7, 7], 1),
    ([6, 6, 6], 1),
    ([5, 5, 5], 1),
    ([1, 1, 1], 0),
    ([100, 80, 60, 40, 20], -1),
    ([5, 15, 25], -1),
    ([4, 4, 4, 4, 4], 1),
    ([8, 6, 4], -1),
    ([2, 2, 2], 1),
])
def test_dec_array_with_func(originalInput, k):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    # 保持与 Java 版相同的 input copy 语义
    originalInput_copy = copy.deepcopy(originalInput)
    originalResult = func(originalInput, k)
    applyMR_Assert(originalInput_copy, k, originalResult)
