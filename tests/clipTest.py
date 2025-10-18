# 不需要 fixture 注入
from textual.events import Print
from mutants import runner
from src.clip import clip
from test_mutants_runner import CURRENT_MUTANT_FUNC
from MetamorphicTestGenerator1 import MetamorphicTestGenerator1
import pytest
import pytest_check as check

print("test_clip 执行了")

def applyMR_Assert(originalInput, originalResult):
    func = clip
    assert func is not None, "mutant_func 没有被注入"

    # MR1: 数组元置换（打乱顺序）
    transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput)
    transformResult1 = func(transformInput1, 1, 5)

    # MR2: 数组元素常数加法
    transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput)
    transformResult2 = func(transformInput2, 1, 5)

    # MR3_1: 加法单位元 0
    transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput)
    transformResult3_1 = func(transformInput3_1, 1, 5)

    # MR3_2: 乘法单位元 1
    transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput)
    transformResult3_2 = func(transformInput3_2, 1, 5)

    # MR5: 数组缩放变换
    transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2)
    transformResult5 = func(transformInput5, 1, 5)

    # MR6: 数组反转变换
    transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput)
    transformResult6 = func(transformInput6, 1, 5)

    # MR7_1: 所有元素乘以1
    transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput)
    transformResult7_1 = func(transformInput7_1, 1, 5)

    # MR7_2: 所有元素加0
    transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput)
    transformResult7_2 = func(transformInput7_2, 1, 5)

    # MR8: 重复输入数组
    transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput)
    transformResult8 = func(transformInput8, 1, 5)

    # MR9: 复合转换一致性
    transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3)
    transformResult9 = func(transformInput9, 1, 5)

    # MR10: 单调性检验
    transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput)
    transformResult10 = func(transformInput10, 1, 5)

    # MR11: 边界值替换(把最大值替换成0)
    transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput)
    transformResult11 = func(transformInput11, 1, 5)

    # MR14: 移除元素的效果（移除最大值）
    transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput)
    transformResult14 = func(transformInput14, 1, 5)

    # MR16: 重复值稳健性
    transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput)
    transformResult16 = func(transformInput16, 1, 5)

    # MR19: 插入重复元素（Java 里你使用 applyMR19）
    transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2)
    transformResult19 = func(transformInput19, 1, 5)

    # MR20: 边界值灵敏度（可能由 Double 返回，需要转换为 int 列表）
    transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput)
    transformInput20_1 = [int(x) for x in transformInput20]
    transformResult20 = func(transformInput20_1, 1, 5)

    # MR22: 应用恒等变换
    transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput)
    transformResult22 = func(transformInput22, 1, 5)

    # ---------- 辅助：把结果当作列表，比较 sum ----------
    # originalResult 以及 transformResultX 都被假设为可迭代的 int 列表（或类似）
    # 为兼容性先把结果转为 list（某些 runner 可能直接返回 tuple）
    def to_list(x):
        try:
            return list(x)
        except Exception:
            # 若是单个值（不大可能），就封装为单元素列表
            return [x]

    orig_list = to_list(originalResult)
    r1 = to_list(transformResult1)
    r2 = to_list(transformResult2)
    r3_1 = to_list(transformResult3_1)
    r3_2 = to_list(transformResult3_2)
    r5 = to_list(transformResult5)
    r6 = to_list(transformResult6)
    r7_1 = to_list(transformResult7_1)
    r7_2 = to_list(transformResult7_2)
    r8 = to_list(transformResult8)
    r9 = to_list(transformResult9)
    r10 = to_list(transformResult10)
    r11 = to_list(transformResult11)
    r14 = to_list(transformResult14)
    r16 = to_list(transformResult16)
    r19 = to_list(transformResult19)
    r20 = to_list(transformResult20)
    r22 = to_list(transformResult22)


    # ---------------- Assertions ----------------
    check.equal(sum(orig_list), sum(r1), "MR1 failed (sum should be equal)")
    check.is_true(sum(orig_list) <= sum(r2), "MR2 failed (orig <= transform2)")
    check.is_true(sum(orig_list) <= sum(r3_1), "MR3_1 failed (orig <= transform3_1)")
    check.is_true(sum(orig_list) <= sum(r3_2), "MR3_2 failed (orig <= transform3_2)")
    check.is_true(sum(orig_list) <= sum(r5), "MR5 failed (orig <= transform5)")
    check.equal(sum(orig_list), sum(r6), "MR6 failed (orig == transform6)")
    check.equal(sum(orig_list), sum(r7_1), "MR7_1 failed (orig == transform7_1)")
    check.equal(sum(orig_list), sum(r7_2), "MR7_2 failed (orig == transform7_2)")
    check.is_true(sum(orig_list) <= sum(r8), "MR8 failed (orig <= transform8)")
    check.is_true(sum(orig_list) <= sum(r9), "MR9 failed (orig <= transform9)")
    check.is_true(sum(orig_list) <= sum(r10), "MR10 failed (orig <= transform10)")
    check.is_true(sum(orig_list) >= sum(r11), "MR11 failed (orig >= transform11)")
    check.is_true(sum(orig_list) >= sum(r14), "MR14 failed (orig >= transform14)")
    check.is_true(sum(orig_list) <= sum(r16), "MR16 failed (orig <= transform16)")
    check.is_true(sum(orig_list) <= sum(r19), "MR19 failed (orig <= transform19)")
    # MR20 Java 中是 assertTrue(sum(originalResult) == sum(transformResult20));
    check.equal(sum(orig_list), sum(r20), "MR20 failed (orig == transform20)")
    check.equal(sum(orig_list), sum(r22), "MR22 failed (orig == transform22)")

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
def test_clip_with_func(originalInput):
    func =clip
    assert func is not None, "mutant_func 没有被注入"
    originalResult = func(originalInput, 1, 5)
    applyMR_Assert(originalInput, originalResult)
