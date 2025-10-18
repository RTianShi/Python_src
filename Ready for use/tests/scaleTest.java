import example.scale;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class scaleTest {

    private void applyMR_Assert(Double val, final Double[] originalInput, double[] originalResult) {
//MR1:数组元置换（打乱顺序）
        final Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double[] transformResult1 = scale.scale_m(val, transformInput1);
        //MR2:数组元素常数加法
        final Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double[] transformResult2 = scale.scale_m(val, transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double[] transformResult3_1 = scale.scale_m(val, transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double[] transformResult3_2 = scale.scale_m(val, transformInput3_2);
        //MR4:数组元素取倒数
        final Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double[] transformResult4 = scale.scale_m(val, transformInput4);
        //MR5:数组缩放变换
        final Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double[] transformResult5 = scale.scale_m(val, transformInput5);
        //MR6:数组反转变换
        final Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double[] transformResult6 = scale.scale_m(val, transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double[] transformResult7_1 = scale.scale_m(val, transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double[] transformResult7_2 = scale.scale_m(val, transformInput7_2);
        //MR8:重复输入数组
        final Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double[] transformResult8 = scale.scale_m(val, transformInput8);
        //MR9:复合转换一致性
        final Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double[] transformResult9 = scale.scale_m(val, transformInput9);
        //MR10:单调性检验
        final Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double[] transformResult10 = scale.scale_m(val, transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        final Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double[] transformResult11 = scale.scale_m(val, transformInput11);
        //MR12:数值取反变换
        final Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double[] transformResult12 = scale.scale_m(val, transformInput12);
        //MR13:微小增量调整
        final Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double[] transformResult13 = scale.scale_m(val, transformInput13);
        //MR14:移除元素的效果（移除最大值）
        final Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double[] transformResult14 = scale.scale_m(val, transformInput14);
        //MR15:类三角函数的周期性
//       final Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double[] transformResult15 = scale.scale_m(val,transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double[] transformResult16 = scale.scale_m(val, transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double[] transformResult19 = scale.scale_m(val, transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double[] transformResult20 = scale.scale_m(val, transformInput20);
        //MR22:应用恒等变换
        final Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double[] transformResult22 = scale.scale_m(val, transformInput22);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
        //OR1:和应该保持不变
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult1));
        assertArraySumEqual(originalResult, transformResult1);
        //OR2:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:数组应该保持不变
        assertArraySumEqual(originalResult, transformResult3_1);
        //OR3_2:数组应该保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult3_2);
        //OR4:和应该减少或保持不变
        assertArraySumDecreasedOrEqual(originalResult, transformResult4);
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
        assertArraySumIncreasedOrEqual(originalResult, transformResult9);
        //OR10:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult11);
        //OR12:源输出大于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult12);
        //OR13:源输出小于等于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult13);
        //OR14:源输出大于等于等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult16));
        assertArraySumIncreasedOrEqual(originalResult, transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
        assertArraySumIncreasedOrEqual(originalResult, transformResult19);
        //OR20:源输出小于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult20);
        //OR22:源输出等于后续输出
        assertArraySumEqual(originalResult, transformResult22);
    }

    private void assertArraySumIncreasedOrEqual(double[] original, double[] transformed) {
        assertTrue(sum(transformed) >= sum(original));
    }

    private void assertArraySumDecreasedOrEqual(double[] original, double[] transformed) {
        assertTrue(sum(transformed) <= sum(original));
    }

    private void assertArraySumEqual(double[] original, double[] transformed) {
        double delta = 1e-9;
        assertEquals(sum(transformed), sum(original), delta);
    }

    private double sum(double[] array) {
        double sum = 0.0;
        for (double value : array) {
            sum += value;
        }
        return sum;
    }


    @Test
    public void testScaleCase1() {
        Double val = 2.0;
        final Double[] originalInput = {1.0, 2.0, 3.0, 4.0};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase2() {
        Double val = 0.5;
        Double[] originalInput = {10.0, 20.0, 30.0};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase3() {
        Double val = 1.5;
        Double[] originalInput = {1.60, 2.55, 3.57};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase4() {
        Double val = 3.14;
        Double[] originalInput = {1.0, 2.0, 3.0};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase5() {
        Double val = 0.0001;
        Double[] originalInput = {100.0, 200.0, 300.0};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase6() {
        Double val = 7.5;
        Double[] originalInput = {0.5, 1.5, 2.5};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase7() {
        Double val = 0.6;
        Double[] originalInput = {10.58, 20.70, 30.55};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase8() {
        Double val = 1.234;
        Double[] originalInput = {4.567, 8.910, 12.345};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase9() {
        Double val = 0.01;
        Double[] originalInput = {1000.0, 2000.0, 3000.0};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }

    @Test
    public void testScaleCase10() {
        Double val = 2.718;
        Double[] originalInput = {3.14, 2.71, 1.61};
        double[] originalResult = scale.scale_m(val, originalInput);
        applyMR_Assert(val, originalInput, originalResult);
    }
}