import example.standardize;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class standardizeTest {

    private void applyMR_Assert(Double[] originalInput, Double[] originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        Double[] transformResult1 = standardize.standardize_m(transformInput1);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        Double[] transformResult2 = standardize.standardize_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        Double[] transformResult3_1 = standardize.standardize_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        Double[] transformResult3_2 = standardize.standardize_m(transformInput3_2);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        Double[] transformResult4 = standardize.standardize_m(transformInput4);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        Double[] transformResult5 = standardize.standardize_m(transformInput5);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        Double[] transformResult6 = standardize.standardize_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        Double[] transformResult7_1 = standardize.standardize_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        Double[] transformResult7_2 = standardize.standardize_m(transformInput7_2);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        Double[] transformResult8 = standardize.standardize_m(transformInput8);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        Double[] transformResult9 = standardize.standardize_m(transformInput9);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        Double[] transformResult10 = standardize.standardize_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        Double[] transformResult11 = standardize.standardize_m(transformInput11);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        Double[] transformResult12 = standardize.standardize_m(transformInput12);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        Double[] transformResult13 = standardize.standardize_m(transformInput13);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        Double[] transformResult14 = standardize.standardize_m(transformInput14);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        Double[] transformResult15 =   standardize.  standardize_m(transformInput15,k);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        Double[] transformResult16 = standardize.standardize_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        Double[] transformResult19 = standardize.standardize_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        Double[] transformResult20 = standardize.standardize_m(transformInput20);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        Double[] transformResult22 = standardize.standardize_m(transformInput22);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
        //OR1:和应该保持不变
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult1));
        assertArraySumEqual(originalResult, transformResult1);
        //OR2:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:数组应该保持不变
//        System.out.println("转换前的输出originalResult应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换前的输出transformInput3_1应该是：" + Arrays.toString(transformInput3_1));
//        System.out.println("转换后的输出transformResult3_1应该是：" + Arrays.toString(transformResult3_1));
//        assertArraySumDecreasedOrEqual(originalResult, transformResult3_1);
        //OR3_2:数组应该增加或保持不变
//        assertArraySumIncreasedOrEqual(originalResult, transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertArraySumDecreasedOrEqual(originalResult, transformResult4);
        //OR5:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult5);
        //OR6:源输出和等于后续输出和
        assertArraySumEqual(originalResult, transformResult6);
        //OR7_1:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_1);
        //OR7_2:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_2);
        //OR8:源输出*2等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult8);
        //OR9:和应该增加或保持不变
//        assertArraySumDecreasedOrEqual(originalResult, transformResult9);
        //OR10:和应该增加或保持不变
//        assertArraySumDecreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
//        assertArraySumDecreasedOrEqual(originalResult, transformResult11);
        //OR12:源输出大于后续输出
//        assertArraySumIncreasedOrEqual(originalResult, transformResult12);
        //OR13:源输出小于等于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult13);
        //OR14:源输出大于等于等于后续输出
//        assertArraySumIncreasedOrEqual(originalResult, transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult16));
//        assertArraySumIncreasedOrEqual(originalResult, transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertArraySumIncreasedOrEqual(originalResult, transformResult19);
        //OR20:源输出小于等于后续输出
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult20));
//        assertArraySumIncreasedOrEqual(originalResult, transformResult20);
        //OR22:源输出等于后续输出
        assertArraySumEqual(originalResult, transformResult22);
    }

    private void assertArraySumIncreasedOrEqual(Double[] original, Double[] transformed) {
        assertTrue(sum(transformed) >= sum(original));
    }

    private void assertArraySumDecreasedOrEqual(Double[] original, Double[] transformed) {
        assertTrue(sum(transformed) <= sum(original));
    }

    private void assertArraySumEqual(Double[] original, Double[] transformed) {
        double delta = 1e-9;
        assertEquals(sum(transformed), sum(original), delta);
    }

    private Double sum(Double[] array) {
        Double sum = 0.0;
        for (Double value : array) {
            sum += value;
        }
        return sum;
    }

    @Test
    public void testStandardizeCase1() {
        Double[] originalInput = {5.60, 6.61, 7.62, 8.64};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase2() {
        Double[] originalInput = {-1.5, -2.5, -3.5, -4.5, -5.5};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase3() {
        Double[] originalInput = {1.2, 1.3, 1.4, 1.5};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase4() {
        Double[] originalInput = {4.00, 5.00, 6.00};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase5() {
        Double[] originalInput = {-2.0, 0.0, 2.0};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase6() {
        Double[] originalInput = {5.00, -5.00, 5.00};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase7() {
        Double[] originalInput = {0.0, 1.0, 1.0, 1.0, 0.0};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase8() {
        Double[] originalInput = {2.5, 3.5, 1.5, 4.5, 0.5};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase9() {
        Double[] originalInput = {-1.0, 1.0, -1.0, 1.0};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testStandardizeCase10() {
        Double[] originalInput = {3.14159, 2.71828, 1.61803, 1.41421, 1.73205};
        Double[] originalResult = standardize.standardize_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}