import example.shell_sort;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class shell_sortTest {

    private void applyMR_Assert(Integer[] originalInput, Integer[] originalResult) {
        //MR1:数组元置换（打乱顺序）
        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
        Integer[] transformResult1 = shell_sort.shell_sort_m(transformInput1);
        //MR2:数组元素常数加法
        Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
        Integer[] transformResult2 = shell_sort.shell_sort_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput);
        Integer[] transformResult3_1 = shell_sort.shell_sort_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput);
        Integer[] transformResult3_2 = shell_sort.shell_sort_m(transformInput3_2);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput);
        Integer[] transformInput4_1 = new Integer[transformInput4.length];
        for (int i = 0; i < transformInput4.length; i++) {
            transformInput4_1[i] = transformInput4[i].intValue();
        }
        Integer[] transformResult4 = shell_sort.shell_sort_m(transformInput4_1);
        //MR5:数组缩放变换
        Integer[] transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2);
        Integer[] transformResult5 = shell_sort.shell_sort_m(transformInput5);
        //MR6:数组反转变换
        Integer[] transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput);
        Integer[] transformResult6 = shell_sort.shell_sort_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput);
        Integer[] transformResult7_1 = shell_sort.shell_sort_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput);
        Integer[] transformResult7_2 = shell_sort.shell_sort_m(transformInput7_2);
        //MR8:重复输入数组
        Integer[] transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput);
        Integer[] transformResult8 = shell_sort.shell_sort_m(transformInput8);
        //MR9:复合转换一致性
        Integer[] transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3);
        Integer[] transformResult9 = shell_sort.shell_sort_m(transformInput9);
        //MR10:单调性检验
        Integer[] transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput);
        Integer[] transformResult10 = shell_sort.shell_sort_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput);
        Integer[] transformResult11 = shell_sort.shell_sort_m(transformInput11);
        //MR12:数值取反变换
        Integer[] transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput);
        Integer[] transformResult12 = shell_sort.shell_sort_m(transformInput12);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput);
        Integer[] transformInput13_1 = new Integer[transformInput13.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_1[i] = transformInput13[i].intValue();
        }
        Integer[] transformResult13 = shell_sort.shell_sort_m(transformInput13_1);
        //MR14:移除元素的效果（移除最大值）
        Integer[] transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput);
        Integer[] transformResult14 = shell_sort.shell_sort_m(transformInput14);
        //MR15:类三角函数的周期性
//        Integer[] transformInput15 = MetamorphicTestGenerator1.applyMR15(originalInput);
//        Integer[] transformResult15 = shell_sort.shell_sort_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput);
        Integer[] transformResult16 = shell_sort.shell_sort_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Integer[] transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2);
        Integer[] transformResult19 = shell_sort.shell_sort_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput);
        Integer[] transformInput20_1 = new Integer[transformInput20.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_1[i] = transformInput20[i].intValue();
        }
        Integer[] transformResult20 = shell_sort.shell_sort_m(transformInput20_1);
        //MR22:应用恒等变换
        Integer[] transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput);
        Integer[] transformResult22 = shell_sort.shell_sort_m(transformInput22);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison

//        //OR1:和应该保持不变
        assertTrue(Arrays.equals(originalResult, transformResult1));
        //OR2:源输出和加3等于后续输入
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:和应该减小或保持不变
        assertArraySumEqual(originalResult, transformResult3_1);
        //OR3_2:和应该保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult3_2);
        //OR4:和应该减少或保持不变
        assertArraySumDecreasedOrEqual(originalResult, transformResult4);
        //OR5:源输出和乘以2等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult5);
        //OR6:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult6));
        //OR7_1:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR7_2:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult7_2));
        //OR8:源输出等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult7_1);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
        assertArraySumIncreasedOrEqual(originalResult, transformResult9);
        //OR10:源输出小于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult11);
        //OR12:源输出负数等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult12);
        //OR13:源输出小于等于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult13);
        //OR14:源输出大于等于等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertArraySumIncreasedOrEqual(originalResult, transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertArraySumIncreasedOrEqual(originalResult, transformResult19);
        //OR20:源输出小于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(Arrays.equals(originalResult, transformResult22));
    }

    private void assertArraySumIncreasedOrEqual(Integer[] original, Integer[] transformed) {
        assertTrue(sum(transformed) >= sum(original));
    }

    private void assertArraySumDecreasedOrEqual(Integer[] original, Integer[] transformed) {
        assertTrue(sum(transformed) <= sum(original));
    }

    private void assertArraySumEqual(Integer[] original, Integer[] transformed) {
        double delta = 1e-9;
        assertEquals(sum(transformed), sum(original), delta);
    }

    private Integer sum(Integer[] array) {
        Integer sum = 0;
        for (Integer value : array) {
            sum += value;
        }
        return sum;
    }


    @Test
    public void testShellSortCase1() {
        Integer[] originalInput = {5, 2, 9, 1, 5, 6};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase2() {
        Integer[] originalInput = {3, 1, 4, 1, 5, 9, 2, 6};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase3() {
        Integer[] originalInput = {12, 11, 13, 5, 6};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase4() {
        Integer[] originalInput = {8, 4, 7, 1, 3};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase5() {
        Integer[] originalInput = {0, 0, 0, 0};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase6() {
        Integer[] originalInput = {5, 8, 7,
                9, 4};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase7() {
        Integer[] originalInput = {34, 7, 23, 32, 5};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase8() {
        Integer[] originalInput = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase9() {
        Integer[] originalInput = {99, 45, 67, 23, 89, 12};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testShellSortCase10() {
        Integer[] originalInput = {15, 22, 7, 18, 3};
        Integer[] originalResult = shell_sort.shell_sort_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}