import example.dist;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class distTest {

    private void applyMR_Assert(Double[] originalInput1_1, Double[] originalInput1_2, double originalResult) {
//MR1:数组元置换（打乱顺序）
        Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        double transformResult1 = dist.dist_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_1));
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_2));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_1));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_2));
        double transformResult2 = dist.dist_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        double transformResult3_1 = dist.dist_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        double transformResult3_2 = dist.dist_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        double transformResult4 = dist.dist_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        double transformResult5 = dist.dist_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        double transformResult6 = dist.dist_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        double transformResult7_1 = dist.dist_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        double transformResult7_2 = dist.dist_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        double transformResult8 = dist.dist_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        double transformResult9 = dist.dist_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        double transformResult10 = dist.dist_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        double transformResult11 = dist.dist_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        double transformResult12 = dist.dist_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        double transformResult13 = dist.dist_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
        Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
        double transformResult14 = dist.dist_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        double transformResult15 = dist.dist_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        double transformResult16 = dist.dist_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        double transformResult19 = dist.dist_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        double transformResult20 = dist.dist_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        double transformResult22 = dist.dist_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult1, 2)));
        //OR2:源输出等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult2);
        assertEquals(originalResult, transformResult2, delta);
        //OR3_1:和应该保持不变
        assertTrue(originalResult == transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult == transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), transformResult4));
        //OR5:源输出和小于等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult6);
        assertEquals(originalResult, transformResult6, delta);
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertEquals(formatArray(originalResult, 2) * 3, transformResult9, delta);
        //OR10:源输出等于后续输出
        assertEquals(originalResult, transformResult10, delta);
        //OR11:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult == transformResult12);
        //OR13:源输出大于等于后续输出
        assertEquals(originalResult, transformResult13, delta);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertArrayNegation(formatArray(originalResult, 2), formatArray(transformResult15, 2));
        //OR16:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult19);
        //OR20:源输出等于后续输出
        assertEquals(originalResult, transformResult20, delta);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testCase1() {
        Double[] originalInput1_1 = {15.2, 15.6, 13.4};
        Double[] originalInput1_2 = {10.1, 15.6, 13.4};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);

    }

    @Test
    public void testCase2() {
        Double[] originalInput1_1 = {5.99, 4.83, 7.26, 9.45};
        Double[] originalInput1_2 = {6.72, 4.61, 7.23, 8.12};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        Double[] originalInput1_1 = {3.14, -2.718};
        Double[] originalInput1_2 = {3.00, -2.70};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        Double[] originalInput1_1 = {-7.89, 1.234, 0.567};
        Double[] originalInput1_2 = {-7.90, 1.230, 0.570};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        Double[] originalInput1_1 = {4.56, 6.13, 7.88};
        Double[] originalInput1_2 = {8.96, 9.50, 4.60};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        Double[] originalInput1_1 = {4.5678, -3.4567, 2.3456};
        Double[] originalInput1_2 = {4.567, -3.456, 2.345};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        Double[] originalInput1_1 = {-1.234, 2.345, -3.456, 4.567};
        Double[] originalInput1_2 = {-1.23, 2.35, -3.46, 4.56};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        Double[] originalInput1_1 = {5.12, 7.56, 8.19};
        Double[] originalInput1_2 = {5.12, 6.79, 0.46};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        Double[] originalInput1_1 = {-3.14159, 2.71828};
        Double[] originalInput1_2 = {-3.14, 2.72};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        Double[] originalInput1_1 = {1.23, 2.24, 3.25, 4.26};
        Double[] originalInput1_2 = {5.27, 6.28, 9.29, 10.30};
        double originalResult = dist.dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}