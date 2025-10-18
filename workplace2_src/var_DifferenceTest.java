import example.var_Difference;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class var_DifferenceTest {


    private void applyMR_Assert(final Double[] originalInput1_1, final Double[] originalInput1_2, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        final Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        final Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        double transformResult1 = var_Difference.var_Difference_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        final Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        final Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
        double transformResult2 = var_Difference.var_Difference_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        final Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        double transformResult3_1 = var_Difference.var_Difference_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        final Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        double transformResult3_2 = var_Difference.var_Difference_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        final Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        final Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        double transformResult4 = var_Difference.var_Difference_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        final Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        final Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        double transformResult5 = var_Difference.var_Difference_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        final Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        final Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        double transformResult6 = var_Difference.var_Difference_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        final Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        double transformResult7_1 = var_Difference.var_Difference_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        final Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        double transformResult7_2 = var_Difference.var_Difference_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        final Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        final Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        double transformResult8 = var_Difference.var_Difference_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        final Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        final Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        double transformResult9 = var_Difference.var_Difference_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        final Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        final Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        double transformResult10 = var_Difference.var_Difference_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        final Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        final Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        double transformResult11 = var_Difference.var_Difference_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        final Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        final Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        double transformResult12 = var_Difference.var_Difference_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        final Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        final Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        double transformResult13 = var_Difference.var_Difference_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
        final Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
        final Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
        double transformResult14 = var_Difference.var_Difference_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        final Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        final Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        double transformResult15 = var_Difference.var_Difference_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        final Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        double transformResult16 = var_Difference.var_Difference_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        final Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        double transformResult19 = var_Difference.var_Difference_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        final Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        double transformResult20 = var_Difference.var_Difference_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        final Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        final Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        double transformResult22 = var_Difference.var_Difference_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertEquals(originalResult, transformResult1, delta);
        //OR2:源输出和加3等于后续输入
        assertEquals(originalResult, transformResult2, delta);
        //OR3_1:和应该保持不变
        assertTrue(originalResult >= transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult >= transformResult3_2);
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
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult8);
//        assertTrue(originalResult == transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertTrue(originalResult <= transformResult9);
        //OR10:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult == transformResult12);
        //OR13:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult <= transformResult14);
        //OR15:源输出大于等于后续输出
        assertTrue(originalResult == transformResult15);
        //OR16:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult16);
        //OR19:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult19);
        //OR20:源输出大于等于后续输出
        assertTrue(originalResult >= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testVarDifferenceCase1() {
        final Double[] originalInput1_1 = {1.0, 2.0, 3.0, 4.0, 5.0};
        final Double[] originalInput1_2 = {5.0, 4.0, 3.0, 2.0, 1.0};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase2() {
        final Double[] originalInput1_1 = {10.0, 20.0, 30.0, 40.0, 50.0};
        final Double[] originalInput1_2 = {50.0, 40.0, 30.0, 20.0, 10.0};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase3() {
        final Double[] originalInput1_1 = {0.5, 1.5, 2.5, 3.5, 4.5};
        final Double[] originalInput1_2 = {4.5, 3.5, 2.5, 1.5, 0.5};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase4() {
        final Double[] originalInput1_1 = {2.718, 7.389, 20.085, 54.598, 148.413};
        final Double[] originalInput1_2 = {148.413, 54.598, 20.085, 7.389, 2.718};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase5() {
        final Double[] originalInput1_1 = {8.5, 0.6, 8.7, 0.8, 8.9};
        final Double[] originalInput1_2 = {-1.5, 1.4, -1.3, 1.2, -1.1};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase6() {
        final Double[] originalInput1_1 = {5.0, 10.0, 15.0, 20.0, 25.0};
        final Double[] originalInput1_2 = {25.0, 20.0, 15.0, 10.0, 5.0};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase7() {
        final Double[] originalInput1_1 = {-24.01, 25.02, -27.03, 26.04, -29.05};
        final Double[] originalInput1_2 = {16.05, -15.04, 18.03, -17.02, 28.01};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase8() {
        final Double[] originalInput1_1 = {1.1, 2.2, 3.3, 4.4, 5.5};
        final Double[] originalInput1_2 = {5.5, 4.4, 3.3, 2.2, 1.1};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase9() {
        final Double[] originalInput1_1 = {3.14, 2.71, 1.61, 0.57, 1.41};
        final Double[] originalInput1_2 = {1.41, 0.57, 1.61, 2.71, 3.14};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testVarDifferenceCase10() {
        final Double[] originalInput1_1 = {9.81, 2.45, 3.67, 4.89, 5.12};
        final Double[] originalInput1_2 = {5.12, 4.89, 3.67, 2.45, 9.81};
        double originalResult = var_Difference.var_Difference_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}
