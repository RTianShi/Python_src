import example.cal_Diff;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertTrue;

public class cal_DiffTest {
    private void applyMR_Assert(final double[] originalInput1_1, final double[] originalInput1_2, double[] originalResult) {

        //MR1:数组元置换（打乱顺序）
        final double[] transformInput1_1 = MetamorphicTestGenerator5.applyMR1(originalInput1_1);
        final double[] transformInput1_2 = MetamorphicTestGenerator5.applyMR1(originalInput1_2);
        double[] transformResult1 = cal_Diff.cal_Diff_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        final double[] transformInput2_1 = MetamorphicTestGenerator5.applyMR2(originalInput1_1);
        final double[] transformInput2_2 = MetamorphicTestGenerator5.applyMR2(originalInput1_2);
        double[] transformResult2 = cal_Diff.cal_Diff_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final double[] transformInput3_1 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_1);
        final double[] transformInput3_2 = MetamorphicTestGenerator5.applyMR3_1(originalInput1_2);
        double[] transformResult3_1 = cal_Diff.cal_Diff_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final double[] transformInput3_3 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_1);
        final double[] transformInput3_4 = MetamorphicTestGenerator5.applyMR3_2(originalInput1_2);
        double[] transformResult3_2 = cal_Diff.cal_Diff_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        final double[] transformInput4_1 = MetamorphicTestGenerator5.applyMR4(originalInput1_1);
        final double[] transformInput4_2 = MetamorphicTestGenerator5.applyMR4(originalInput1_2);
        double[] transformResult4 = cal_Diff.cal_Diff_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        final double[] transformInput5_1 = MetamorphicTestGenerator5.applyMR5(originalInput1_1, 2);
        final double[] transformInput5_2 = MetamorphicTestGenerator5.applyMR5(originalInput1_2, 2);
        double[] transformResult5 = cal_Diff.cal_Diff_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        final double[] transformInput6_1 = MetamorphicTestGenerator5.applyMR6(originalInput1_1);
        final double[] transformInput6_2 = MetamorphicTestGenerator5.applyMR6(originalInput1_2);
        double[] transformResult6 = cal_Diff.cal_Diff_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final double[] transformInput7_1 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_1);
        final double[] transformInput7_2 = MetamorphicTestGenerator5.applyMR7_1(originalInput1_2);
        double[] transformResult7_1 = cal_Diff.cal_Diff_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final double[] transformInput7_3 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_1);
        final double[] transformInput7_4 = MetamorphicTestGenerator5.applyMR7_2(originalInput1_2);
        double[] transformResult7_2 = cal_Diff.cal_Diff_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        final double[] transformInput8_1 = MetamorphicTestGenerator5.applyMR8(originalInput1_1);
        final double[] transformInput8_2 = MetamorphicTestGenerator5.applyMR8(originalInput1_2);
        double[] transformResult8 = cal_Diff.cal_Diff_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        final double[] transformInput9_1 = MetamorphicTestGenerator5.applyMR9(originalInput1_1, 1);
        final double[] transformInput9_2 = MetamorphicTestGenerator5.applyMR9(originalInput1_2, 1);
        double[] transformResult9 = cal_Diff.cal_Diff_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        final double[] transformInput10_1 = MetamorphicTestGenerator5.applyMR10(originalInput1_1);
        final double[] transformInput10_2 = MetamorphicTestGenerator5.applyMR10(originalInput1_2);
        double[] transformResult10 = cal_Diff.cal_Diff_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        final double[] transformInput11_1 = MetamorphicTestGenerator5.applyMR11(originalInput1_1);
        final double[] transformInput11_2 = MetamorphicTestGenerator5.applyMR11(originalInput1_2);
        double[] transformResult11 = cal_Diff.cal_Diff_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        final double[] transformInput12_1 = MetamorphicTestGenerator5.applyMR12(originalInput1_1);
        final double[] transformInput12_2 = MetamorphicTestGenerator5.applyMR12(originalInput1_2);
        double[] transformResult12 = cal_Diff.cal_Diff_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        final double[] transformInput13_1 = MetamorphicTestGenerator5.applyMR13(originalInput1_1);
        final double[] transformInput13_2 = MetamorphicTestGenerator5.applyMR13(originalInput1_2);
        double[] transformResult13 = cal_Diff.cal_Diff_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
        final double[] transformInput14_1 = MetamorphicTestGenerator5.applyMR14(originalInput1_1);
        final double[] transformInput14_2 = MetamorphicTestGenerator5.applyMR14(originalInput1_2);
        double[] transformResult14 = cal_Diff.cal_Diff_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        final double[] transformInput15_1 = MetamorphicTestGenerator5.applyMR15(originalInput1_1);
        final double[] transformInput15_2 = MetamorphicTestGenerator5.applyMR15(originalInput1_2);
        double[] transformResult15 = cal_Diff.cal_Diff_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final double[] transformInput16_1 = MetamorphicTestGenerator5.applyMR16(originalInput1_1);
        final double[] transformInput16_2 = MetamorphicTestGenerator5.applyMR16(originalInput1_2);
        double[] transformResult16 = cal_Diff.cal_Diff_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final double[] transformInput19_1 = MetamorphicTestGenerator5.applyMR19(originalInput1_1, 2);
        final double[] transformInput19_2 = MetamorphicTestGenerator5.applyMR19(originalInput1_2, 2);
        double[] transformResult19 = cal_Diff.cal_Diff_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final double[] transformInput20_1 = MetamorphicTestGenerator5.applyMR20(originalInput1_1);
        final double[] transformInput20_2 = MetamorphicTestGenerator5.applyMR20(originalInput1_2);
        double[] transformResult20 = cal_Diff.cal_Diff_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        final double[] transformInput22_1 = MetamorphicTestGenerator5.applyMR22(originalInput1_1);
        final double[] transformInput22_2 = MetamorphicTestGenerator5.applyMR22(originalInput1_2);
        double[] transformResult22 = cal_Diff.cal_Diff_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
