# 转换自 Java 的 array_calcTest -> 与第一个程序相同的 Python 测试格式
# 保留注释状态与已启用的 MR（与原 Java 保持一致：仅 MR7_1, MR7_2, MR22 被启用）
from mutants import runner
from MetamorphicTestGenerator2 import MetamorphicTestGenerator2
import pytest
import pytest_check as check

print("test_array_calc 执行了")


def applyMR_Assert(originalInput, originalResult, k):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR1:数组元置换（打乱顺序）
    # transformInput1 = MetamorphicTestGenerator2.applyMR1(originalInput)
    # transformResult1 = func(transformInput1, 3)

    # MR2:数组元素常数加法
    # transformInput2 = MetamorphicTestGenerator2.applyMR2(originalInput)
    # transformResult2 = func(transformInput2, k)

    # MR3_1:加入单位元不变性（加法的单位元0）
    # transformInput3_1 = MetamorphicTestGenerator2.applyMR3_1(originalInput)
    # transformResult3_1 = func(transformInput3_1, k)

    # MR3_2:加入单位元不变性（乘法的单位元1）
    # transformInput3_2 = MetamorphicTestGenerator2.applyMR3_2(originalInput)
    # transformResult3_2 = func(transformInput3_2, k)

    # MR4:数组元素取倒数
    # transformInput4 = MetamorphicTestGenerator2.applyMR4(originalInput)
    # transformInput4_1 = [int(x) for x in transformInput4]
    # transformResult4 = func(transformInput4_1, 2)

    # MR5:数组缩放变换
    # transformInput5 = MetamorphicTestGenerator2.applyMR5(originalInput, 2)
    # transformResult5 = func(transformInput5, 2)

    # MR6:数组反转变换
    # transformInput6 = MetamorphicTestGenerator2.applyMR6(originalInput)
    # transformResult6 = func(transformInput6, 2)

    # MR7_1:中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator2.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, k)

    # MR7_2:中立操作的恒等变换（所有元素加上0）
    transformInput7_2 = MetamorphicTestGenerator2.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, k)

    # MR8:重复输入数组
    # transformInput8 = MetamorphicTestGenerator2.applyMR8(originalInput)
    # transformResult8 = func(transformInput8, 2)

    # MR9:复合转换一致性
    # transformInput9 = MetamorphicTestGenerator2.applyMR9(originalInput, 3)
    # transformResult9 = func(transformInput9, 2)

    # MR10:单调性检验
    # transformInput10 = MetamorphicTestGenerator2.applyMR10(originalInput)
    # transformResult10 = func(transformInput10, 2)

    # MR11:边界值替换(把最大值替换成0)
    # transformInput11 = MetamorphicTestGenerator2.applyMR11(originalInput)
    # transformResult11 = func(transformInput11, 2)

    # MR12:数值取反变换
    # transformInput12 = MetamorphicTestGenerator2.applyMR12(originalInput)
    # transformResult12 = func(transformInput12, 2)

    # MR13:微小增量调整
    # transformInput13 = MetamorphicTestGenerator2.applyMR13(originalInput)
    # transformInput13_1 = [int(x) for x in transformInput13]
    # transformResult13 = func(transformInput13_1, 2)

    # MR14:移除元素的效果（移除最大值）
    # transformInput14 = MetamorphicTestGenerator2.applyMR14(originalInput)
    # transformResult14 = func(transformInput14, 2)

    # MR16:重复值稳健性(复制输入中的一个元素)
    # transformInput16 = MetamorphicTestGenerator2.applyMR16(originalInput)
    # transformResult16 = func(transformInput16, 2)

    # MR20:边界值灵敏度（给最小值增加一个极小值）
    # transformInput20 = MetamorphicTestGenerator2.applyMR20(originalInput)
    # transformInput20_1 = [int(x) for x in transformInput20]
    # transformResult20 = func(transformInput20_1, 2)

    # MR22:应用恒等变换
    transformInput22 = MetamorphicTestGenerator2.applyMR22(originalInput)
    transformResult22 = func(transformInput22, k)

    # ---------------------------------------------------------
    # 断言（保留 Java 原注释和只启用原来启用的断言）
    # OR1:和应该保持不变
    # assert originalResult == transformResult1
    # OR2:源输出和加上n*3等于后续输入
    # assert originalResult == transformResult2
    # OR3_1:数组应该保持不变
    # assert originalResult == transformResult3_1
    # OR3_2:数组应该保持不变
    # assert originalResult == transformResult3_2
    # OR4:和应该减少或保持不变
    # assert originalResult == transformResult4
    # OR5:源输出和乘以2等于后续输出
    # assert originalResult == transformResult5
    # OR6:源输出和等于后续输出和
    # assert originalResult == transformResult6

    # OR7_1:源输出数组和后续输出数组保持不变
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")
    # OR7_2:源输出数组和后续输出数组保持不变
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")

    # OR8:源输出*2等于后续输出
    # assert originalResult == transformResult8
    # OR9:源输出*3等于后续输出
    # assert originalResult == transformResult9
    # OR10:源输出小于等于后续输出
    # assert originalResult == transformResult10
    # OR11:源输出大于等于后续输出
    # assert originalResult == transformResult11
    # OR12:源输出负数等于后续输出
    # assert originalResult == transformResult12
    # OR13:源输出小于等于等于后续输出
    # assert originalResult == transformResult13
    # OR14:源输出大于等于等于后续输出
    # assert originalResult == transformResult14
    # OR15:源输出大于等于等于后续输出
    # assert originalResult >= transformResult15
    # OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
    # assert originalResult <= transformResult16
    # OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
    # assert originalResult <= transformResult16
    # OR20:源输出小于等于后续输出
    # assert originalResult <= transformResult20
    # OR22:源输出等于后续输出
    check.equal(originalResult, transformResult22, "MR22 failed")


# 将 Java 的十个 @Test 转为 parametrize（保持每个 case 的 k 值）
@pytest.mark.parametrize("originalInput,k", [
    ([1, 3, 2, 6, 9], 2),
    ([2, 1, 4, 4, 2], 2),
    ([4, -2, 4, 6, 2], 2),
    ([9, 2, 1, 5, 3, 2], 2),
    ([-1, 9, 1, -3, -3], 1),
    ([8, 3, 2, 6, 2, 3], 3),
    ([1, 2, 3, 4, -5, 6], 4),
    ([1, 2, 4, 2, 7, 5], 2),
    ([1, 1, 2, 4, 1, 2], 2),
    ([-2, 3, 1, 4, 7], 2),
])

def test_array_calc_with_func(originalInput, k):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, k)
    applyMR_Assert(originalInput, originalResult, k)
