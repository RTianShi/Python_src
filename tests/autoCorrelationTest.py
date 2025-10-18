# test_autoCorrelation_float.py
from mutants import runner
from MetamorphicTestGenerator4 import MetamorphicTestGenerator4
from src.autoCorrelation import autoCorrelation
import pytest
import pytest_check as check

def applyMR_Assert(originalInput, originalResult, lag, mean, variance):
    func = autoCorrelation
    # 打印换行（与 Java 中的 System.out.println("\n"); 对应）
    print("\n")
    hasFailed = False
    delta = 1e-9  # 浮点比较容差

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, lag, mean, variance)

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
    transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, lag, mean, variance)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput)
    transformResult22 = func(transformInput22, lag, mean, variance)


# ---------------- Assertions ----------------
# 与 Java 里相同：对启用的 MR 进行相同的断言（数组等价）
    check.is_true(abs(originalResult - transformResult7_1) <= delta, "MR7_1 failed")
    check.is_true(abs(originalResult - transformResult7_2) <= delta, "MR7_2 failed")
    check.is_true(abs(originalResult - transformResult22) <= delta, "MR22 failed")

@pytest.mark.parametrize("originalInput, lag, mean, variance", [
    ([1.2, 2.3, 3.5, 4.7], 1, 2.925, 1.712),
    ([-1.1, 0.5, -0.3, 2.0, 3.7], 1, 0.96, 2.9264),
    ([3.14, -2.71, 1.61, 0.57, -3.14], 1, -0.106, 6.82),
    # ([0.0, 0.0, 0.0, 0.0], 1, 0.0, 0.0),
    ([-2.5, 2.5, -2.5, 2.5, -2.5], 1, -5.0, 6.0),
    ([1.11, 2.22, 3.33], 1, 2.22, 0.8214),
    ([4.4, -5.5, 6.6, -7.7], 1, -0.55, 37.8125),
    ([-1.2, -2.3, -1.5, -2.7], 1, -1.925, 0.3619),
    ([5.5, 3.2, 4.1, 2.8, 1.9], 1, 3.5, 1.5),
    ([0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 1, 3.0, 2.9167),
])
def test_autoCorrelation_with_func(originalInput, lag, mean, variance):
    func = autoCorrelation
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, lag, mean, variance)
    applyMR_Assert(originalInput, originalResult, lag, mean, variance)
