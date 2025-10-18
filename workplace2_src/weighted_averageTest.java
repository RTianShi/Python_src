import example.weighted_average;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class weighted_averageTest {


    private void applyMR_Assert(Double[] originalInput1_1, Double[] originalInput1_2, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        double transformResult1 = weighted_average.weighted_average_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
        double transformResult2 = weighted_average.weighted_average_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        double transformResult3_1 = weighted_average.weighted_average_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        double transformResult3_2 = weighted_average.weighted_average_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        double transformResult4 = weighted_average.weighted_average_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        double transformResult5 = weighted_average.weighted_average_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        double transformResult6 = weighted_average.weighted_average_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        double transformResult7_1 = weighted_average.weighted_average_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        double transformResult7_2 = weighted_average.weighted_average_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        double transformResult8 = weighted_average.weighted_average_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        double transformResult9 = weighted_average.weighted_average_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        double transformResult10 = weighted_average.weighted_average_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        double transformResult11 = weighted_average.weighted_average_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        double transformResult12 = weighted_average.weighted_average_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        double transformResult13 = weighted_average.weighted_average_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
//        Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
//        Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
//        double transformResult14 = weighted_average.weighted_average_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        double transformResult15 = weighted_average.weighted_average_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        double transformResult16 = weighted_average.weighted_average_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        double transformResult19 = weighted_average.weighted_average_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        double transformResult20 = weighted_average.weighted_average_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        double transformResult22 = weighted_average.weighted_average_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertEquals(originalResult, transformResult1, delta);
        //OR2:源输出和加3等于后续输入
        assertTrue(originalResult <= transformResult2);
        //OR3_1:和应该保持不变
        assertTrue(originalResult <= transformResult3_1);
        //OR3_2:和应该保持不变
//        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该减少或保持不变
        assertTrue(originalResult >= transformResult4);
        //OR5:源输出和等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult6);
        assertEquals(originalResult, transformResult6, delta);
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出小于后续输出
//        assertTrue(originalResult >= transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertTrue(originalResult >= transformResult9);
        //OR10:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出大于等于后续输出
        assertTrue(originalResult >= transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult >= transformResult12);
        //OR13:源输出大于等于后续输出
        assertTrue(originalResult <= transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult <= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertArrayNegation(formatArray(originalResult, 2), formatArray(transformResult15, 2));
        //OR16:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult16);
        //OR19:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult19);
        //OR20:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testWeightedAverageCase1() {
        Double[] originalInput1_1 = {1.0, 2.0, 3.0, 4.0};
        Double[] originalInput1_2 = {0.5, 0.5, 0.5, 0.5};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase2() {
        Double[] originalInput1_1 = {15.55, 24.57, 31.58};
        Double[] originalInput1_2 = {-12.05, -24.07, -30.08};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase3() {
        Double[] originalInput1_1 = {0.1, 0.2, 0.3};
        Double[] originalInput1_2 = {10.0, 20.0, 30.0};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);

    }

    @Test
    public void testWeightedAverageCase4() {
        Double[] originalInput1_1 = {2.718, 3.141, 1.618};
        Double[] originalInput1_2 = {1.0, 2.0, 3.0};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase5() {
        Double[] originalInput1_1 = {5.01, 6.02, 7.03, 8.04};
        Double[] originalInput1_2 = {1.05, 1.06, 1.07, 1.08};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase6() {
        Double[] originalInput1_1 = {5.12, 10.89, 15.16};
        Double[] originalInput1_2 = {5.1, 5.2, 5.3};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase7() {
        Double[] originalInput1_1 = {7.123456, 8.654321};
        Double[] originalInput1_2 = {1.5, 2.5};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase8() {
        Double[] originalInput1_1 = {3.14, 1.59, 2.65};
        Double[] originalInput1_2 = {1.0, 1.0, 1.0};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
    }

    @Test
    public void testWeightedAverageCase9() {
        Double[] originalInput1_1 = {1.0001, 1.0002, 1.0003};
        Double[] originalInput1_2 = {0.5, 0.5, 0.5};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testWeightedAverageCase10() {
        Double[] originalInput1_1 = {9.81, 9.82, 9.83, 9.84};
        Double[] originalInput1_2 = {2.0, 2.0, 2.0, 2.0};
        double originalResult = weighted_average.weighted_average_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}