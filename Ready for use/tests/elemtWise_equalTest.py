# mutants/tests/test_elemtWise_equal.py
import copy
from typing import List

import pytest
import pytest_check as check
import mutants.runner as runner

# 假设 MetamorphicTestGenerator1 在项目中有对应的 Python 模块
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1


def bool_array_equal(a, b) -> bool:
    """比较两个 boolean-like sequences 是否相等（支持 list/tuple/array 等）"""
    if a is None or b is None:
        return a is b
    return list(a) == list(b)


def applyMR_Assert(originalInput1_1: List[int], originalInput1_2: List[int], originalResult: List[bool]):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant function not injected into runner.CURRENT_MUTANT_FUNC"

    # MR1: 元置换（打乱顺序）
    transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1_1)
    transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput1_2)
    transformResult1 = func(transformInput1_1, transformInput1_2)

    # MR2: 元素常数加法
    transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1_1)
    transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput1_2)
    transformResult2 = func(transformInput2_1, transformInput2_2)

    # MR3_1: 加法单位元0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_1)
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_2)
    transformResult3_1 = func(transformInput3_1, transformInput3_2)

    # MR3_2: 乘法单位元1
    transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_1)
    transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_2)
    transformResult3_2 = func(transformInput3_3, transformInput3_4)

    # MR4: 数组元素取倒数（Java 中转换过后又转成 Integer[]，这里直接 call）
    transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1_1)
    transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput1_2)
    # 在 Java 中他们把 Double[] -> Integer[] 再调用，这里假设生成器给出与目标函数兼容的类型
    transformResult4 = func(transformInput4_1, transformInput4_2)

    # MR5: 缩放变换
    transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1_1, 2)
    transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput1_2, 2)
    transformResult5 = func(transformInput5_1, transformInput5_2)

    # MR6: 反转
    transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1_1)
    transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput1_2)
    transformResult6 = func(transformInput6_1, transformInput6_2)

    # MR7_1: 乘1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_1)
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_2)
    transformResult7_1 = func(transformInput7_1, transformInput7_2)

    # MR7_2: 加0
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

    # MR11: 边界值替换
    transformInput11_1 = MetamorphicTestGenerator1.applyMR11(originalInput1_1)
    transformInput11_2 = MetamorphicTestGenerator1.applyMR11(originalInput1_2)
    transformResult11 = func(transformInput11_1, transformInput11_2)

    # MR12: 数值取反
    transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1_1)
    transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput1_2)
    transformResult12 = func(transformInput12_1, transformInput12_2)

    # MR13: 微小增量调整（Java 中又转回 Integer[]）
    transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1_1)
    transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput1_2)
    transformResult13 = func(transformInput13_1, transformInput13_2)

    # MR14: 移除最大值
    transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1_1)
    transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput1_2)
    transformResult14 = func(transformInput14_1, transformInput14_2)

    # MR15: π - x -> Java 中再转 Integer[]
    transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1_1)
    transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput1_2)
    transformResult15 = func(transformInput15_1, transformInput15_2)

    # MR16: 复制第一个元素
    transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1_1)
    transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput1_2)
    transformResult16 = func(transformInput16_1, transformInput16_2)

    # MR19: 输入重复（重复第一个元素多次）
    transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1_1, 2)
    transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput1_2, 2)
    transformResult19 = func(transformInput19_1, transformInput19_2)

    # MR20: 给最小值增加极小值（Java 中再转 Integer[]）
    transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1_1)
    transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput1_2)
    transformResult20 = func(transformInput20_1, transformInput20_2)

    # MR22: 恒等变换
    transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1_1)
    transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput1_2)
    transformResult22 = func(transformInput22_1, transformInput22_2)

    # --------------- 与 Java 测试中启用的 OR 对应的断言 ---------------
    # Java 测试里对很多 MR 使用了 Arrays.equals(...) 的断言，我们在这里将它们转换为 bool_array_equal

    # OR2: 源输出等于 MR2 输出
    check.is_true(bool_array_equal(originalResult, transformResult2), "MR2 failed")

    # OR4: 源输出等于 MR4 输出
    check.is_true(bool_array_equal(originalResult, transformResult4), "MR4 failed")

    # OR5: 源输出等于 MR5 输出
    check.is_true(bool_array_equal(originalResult, transformResult5), "MR5 failed")

    # OR6: 源输出等于 MR6 输出
    check.is_true(bool_array_equal(originalResult, transformResult6), "MR6 failed")

    # OR7_1 / OR7_2: 恒等变换 -> 相等
    check.is_true(bool_array_equal(originalResult, transformResult7_1), "MR7_1 failed")
    check.is_true(bool_array_equal(originalResult, transformResult7_2), "MR7_2 failed")

    # OR10: 源输出等于 MR10 输出
    check.is_true(bool_array_equal(originalResult, transformResult10), "MR10 failed")

    # OR12: 源输出等于 MR12 输出
    check.is_true(bool_array_equal(originalResult, transformResult12), "MR12 failed")

    # OR22: 源输出等于 MR22 输出
    check.is_true(bool_array_equal(originalResult, transformResult22), "MR22 failed")


@pytest.mark.parametrize("a,b", [
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
def test_elemtWise_equal_with_func(a, b):
    func = runner.CURRENT_MUTANT_FUNC
    assert func is not None, "mutant function not injected"

    in1 = copy.deepcopy(a)
    in2 = copy.deepcopy(b)
    originalResult = func(in1, in2)
    applyMR_Assert(in1, in2, originalResult)
