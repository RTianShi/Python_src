import example.winsorizedMean;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class winsorizedMeanTest {

    private void applyMR_Assert(Double[] originalInput, Integer left, Integer right, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double transformResult1 = winsorizedMean.winsorizedMean_m(transformInput1, left, right);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double transformResult2 = winsorizedMean.winsorizedMean_m(transformInput2, left, right);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double transformResult3_1 = winsorizedMean.winsorizedMean_m(transformInput3_1, left, right);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double transformResult3_2 = winsorizedMean.winsorizedMean_m(transformInput3_2, left, right);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double transformResult4 = winsorizedMean.winsorizedMean_m(transformInput4, left, right);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double transformResult5 = winsorizedMean.winsorizedMean_m(transformInput5, left, right);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double transformResult6 = winsorizedMean.winsorizedMean_m(transformInput6, left, right);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double transformResult7_1 = winsorizedMean.winsorizedMean_m(transformInput7_1, left, right);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double transformResult7_2 = winsorizedMean.winsorizedMean_m(transformInput7_2, left, right);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double transformResult8 = winsorizedMean.winsorizedMean_m(transformInput8, left, right);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double transformResult9 = winsorizedMean.winsorizedMean_m(transformInput9, left, right);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double transformResult10 = winsorizedMean.winsorizedMean_m(transformInput10, left, right);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double transformResult11 = winsorizedMean.winsorizedMean_m(transformInput11, left, right);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double transformResult12 = winsorizedMean.winsorizedMean_m(transformInput12, left, right);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double transformResult13 = winsorizedMean.winsorizedMean_m(transformInput13, left, right);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double transformResult14 = winsorizedMean.winsorizedMean_m(transformInput14, left, right);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double transformResult15 =   winsorizedMean.  winsorizedMean_m(transformInput15,left,right );
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double transformResult16 = winsorizedMean.winsorizedMean_m(transformInput16, left, right);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double transformResult19 = winsorizedMean.winsorizedMean_m(transformInput19, left, right);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double transformResult20 = winsorizedMean.winsorizedMean_m(transformInput20, left, right);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double transformResult22 = winsorizedMean.winsorizedMean_m(transformInput22, left, right);
        //----------------------------------------------------------
        double delta = 0.0001; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertEquals(originalResult, transformResult1, delta);
        //OR2:源输出和加3等于后续输入
        assertTrue(originalResult <= transformResult2);
        //OR3_1:和应该保持不变
//        assertTrue(originalResult >= transformResult3_1);
        //OR3_2:和应该保持不变
//        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该减少或保持不变
        assertTrue(originalResult >= transformResult4);
        //OR5:源输出和等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult6);
//        assertEquals(originalResult, transformResult6, delta);
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
        assertTrue(originalResult <= transformResult9);
        //OR10:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出大于等于后续输出
        assertTrue(originalResult >= transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult >= transformResult12);
        //OR13:源输出大于等于后续输出
//        assertTrue(originalResult <= transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult <= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertArrayNegation(formatArray(originalResult, 2), formatArray(transformResult15, 2));
        //OR16:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult16);
        //OR19:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult19);
        //OR20:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testWinsorizedMean1() {
        Double[] originalInput = {1.0, 2.0, 3.0, 4.0, 5.0};
        Integer left = 1;
        Integer right = 1;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean2() {
        Double[] originalInput = {8.123, 9.234, 10.345, 11.456, 12.567};
        int left = 1;
        int right = 3;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean3() {
        Double[] originalInput = {2.5, 3.5, 4.5, 5.5, 6.5};
        int left = 0;
        int right = 0;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean4() {
        Double[] originalInput = {1.234, 2.345, 3.456, 4.567, 5.678};
        int left = 1;
        int right = 1;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean5() {
        Double[] originalInput = {10.05, 11.02, 12.03, 13.04, 14.05};
        int left = 2;
        int right = 2;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean6() {
        Double[] originalInput = {10.0, 20.0, 30.0, 40.0, 50.0};
        int left = 2;
        int right = 2;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean7() {
        Double[] originalInput = {-1.11, 0.99, 3.456, 7.89};
        int left = 2;
        int right = 2;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean8() {
        Double[] originalInput = {-2.45, 5.68, 3.141, 7.888};
        int left = 1;
        int right = 2;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean9() {
        Double[] originalInput = {9.81, 9.82, 9.83, 9.84, 9.85};
        int left = 0;
        int right = 1;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }

    @Test
    public void testWinsorizedMean10() {
        Double[] originalInput = {6.72, 9.05, -5.0};
        int left = 0;
        int right = 1;
        double originalResult = winsorizedMean.winsorizedMean_m(originalInput, left, right);
        applyMR_Assert(originalInput, left, right, originalResult);
    }
}