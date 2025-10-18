import example.evalWeightedProd;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class evalWeightedProdTest {

    private void applyMR_Assert(final Double[] originalInput1_1, final Double[] originalInput1_2, final Integer begin, final Integer length, double originalResult) {
//MR1:数组元置换（打乱顺序）
        final Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        final Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        double transformResult1 = evalWeightedProd.evalWeightedProd_m(transformInput1_1, transformInput1_2, begin, length);
        //MR2:数组元素常数加法
        final Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        final Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
        double transformResult2 = evalWeightedProd.evalWeightedProd_m(transformInput2_1, transformInput2_2, begin, length);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        final Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        double transformResult3_1 = evalWeightedProd.evalWeightedProd_m(transformInput3_1, transformInput3_2, begin, length);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        final Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        double transformResult3_2 = evalWeightedProd.evalWeightedProd_m(transformInput3_3, transformInput3_4, begin, length);
        //MR4:数组元素取倒数
        final Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        final Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        double transformResult4 = evalWeightedProd.evalWeightedProd_m(transformInput4_1, transformInput4_2, begin, length);
        //MR5:数组缩放变换
        final Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        final Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        double transformResult5 = evalWeightedProd.evalWeightedProd_m(transformInput5_1, transformInput5_2, begin, length);
        //MR6:数组反转变换
        final Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        final Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        double transformResult6 = evalWeightedProd.evalWeightedProd_m(transformInput6_1, transformInput6_2, begin, length);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        final Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        double transformResult7_1 = evalWeightedProd.evalWeightedProd_m(transformInput7_1, transformInput7_2, begin, length);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        final Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        double transformResult7_2 = evalWeightedProd.evalWeightedProd_m(transformInput7_3, transformInput7_4, begin, length);
        //MR8:重复输入数组
        final Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        final Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        double transformResult8 = evalWeightedProd.evalWeightedProd_m(transformInput8_1, transformInput8_2, begin, length);
        //MR9:复合转换一致性
        final Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        final Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        double transformResult9 = evalWeightedProd.evalWeightedProd_m(transformInput9_1, transformInput9_2, begin, length);
        //MR10:单调性检验
        final Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        final Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        double transformResult10 = evalWeightedProd.evalWeightedProd_m(transformInput10_1, transformInput10_2, begin, length);
        //MR11:边界值替换(把最大值替换成0)
        final Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        final Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        double transformResult11 = evalWeightedProd.evalWeightedProd_m(transformInput11_1, transformInput11_2, begin, length);
        //MR12:数值取反变换
        final Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        final Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        double transformResult12 = evalWeightedProd.evalWeightedProd_m(transformInput12_1, transformInput12_2, begin, length);
        //MR13:微小增量调整
        final Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        final Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        double transformResult13 = evalWeightedProd.evalWeightedProd_m(transformInput13_1, transformInput13_2, begin, length);
        //MR14:移除元素的效果（移除最大值）
        final Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
        final Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
        double transformResult14 = evalWeightedProd.evalWeightedProd_m(transformInput14_1, transformInput14_2, begin, length);
        //MR15:类三角函数的周期性
        final Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        final Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        double transformResult15 = evalWeightedProd.evalWeightedProd_m(transformInput15_1, transformInput15_2, begin, length);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        final Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        double transformResult16 = evalWeightedProd.evalWeightedProd_m(transformInput16_1, transformInput16_2, begin, length);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        final Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        double transformResult19 = evalWeightedProd.evalWeightedProd_m(transformInput19_1, transformInput19_2, begin, length);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        final Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        double transformResult20 = evalWeightedProd.evalWeightedProd_m(transformInput20_1, transformInput20_2, begin, length);
        //MR22:应用恒等变换
        final Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        final Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        double transformResult22 = evalWeightedProd.evalWeightedProd_m(transformInput22_1, transformInput22_2, begin, length);
        //----------------------------------------------------------
//        //OR1:和应该保持不变
        //assertTrue(Arrays.equals(originalResult, transformResult1));
        //OR2:源输出和等于后续输入
        assertTrue(originalResult <= transformResult2);
        //OR3_1:和应该减小或保持不变
        assertTrue(originalResult <= transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult4));
        //OR5:源输出和乘以2等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
//        assertTrue(Arrays.equals(originalResult, transformResult6));
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertEquals(originalResult * 3, transformResult9, delta);
        //OR10:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出大于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult11));
        //OR12:源输出数组等于后续数组
//        assertTrue(Arrays.equals(originalResult, transformResult12));
        //OR13:源输出小于等于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult13));
        //OR14:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
        assertTrue(originalResult <= transformResult19);
        //OR20:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult7_1);
    }

    @Test
    public void testCase1() {
        final Double[] originalInput1_1 = {1.2, 3.0, 0.8, 2.2};  // 调整 -0.5 为正数 0.8
        final Double[] originalInput1_2 = {2.0, 1.0, 1.0, 0.5};  // 调整负数 -1.0 为 1.0
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase2() {
        final Double[] originalInput1_1 = {1.55, 2.55, 3.55};
        final Double[] originalInput1_2 = {4.12, 4.13, 4.14};
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase3() {
        final Double[] originalInput1_1 = {5.55, 7.55, 9.55};
        final Double[] originalInput1_2 = {10.55, 12.55, 14.55};
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase4() {
        final Double[] originalInput1_1 = {12.16, 12.17, 12.18};
        final Double[] originalInput1_2 = {12.19, 12.20, 12.21};
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase5() {
        final Double[] originalInput1_1 = {2.5, 0.7, 3.3};  // 保持不变
        final Double[] originalInput1_2 = {1.1, 2.2, 0.9};  // 调整负数 -1.1 为 1.1
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase6() {
        final Double[] originalInput1_1 = {1.6, 2.2, 3.4, 0.7};  // 调整 -2.2 为 2.2，-0.7 为 0.7
        final Double[] originalInput1_2 = {0.5, 1.5, 2.1, 1.0};  // 调整负数 -1.5 为正数
        final Integer begin = 0;
        final Integer length = 3;  // 调整 length 以避免数组越界
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase7() {
        final Double[] originalInput1_1 = {0.9, 1.8, 2.2};  // 调整负数 -0.9 为正数 0.9
        final Double[] originalInput1_2 = {0.3, 1.0, 1.2};  // 调整负数 -1.2 为 1.2
        final Integer begin = 0;
        final Integer length = 2;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase8() {
        final Double[] originalInput1_1 = {2.0, 1.5, 0.8, 3.1};  // 调整负数 -1.5 为 1.5
        final Double[] originalInput1_2 = {0.7, 1.2, 1.5, 0.3};  // 调整负数 -0.7 为 0.7，-0.3 为 0.3
        final Integer begin = 0;
        final Integer length = 2;  // 调整 length 以避免数组越界
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase9() {
        final Double[] originalInput1_1 = {1.1, 2.5, 0.4};  // 调整负数 -1.1 为正数 1.1
        final Double[] originalInput1_2 = {1.0, 0.9, 0.8};  // 调整负数 -0.9 为正数
        final Integer begin = 1;
        final Integer length = 1;  // 调整 length 以避免数组越界
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }

    @Test
    public void testCase10() {
        final Double[] originalInput1_1 = {0.3, 2.2, 1.5, 2.9, 1.1};  // 调整负数 -2.2 为 2.2，-1.1 为 1.1
        final Double[] originalInput1_2 = {1.1, 0.8, 2.0, 1.2, 0.6};  // 调整负数 -0.8 为 0.8，-0.6 为 0.6
        final Integer begin = 0;
        final Integer length = 4;
        double originalResult = evalWeightedProd.evalWeightedProd_m(originalInput1_1, originalInput1_2, begin, length);
        applyMR_Assert(originalInput1_1, originalInput1_2, begin, length, originalResult);
    }
}