//        //OR1:和应该保持不变
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult1, 2)));
        //OR2:源输出和加3等于后续输入
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult2, 2)));
        //OR3_1:和应该减小或保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult3_1));
        //OR3_2:和应该保持不变
//        assertTrue(formatArray(originalResult, 2)  >= transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult4));
        //OR5:源输出和乘以2等于后续输出
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult5, 2)));
        //OR6:源输出和等于后续输出和
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult6));
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult7_1, 2)));
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult7_2, 2)));
        //OR8:源输出等于后续输出
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult7_1, 2)));
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertEquals(formatArray(originalResult, 2) * 3, transformResult9, delta);
        //OR10:源输出小于等于后续输出
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult10, 2)));
        //OR11:源输出大于等于后续输出
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult11));
        //OR12:源输出数组等于后续数组
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult12));
        //OR13:源输出小于等于等于后续输出
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult13));
        //OR14:源输出大于等于等于后续输出
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult14));
        //OR15:源输出大于等于等于后续输出
        assertArrayNegation(formatArray(originalResult, 2), formatArray(transformResult15, 2));
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(formatArray(originalResult, 2) <= transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(formatArray(originalResult, 2) <= transformResult16);
        //OR20:源输出小于等于后续输出
//        assertTrue(formatArray(originalResult, 2) <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult22, 2)));
    }

    public static boolean assertArrayNegation(double[] arr1, double[] arr2) {
        if (arr1.length == 0 || arr2.length == 0 || arr1.length != arr2.length) {
            return false;
        }
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] == -arr2[i])
                return true;
        }
        return false;
    }

    public static double[] formatArray(double[] arr, int places) {
        double[] formatted = new double[arr.length];
        for (int i = 0; i < arr.length; i++) {
            formatted[i] = round(arr[i], places);
        }
        return formatted;
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();
        long factor = (long) Math.pow(10, places);
        value *= factor;
        long tmp = Math.round(value);
        return (double) tmp / factor;
    }

    @Test
    public void testCase1() {
        double[] originalInput1_1 = {1.5, 2.5, 3.5, 4.5, 5.5};
        double[] originalInput1_2 = {3.8, 4.8, 5.8, 6.8, 7.8};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase2() {
        double[] originalInput1_1 = {10.2, 20.2, 30.2, 40.2};
        double[] originalInput1_2 = {5.6, 6.6, 7.6, 8.6};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        final double[] originalInput1_1 = {5.56, 10.83, 15.21, 20.55};
        final double[] originalInput1_2 = {2.61, 7.25, 8.36, 4.55};
        final double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        double[] originalInput1_1 = {1.62, 3.56, 5.74, 7.89, 9.96};
        double[] originalInput1_2 = {6.55, 6.33, 7.53, 8.12, 9.13};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        double[] originalInput1_1 = {1.62, 3.56, 5.74, 7.89};
        double[] originalInput1_2 = {2.61, 7.25, 8.36, 4.55};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        double[] originalInput1_1 = {10.2, 20.2, 30.2, 40.2};
        double[] originalInput1_2 = {2.61, 7.25, 8.36, 4.55};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        double[] originalInput1_1 = {3.8, 4.8, 5.8, 6.8, 7.8};
        double[] originalInput1_2 = {1.62, 3.56, 5.74, 7.89, 9.96};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        double[] originalInput1_1 = {5.56, 2.56, 7.56};
        double[] originalInput1_2 = {3.8, 4.8, 5.8};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        double[] originalInput1_1 = {99.86, 100.23, 101.43, 102.55};
        double[] originalInput1_2 = {2.61, 7.25, 8.36, 4.55};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        double[] originalInput1_1 = {3.8, 4.8, 5.8};
        double[] originalInput1_2 = {5.56, 2.56, 7.56};
        double[] originalResult = cal_Diff.cal_Diff_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}