import example.cal_AbsoluteDiff;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertTrue;

public class cal_AbsoluteDiffTest {
    private void applyMR_Assert(Double[] originalInput, double[] originalResult) {

        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double[] transformResult1 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput1);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double[] transformResult2 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double[] transformResult3_1 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double[] transformResult3_2 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput3_2);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double[] transformResult4 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput4);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double[] transformResult5 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput5);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double[] transformResult6 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double[] transformResult7_1 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double[] transformResult7_2 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput7_2);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double[] transformResult8 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput8);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double[] transformResult9 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput9);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double[] transformResult10 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double[] transformResult11 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput11);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double[] transformResult12 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput12);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double[] transformResult13 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput13);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double[] transformResult14 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput14);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double[] transformResult15 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double[] transformResult16 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
//        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
//        double[] transformResult19 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double[] transformResult20 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput20);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double[] transformResult22 = cal_AbsoluteDiff.cal_AbsoluteDiff_m(transformInput22);
        //----------------------------------------------------------
//        //OR1:和应该保持不变
        //assertTrue(Arrays.equals(originalResult, transformResult1));
        //OR2:源输出和加3等于后续输入
//        assertEquals(originalResult + 3, transformResult2, delta);
        //OR3_1:和应该减小或保持不变
        // assertTrue(Arrays.equals(originalResult, transformResult3_1));
        //OR3_2:和应该保持不变
//        assertTrue(originalResult  >= transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult4));
        //OR5:源输出和乘以2等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR6:源输出和等于后续输出和
//        assertTrue(Arrays.equals(originalResult, transformResult6));
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(Arrays.equals(originalResult, transformResult7_2));
        //OR8:源输出等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertEquals(originalResult * 3, transformResult9, delta);
        //OR10:源输出小于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult10));
        //OR11:源输出大于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult11));
        //OR12:源输出数组等于后续数组
        assertTrue(Arrays.equals(originalResult, transformResult12));
        //OR13:源输出小于等于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult13));
        //OR14:源输出大于等于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult14));
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(originalResult <= transformResult16);
        //OR20:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(Arrays.equals(originalResult, transformResult22));
    }


    @Test
    public void testCase1() {
        Double[] originalInput = {-1.0, 3.3, 2.0, 6.0, 9.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase2() {
        Double[] originalInput = {2.0, 1.0, 4.6, 4.0, 2.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        Double[] originalInput = {4.0, -2.0, 4.0, 6.0, 2.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        Double[] originalInput = {9.0, 2.0, 1.0, 5.8, 3.5, 2.3};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        Double[] originalInput = {-1.2, 9.4, 1.0, -3.0, -3.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        Double[] originalInput = {8.0, 3.4, 2.5, 6.9, 2.0, 3.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        Double[] originalInput = {1.0, 2.0, 3.3, 4.1, -5.0, 6.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        Double[] originalInput = {1.0, 2.0, 4.9, 2.4, 7.0, 5.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        Double[] originalInput = {1.3, 1.9, 2.0, 4.8, 1.0, 2.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        Double[] originalInput = {-2.4, 3.0, 1.0, 4.0, 7.0};
        double[] originalResult = cal_AbsoluteDiff.cal_AbsoluteDiff_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}