# mutants/tests/test_euc_dist_py2_style.py
import copy
from typing import List

import pytest
import pytest_check as check
from mutants import runner
from MetamorphicTestGenerator3 import MetamorphicTestGenerator3

print("test_euc_dist_py2_style 执行中")

TOL = 1e-9  # 对应 Java delta

def almost_equal(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol

def applyMR_Assert(originalInput1_1: List[float], originalInput1_2: List[float], originalResult: float):
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected")
    if func is None:
        return

    # MR1: 数组元置换
    transformInput1_1 = MetamorphicTestGenerator3.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator3.applyMR1(originalInput1_2)
    transformResult1 = func(copy.deepcopy(transformInput1_1), copy.deepcopy(transformInput1_2))
    # MR2: 数组元素常数加法
    transformInput2_1 = MetamorphicTestGenerator3.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator3.applyMR2(originalInput1_2)
    transformResult2 = func(copy.deepcopy(transformInput2_1), copy.deepcopy(transformInput2_2))
    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator3.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator3.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(copy.deepcopy(transformInput3_1), copy.deepcopy(transformInput3_2))
    # MR3_2: 乘法单位元1
    transformInput3_3 = MetamorphicTestGenerator3.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator3.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(copy.deepcopy(transformInput3_3), copy.deepcopy(transformInput3_4))
    # MR4: 数组元素取倒数
    transformInput4_1 = MetamorphicTestGenerator3.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator3.applyMR4(originalInput1_2)
    transformResult4 = func(copy.deepcopy(transformInput4_1), copy.deepcopy(transformInput4_2))
    # MR5: 缩放变换
    transformInput5_1 = MetamorphicTestGenerator3.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator3.applyMR5(originalInput1_2, 2)
    transformResult5 = func(copy.deepcopy(transformInput5_1), copy.deepcopy(transformInput5_2))
    # MR6: 数组反转
    transformInput6_1 = MetamorphicTestGenerator3.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator3.applyMR6(originalInput1_2)
    transformResult6 = func(copy.deepcopy(transformInput6_1), copy.deepcopy(transformInput6_2))
    # MR7_1 / MR7_2: 恒等变换
    transformInput7_1 = MetamorphicTestGenerator3.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator3.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(copy.deepcopy(transformInput7_1), copy.deepcopy(transformInput7_2))
    transformInput7_3 = MetamorphicTestGenerator3.applyMR7_2(originalInput1_1)
    transformInput7_4 = MetamorphicTestGenerator3.applyMR7_2(originalInput1_2)
    transformResult7_2 = func(copy.deepcopy(transformInput7_3), copy.deepcopy(transformInput7_4))
    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator3.applyMR8(originalInput1_1)
    transformInput8_2 = MetamorphicTestGenerator3.applyMR8(originalInput1_2)
    transformResult8 = func(copy.deepcopy(transformInput8_1), copy.deepcopy(transformInput8_2))
    # MR9: 复合转换一致性
    transformInput9_1 = MetamorphicTestGenerator3.applyMR9(originalInput1_1, 1)
    transformInput9_2 = MetamorphicTestGenerator3.applyMR9(originalInput1_2, 1)
    transformResult9 = func(copy.deepcopy(transformInput9_1), copy.deepcopy(transformInput9_2))
    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator3.applyMR10(originalInput1_1)
    transformInput10_2 = MetamorphicTestGenerator3.applyMR10(originalInput1_2)
    transformResult10 = func(copy.deepcopy(transformInput10_1), copy.deepcopy(transformInput10_2))
    # MR12: 数值取反
    transformInput12_1 = MetamorphicTestGenerator3.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator3.applyMR12(originalInput1_2)
    transformResult12 = func(copy.deepcopy(transformInput12_1), copy.deepcopy(transformInput12_2))
    # MR13: 微小增量调整
    transformInput13_1 = MetamorphicTestGenerator3.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator3.applyMR13(originalInput1_2)
    transformResult13 = func(copy.deepcopy(transformInput13_1), copy.deepcopy(transformInput13_2))
    # MR16: 重复值稳健性
    transformInput16_1 = MetamorphicTestGenerator3.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator3.applyMR16(originalInput1_2)
    transformResult16 = func(copy.deepcopy(transformInput16_1), copy.deepcopy(transformInput16_2))
    # MR19: 输入重复
    transformInput19_1 = MetamorphicTestGenerator3.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator3.applyMR19(originalInput1_2, 2)
    transformResult19 = func(copy.deepcopy(transformInput19_1), copy.deepcopy(transformInput19_2))
    # MR20: 边界值灵敏度
    transformInput20_1 = MetamorphicTestGenerator3.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator3.applyMR20(originalInput1_2)
    transformResult20 = func(copy.deepcopy(transformInput20_1), copy.deepcopy(transformInput20_2))
    # MR22: 恒等变换
    transformInput22_1 = MetamorphicTestGenerator3.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator3.applyMR22(originalInput1_2)
    transformResult22 = func(copy.deepcopy(transformInput22_1), copy.deepcopy(transformInput22_2))

    # ---------------- Assertions ----------------
    # 对应 Java 中启用的断言
    check.is_true(almost_equal(originalResult, transformResult2), f"OR2 failed: {originalResult} vs {transformResult2}")
    check.is_true(originalResult == transformResult3_1, f"OR3_1 failed: {originalResult} vs {transformResult3_1}")
    check.is_true(originalResult == transformResult3_2, f"OR3_2 failed: {originalResult} vs {transformResult3_2}")
    check.is_true(originalResult >= transformResult4, f"OR4 failed: {originalResult} vs {transformResult4}")
    check.is_true(originalResult <= transformResult5, f"OR5 failed: {originalResult} vs {transformResult5}")
    check.is_true(almost_equal(originalResult, transformResult6), f"OR6 failed: {originalResult} vs {transformResult6}")
    check.is_true(almost_equal(originalResult, transformResult7_1), f"OR7_1 failed: {originalResult} vs {transformResult7_1}")
    check.is_true(almost_equal(originalResult, transformResult7_2), f"OR7_2 failed: {originalResult} vs {transformResult7_2}")
    check.is_true(originalResult <= transformResult8, f"OR8 failed: {originalResult} vs {transformResult8}")
    check.is_true(almost_equal(originalResult, transformResult10), f"OR10 failed: {originalResult} vs {transformResult10}")
    check.is_true(almost_equal(originalResult, transformResult12), f"OR12 failed: {originalResult} vs {transformResult12}")
    check.is_true(almost_equal(originalResult, transformResult13), f"OR13 failed: {originalResult} vs {transformResult13}")
    check.is_true(originalResult <= transformResult16, f"OR16 failed: {originalResult} vs {transformResult16}")
    check.is_true(originalResult <= transformResult19, f"OR19 failed: {originalResult} vs {transformResult19}")
    check.is_true(almost_equal(originalResult, transformResult20), f"OR20 failed: {originalResult} vs {transformResult20}")
    check.is_true(almost_equal(originalResult, transformResult22), f"OR22 failed: {originalResult} vs {transformResult22}")


# ---------------- Parameterized Test Cases ----------------
@pytest.mark.parametrize("originalInput1_1, originalInput1_2", [
    ([1.234, 2.56, 3.78], [1.234, 2.56, 3.780]),
    ([-1.11, 4.5, 3.001], [-1.1101, 4.5001, 3.0011]),
    ([-1.11, 4.5, 3.001], [7.0009, -3.1201, 0.9901]),
    ([7.001, -3.12, 0.99], [7.0009, -3.1201, 0.9901]),
    ([5.0, -8.765, 1.222], [5.0, -8.765, 1.222]),
    ([5.0, -8.765, 1.222], [2.333, 4.444, 1.0]),
    ([2.333, 4.444, 1.0], [2.333, 4.444, 1.0]),
    ([6.789, 1.23, -5.67], [0.1, -3.456, 2.789]),
    ([6.789, 1.23, -5.67], [6.7891, 1.23, -5.6699]),
    ([0.1, -3.456, 2.789], [0.1, -3.456, 2.789]),
])
def test_euc_dist_with_func(originalInput1_1, originalInput1_2):
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected")
    if func is None:
        return
    in1 = copy.deepcopy(originalInput1_1)
    in2 = copy.deepcopy(originalInput1_2)
    originalResult = func(in1, in2)
    applyMR_Assert(in1, in2, originalResult)
