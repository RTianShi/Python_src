import example.checkNonNegative;
import example.checkPositive;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class checkPositiveTest {

    // Apply metamorphic test and assert results
    private void applyMR_Assert(final double[] originalInput, boolean originalResult) {
        //MR1:数组元置换（打乱顺序）
        final double[] transformInput1 = MetamorphicTestGenerator3.applyMR1(originalInput);
        boolean transformResult1 = checkNonNegative.checkNonNegative_m(transformInput1);
        //MR2:数组元素常数加法
        final double[] transformInput2 = MetamorphicTestGenerator3.applyMR2(originalInput);
        boolean transformResult2 = checkNonNegative.checkNonNegative_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final double[] transformInput3_1 = MetamorphicTestGenerator3.applyMR3_1(originalInput);
        boolean transformResult3_1 = checkNonNegative.checkNonNegative_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final double[] transformInput3_2 = MetamorphicTestGenerator3.applyMR3_2(originalInput);
        boolean transformResult3_2 = checkNonNegative.checkNonNegative_m(transformInput3_2);
        //MR4:数组元素取倒数
        final double[] transformInput4 = MetamorphicTestGenerator3.applyMR4(originalInput);
        boolean transformResult4 = checkNonNegative.checkNonNegative_m(transformInput4);
        //MR5:数组缩放变换
        final double[] transformInput5 = MetamorphicTestGenerator3.applyMR5(originalInput, 2);
        boolean transformResult5 = checkNonNegative.checkNonNegative_m(transformInput5);
        //MR6:数组反转变换
        final double[] transformInput6 = MetamorphicTestGenerator3.applyMR6(originalInput);
        boolean transformResult6 = checkNonNegative.checkNonNegative_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final double[] transformInput7_1 = MetamorphicTestGenerator3.applyMR7_1(originalInput);
        boolean transformResult7_1 = checkNonNegative.checkNonNegative_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final double[] transformInput7_2 = MetamorphicTestGenerator3.applyMR7_2(originalInput);
        boolean transformResult7_2 = checkNonNegative.checkNonNegative_m(transformInput7_2);
        //MR8:重复输入数组
        final double[] transformInput8 = MetamorphicTestGenerator3.applyMR8(originalInput);
        boolean transformResult8 = checkNonNegative.checkNonNegative_m(transformInput8);
        //MR9:复合转换一致性
        final double[] transformInput9 = MetamorphicTestGenerator3.applyMR9(originalInput, 3);
        boolean transformResult9 = checkNonNegative.checkNonNegative_m(transformInput9);
        //MR10:单调性检验
        final double[] transformInput10 = MetamorphicTestGenerator3.applyMR10(originalInput);
        boolean transformResult10 = checkNonNegative.checkNonNegative_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        final double[] transformInput11 = MetamorphicTestGenerator3.applyMR11(originalInput);
        boolean transformResult11 = checkNonNegative.checkNonNegative_m(transformInput11);
        //MR12:数值取反变换
        final double[] transformInput12 = MetamorphicTestGenerator3.applyMR12(originalInput);
        boolean transformResult12 = checkNonNegative.checkNonNegative_m(transformInput12);
        //MR13:微小增量调整
        final double[] transformInput13 = MetamorphicTestGenerator3.applyMR13(originalInput);
        boolean transformResult13 = checkNonNegative.checkNonNegative_m(transformInput13);
        //MR14:移除元素的效果（移除最大值）
        final double[] transformInput14 = MetamorphicTestGenerator3.applyMR14(originalInput);
        boolean transformResult14 = checkNonNegative.checkNonNegative_m(transformInput14);
        //MR15:类三角函数的周期性
//        final double[] transformInput15 = MetamorphicTestGenerator3.applyMR15(originalInput);
//        boolean transformResult15 = checkNonNegative.checkNonNegative_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final double[] transformInput16 = MetamorphicTestGenerator3.applyMR16(originalInput);
        boolean transformResult16 = checkNonNegative.checkNonNegative_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final double[] transformInput19 = MetamorphicTestGenerator3.applyMR19(originalInput, 2);
        boolean transformResult19 = checkNonNegative.checkNonNegative_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final double[] transformInput20 = MetamorphicTestGenerator3.applyMR20(originalInput);
        boolean transformResult20 = checkNonNegative.checkNonNegative_m(transformInput20);
        //MR22:应用恒等变换
        final double[] transformInput22 = MetamorphicTestGenerator3.applyMR22(originalInput);
        boolean transformResult22 = checkNonNegative.checkNonNegative_m(transformInput22);
//        //----------------------------------------------------------
//        //OR1:和应该保持不变
        assertTrue(originalResult == transformResult1);
        //OR2:源输出和加3等于后续输入
//        assertEquals(originalResult + 3, transformResult2, delta);
        //OR3_1:和应该减小或保持不变
        assertTrue(originalResult == transformResult3_1);
        //OR3_2:应该保持不变
        assertTrue(originalResult == transformResult3_2);
        //OR4:和应该减少或保持不变
        assertTrue(originalResult == transformResult4);
        //OR5:源输出和乘以2等于后续输出
        assertTrue(originalResult == transformResult5);
        //OR6:源输出和等于后续输出和
//        assertTrue(Arrays.equals(originalResult, transformResult6));
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出等于后续输出
        assertTrue(originalResult == transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
        assertTrue(originalResult == transformResult9);
        //OR10:源输出小于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult10));
        //OR11:源输出等于后续输出
        assertTrue(originalResult == transformResult11);
        //OR12:源输出数组等于后续数组
//        assertTrue(Arrays.equals(originalResult, transformResult12));
        //OR13:源输出等于等于后续输出
        assertTrue(originalResult == transformResult13);
        //OR14:源输出等于等于后续输出
        assertTrue(originalResult == transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出等于等于后续输出
        assertTrue(originalResult == transformResult16);
        //OR19:源输出等于等于后续输出
        assertTrue(originalResult == transformResult19);
        //OR20:源输出等于后续输出
        assertTrue(originalResult == transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }


    @Test
    public void testCase1() {
        final double[] originalInput = {1.2, 2.3, 3.4};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase2() {
        final double[] originalInput = {0.7, 1.8, 2.9};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        final double[] originalInput = {-1.1, 2.5, 3.6};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        final double[] originalInput = {5.4, 6.7};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        final double[] originalInput = {2.1, -3.2, 4.3};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        final double[] originalInput = {1.1, 1.2, 1.3};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        final double[] originalInput = {3.5, 7.8, 9.9};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        final double[] originalInput = {-0.5, 2.6};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        final double[] originalInput = {10.7, 15.2, 20.3};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        final double[] originalInput = {-1.4, -2.5, -3.6};
        boolean originalResult = checkPositive.checkPositive_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}