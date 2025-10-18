# test_bi_SearchFromTo.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, originalResult, key, from_idx, to_idx):
    # 对应 Java 中的 System.out.println("\n");
    print("\n")
    hasFailed = False

    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"

    # MR3_1: 加法单位元0

    transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1, key, from_idx, to_idx)
    check.equal(originalResult, transformResult3_1, "MR3_1 failed")


    # MR3_2: 乘法单位元1
    transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2, key, from_idx, to_idx)
    check.equal(originalResult, transformResult3_2, "MR3_2 failed")

    # MR4: 数组元素取倒数
    transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput)
    transformResult4 = func(transformInput4, key, from_idx, to_idx)
    check.is_true(originalResult >= transformResult4, "MR4 failed")

    # MR7_1: 中立操作（乘1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, key, from_idx, to_idx)
    check.equal(originalResult, transformResult7_1, "MR7_1 failed")

    # MR7_2: 中立操作（加0）
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, key, from_idx, to_idx)
    check.equal(originalResult, transformResult7_2, "MR7_2 failed")

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput)
    transformResult8 = func(transformInput8, key, from_idx, to_idx)
    check.is_true(originalResult <= transformResult8, "MR8 failed")

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput)
    transformResult10 = func(transformInput10, key, from_idx, to_idx)
    check.is_true(originalResult >= transformResult10, "MR10 failed")

    # MR11: 边界值替换
    transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput)
    transformResult11 = func(transformInput11, key, from_idx, to_idx)
    check.is_true(originalResult >= transformResult11, "MR11 failed")

    # MR13: 微小增量调整
    transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput)
    transformResult13 = func(transformInput13, key, from_idx, to_idx)
    check.is_true(originalResult >= transformResult13, "MR13 failed")

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(transformInput22, key, from_idx, to_idx)
    check.equal(originalResult, transformResult22, "MR22 failed")


@pytest.mark.parametrize("originalInput, key, from_idx, to_idx", [
    ([1.2, 2.3, 3.5, 4.7], 1.2, 0, 3),
    ([-1.1, 0.5, -0.3, 2.0, 3.7], 2.0, 0, 4),
    ([3.14, -2.71, 1.61, 0.57, -3.14], 1.61, 0, 4),
    ([0.0, 0.0, 0.0, 0.0], 0.0, 0, 3),
    ([-2.5, 2.5, -2.5, 2.5, -2.5], 2.5, 0, 4),
    ([1.11, 2.22, 3.33], 1.2, 0, 2),
    ([4.4, -5.5, 6.6, -7.7], 4.4, 0, 3),
    ([-1.2, -2.3, -1.5, -2.7], 1.2, 0, 3),
    ([5.5, 3.2, 4.1, 2.8, 1.9], 4.1, 0, 4),
    ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 1.5, 0, 5),
])
def test_bi_SearchFromTo_with_func(originalInput, key, from_idx, to_idx):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, key, from_idx, to_idx)
    applyMR_Assert(originalInput, originalResult, key, from_idx, to_idx)
