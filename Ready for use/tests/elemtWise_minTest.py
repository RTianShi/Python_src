# mutants/tests/test_elemtWise_min_py2_style.py
import copy
from typing import List

import pytest
import pytest_check as check
from mutants import runner
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1

print("test_elemtWise_min_py2_style 执行中")


def sum_int_array(arr: List[int]) -> int:
    """把返回的列表视为 int[]，计算元素之和（模仿 Java 中 sum 校验策略）。"""
    if arr is None:
        return 0
    return sum(int(v) for v in arr)


def applyMR_Assert(originalInput1: List[int], originalInput2: List[int], originalResult: List[int]):
    """
    与 Java 测试中的 OR 断言对应：
    使用 pytest-check 的 check.*（主要使用 check.equal / check.is_true）以收集多个断言失败。
    """
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected into runner.CURRENT_MUTANT_FUNC")
    if func is None:
        return

    # MR1: 元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1)
    transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput2)
    transformResult1 = func(copy.deepcopy(transformInput1_1), copy.deepcopy(transformInput1_2))

    # MR2: 元素常数加法
    transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1)
    transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput2)
    transformResult2 = func(copy.deepcopy(transformInput2_1), copy.deepcopy(transformInput2_2))

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1)
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput2)
    transformResult3_1 = func(copy.deepcopy(transformInput3_1), copy.deepcopy(transformInput3_2))

    # MR3_2: 乘法单位元1
    transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1)
    transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput2)
    transformResult3_2 = func(copy.deepcopy(transformInput3_3), copy.deepcopy(transformInput3_4))

    # MR4: 数组元素取倒数 -> Java 中随后 intValue，这里把生成器结果转 int
    transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1)
    transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput2)
    transformInput4_1_int = [int(x) for x in transformInput4_1]
    transformInput4_2_int = [int(x) for x in transformInput4_2]
    transformResult4 = func(copy.deepcopy(transformInput4_1_int), copy.deepcopy(transformInput4_2_int))

    # MR5: 缩放变换（scale=2）
    transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1, 2)
    transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput2, 2)
    transformResult5 = func(copy.deepcopy(transformInput5_1), copy.deepcopy(transformInput5_2))

    # MR6: 反转
    transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1)
    transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput2)
    transformResult6 = func(copy.deepcopy(transformInput6_1), copy.deepcopy(transformInput6_2))

    # MR7_1: 乘以1（恒等）
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1)
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput2)
    transformResult7_1 = func(copy.deepcopy(transformInput7_1), copy.deepcopy(transformInput7_2))

    # MR7_2: 加0（恒等）
    transformInput7_3 = MetamorphicTestGenerator1.applyMR7_2(originalInput1)
    transformInput7_4 = MetamorphicTestGenerator1.applyMR7_2(originalInput2)
    transformResult7_2 = func(copy.deepcopy(transformInput7_3), copy.deepcopy(transformInput7_4))

    # MR8: 重复输入数组
    transformInput8_1 = MetamorphicTestGenerator1.applyMR8(originalInput1)
    transformInput8_2 = MetamorphicTestGenerator1.applyMR8(originalInput2)
    transformResult8 = func(copy.deepcopy(transformInput8_1), copy.deepcopy(transformInput8_2))

    # MR9: 复合转换一致性 (保留计算)
    transformInput9_1 = MetamorphicTestGenerator1.applyMR9(originalInput1, 1)
    transformInput9_2 = MetamorphicTestGenerator1.applyMR9(originalInput2, 1)
    transformResult9 = func(copy.deepcopy(transformInput9_1), copy.deepcopy(transformInput9_2))

    # MR10: 单调性检验
    transformInput10_1 = MetamorphicTestGenerator1.applyMR10(originalInput1)
    transformInput10_2 = MetamorphicTestGenerator1.applyMR10(originalInput2)
    transformResult10 = func(copy.deepcopy(transformInput10_1), copy.deepcopy(transformInput10_2))

    # MR11: 边界值替换（把最大值替换成0）
    transformInput11_1 = MetamorphicTestGenerator1.applyMR11(originalInput1)
    transformInput11_2 = MetamorphicTestGenerator1.applyMR11(originalInput2)
    transformResult11 = func(copy.deepcopy(transformInput11_1), copy.deepcopy(transformInput11_2))

    # MR12: 数值取反变换
    transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1)
    transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput2)
    transformResult12 = func(copy.deepcopy(transformInput12_1), copy.deepcopy(transformInput12_2))

    # MR13: 微小增量调整 -> 再转 int
    transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1)
    transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput2)
    transformInput13_1_int = [int(x) for x in transformInput13_1]
    transformInput13_2_int = [int(x) for x in transformInput13_2]
    transformResult13 = func(copy.deepcopy(transformInput13_1_int), copy.deepcopy(transformInput13_2_int))

    # MR14: 移除最大值
    transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1)
    transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput2)
    transformResult14 = func(copy.deepcopy(transformInput14_1), copy.deepcopy(transformInput14_2))

    # MR15: 类三角函数周期性 -> 计算但 Java 中未启用断言
    transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1)
    transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput2)
    transformInput15_1_int = [int(x) for x in transformInput15_1]
    transformInput15_2_int = [int(x) for x in transformInput15_2]
    transformResult15 = func(copy.deepcopy(transformInput15_1_int), copy.deepcopy(transformInput15_2_int))

    # MR16: 复制元素
    transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1)
    transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput2)
    transformResult16 = func(copy.deepcopy(transformInput16_1), copy.deepcopy(transformInput16_2))

    # MR19: 输入重复（元素复制）
    transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1, 2)
    transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput2, 2)
    transformResult19 = func(copy.deepcopy(transformInput19_1), copy.deepcopy(transformInput19_2))

    # MR20: 给最小值增加极小量 -> 再转 int
    transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1)
    transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput2)
    transformInput20_1_int = [int(x) for x in transformInput20_1]
    transformInput20_2_int = [int(x) for x in transformInput20_2]
    transformResult20 = func(copy.deepcopy(transformInput20_1_int), copy.deepcopy(transformInput20_2_int))

    # MR22: 恒等变换
    transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1)
    transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput2)
    transformResult22 = func(copy.deepcopy(transformInput22_1), copy.deepcopy(transformInput22_2))

    # ----------------- 对应 Java 测试中启用的 OR 断言（以和的比较为准），使用 check 收集失败 -----------------
    orig_sum = sum_int_array(originalResult)

    # OR2: sum(transformed) >= sum(original)
    check.is_true(sum_int_array(transformResult2) >= orig_sum, "OR2 failed")

    # OR3_1: sum equal
    check.equal(sum_int_array(transformResult3_1), orig_sum, "OR3_1 failed")

    # OR3_2: sum increased or equal
    check.is_true(sum_int_array(transformResult3_2) >= orig_sum, "OR3_2 failed")

    # OR4: sum decreased or equal
    check.is_true(sum_int_array(transformResult4) <= orig_sum, "OR4 failed")

    # OR5: sum increased or equal
    check.is_true(sum_int_array(transformResult5) >= orig_sum, "OR5 failed")

    # OR6: sum equal
    check.equal(sum_int_array(transformResult6), orig_sum, "OR6 failed")

    # OR7_1 / OR7_2: sum equal
    check.equal(sum_int_array(transformResult7_1), orig_sum, "OR7_1 failed")
    check.equal(sum_int_array(transformResult7_2), orig_sum, "OR7_2 failed")

    # OR8: sum increased or equal
    check.is_true(sum_int_array(transformResult8) >= orig_sum, "OR8 failed")

    # OR10: sum increased or equal
    check.is_true(sum_int_array(transformResult10) >= orig_sum, "OR10 failed")

    # OR11: sum decreased or equal
    check.is_true(sum_int_array(transformResult11) <= orig_sum, "OR11 failed")

    # OR12: sum decreased or equal
    check.is_true(sum_int_array(transformResult12) <= orig_sum, "OR12 failed")

    # OR13: sum increased or equal
    check.is_true(sum_int_array(transformResult13) >= orig_sum, "OR13 failed")

    # OR14: sum decreased or equal
    check.is_true(sum_int_array(transformResult14) <= orig_sum, "OR14 failed")

    # OR20: sum increased or equal
    check.is_true(sum_int_array(transformResult20) >= orig_sum, "OR20 failed")

    # OR22: sum equal
    check.equal(sum_int_array(transformResult22), orig_sum, "OR22 failed")


# 参数化与 Java 测例对应（两个输入数组）
@pytest.mark.parametrize("a,b", [
    ([1, 2, 3], [1, 2, 3]),
    ([4, 5, 6, 7], [4, 5, 6, 8]),
    ([-1, 0, 1], [-1, 0, 2]),
    ([3, -4, 5, 6], [3, -4, 5, 7]),
    ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
    ([5, 4, 3, 2], [5, 4, 3, 1]),
    ([-7, 8, 9], [-7, 8, 10]),
    ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
    ([1, 2, 3], [0, 2, 3]),
    ([0, 0, 0, 1], [0, 0, 0, 1]),
])
def test_elemtWise_min_with_func(a, b):
    func = runner.CURRENT_MUTANT_FUNC
    check.is_not_none(func, "mutant function not injected")
    if func is None:
        return

    in1 = copy.deepcopy(a)
    in2 = copy.deepcopy(b)
    originalResult = func(in1, in2)
    applyMR_Assert(in1, in2, originalResult)
