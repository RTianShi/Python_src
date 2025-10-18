import example.ebeSubtract;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class ebeSubtractTest {

    private void applyMR_Assert(Double[] originalInput1_1, Double[] originalInput1_2, Double[] originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        Double[] transformResult1 = ebeSubtract.ebeSubtract_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_1));
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_2));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_1));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_2));
        Double[] transformResult2 = ebeSubtract.ebeSubtract_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        Double[] transformResult3_1 = ebeSubtract.ebeSubtract_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        Double[] transformResult3_2 = ebeSubtract.ebeSubtract_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        Double[] transformResult4 = ebeSubtract.ebeSubtract_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        Double[] transformResult5 = ebeSubtract.ebeSubtract_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        Double[] transformResult6 = ebeSubtract.ebeSubtract_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        Double[] transformResult7_1 = ebeSubtract.ebeSubtract_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        Double[] transformResult7_2 = ebeSubtract.ebeSubtract_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        Double[] transformResult8 = ebeSubtract.ebeSubtract_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        Double[] transformResult9 = ebeSubtract.ebeSubtract_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        Double[] transformResult10 = ebeSubtract.ebeSubtract_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        Double[] transformResult11 = ebeSubtract.ebeSubtract_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        Double[] transformResult12 = ebeSubtract.ebeSubtract_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        Double[] transformResult13 = ebeSubtract.ebeSubtract_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
        Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
        Double[] transformResult14 = ebeSubtract.ebeSubtract_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        Double[] transformResult15 = ebeSubtract.ebeSubtract_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        Double[] transformResult16 = ebeSubtract.ebeSubtract_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        Double[] transformResult19 = ebeSubtract.ebeSubtract_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        Double[] transformResult20 = ebeSubtract.ebeSubtract_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        Double[] transformResult22 = ebeSubtract.ebeSubtract_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
        //OR1:和应该保持不变
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult1));
//        assertArraySumEqual(originalResult, transformResult1);
        //OR2:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:数组应该保持不变
        assertArraySumEqual(originalResult, transformResult3_1);
        //OR3_2:数组应该保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertArraySumDecreasedOrEqual(originalResult, transformResult4);
        //OR5:和应该增加或保持不变
//        assertArraySumDecreasedOrEqual(originalResult, transformResult5);
        //OR6:源输出和等于后续输出和
//        assertArraySumEqual(originalResult, transformResult6);
        //OR7_1:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_1);
        //OR7_2:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_2);
        //OR8:源输出*2等于后续输出
//        assertArraySumIncreasedOrEqual(originalResult, transformResult8);
        //OR9:和应该增加或保持不变
//        assertArraySumIncreasedOrEqual(originalResult, transformResult9);
        //OR10:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
//        assertArraySumDecreasedOrEqual(originalResult, transformResult11);
        //OR12:源输出大于后续输出
//        assertArraySumDecreasedOrEqual(originalResult, transformResult12);
        //OR13:源输出小于等于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult13);
        //OR14:源输出大于等于等于后续输出
//        assertArraySumDecreasedOrEqual(originalResult, transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult16));
//        assertArraySumIncreasedOrEqual(originalResult, transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertArraySumIncreasedOrEqual(originalResult, transformResult19);
        //OR20:源输出小于等于后续输出
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
        assertTrue(sum(transformed) == sum(original));
    }

    private double sum(Double[] array) {
        double sum = 0.0;
        for (double value : array) {
            sum += value;
        }
        return sum;
    }

    @Test
    public void testCase1() {
        Double[] originalInput1_1 = {1.5, -2.3, 3.7};
        Double[] originalInput1_2 = {2.0, 1.1, -0.5};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase2() {
        Double[] originalInput1_1 = {-6.5, 7.5, -8.5, 9.5};
        Double[] originalInput1_2 = {2.4, 2.6, 2.7, 2.9};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        Double[] originalInput1_1 = {3.14, -2.71, 1.61};
        Double[] originalInput1_2 = {-1.23, 2.34, -0.45};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        Double[] originalInput1_1 = {-2.5, 2.5, -3.5, 4.5};
        Double[] originalInput1_2 = {1.5, -1.0, 1.0, -0.5};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        Double[] originalInput1_1 = {0.0, 0.0, 0.0, 0.0};
        Double[] originalInput1_2 = {1.1, 2.2, 3.3, 4.4};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        Double[] originalInput1_1 = {5.55, -1.55, 2.25};
        Double[] originalInput1_2 = {-0.55, 1.55, -2.25};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        Double[] originalInput1_1 = {4.4, 3.3};
        Double[] originalInput1_2 = {1.1, 2.2};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        Double[] originalInput1_1 = {3.25, -7.69, 5.48, -1.32, 6.55};
        Double[] originalInput1_2 = {-7.29, 8.12, -9.13, 4.68, 7.23};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        Double[] originalInput1_1 = {6.57, 4.32, 4.98};
        Double[] originalInput1_2 = {6.70, 8.25, 9.47};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        Double[] originalInput1_1 = {5.13, -1.25, 0.0, 4.36};
        Double[] originalInput1_2 = {-6.21, 7.31, 4.55, 2.12};
        Double[] originalResult = ebeSubtract.ebeSubtract_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}