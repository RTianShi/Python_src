import example.entropy;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class entropyTest {

    private void applyMR_Assert(final Double[] originalInput, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        final Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double transformResult1 = entropy.entropy_m(transformInput1);
        //MR2:数组元素常数加法
        final Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double transformResult2 = entropy.entropy_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        final Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double transformResult3_1 = entropy.entropy_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        final Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double transformResult3_2 = entropy.entropy_m(transformInput3_2);
        //MR4:数组元素取倒数
        final Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double transformResult4 = entropy.entropy_m(transformInput4);
        //MR5:数组缩放变换
        final Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double transformResult5 = entropy.entropy_m(transformInput5);
        //MR6:数组反转变换
        final Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double transformResult6 = entropy.entropy_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        final Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double transformResult7_1 = entropy.entropy_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        final Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double transformResult7_2 = entropy.entropy_m(transformInput7_2);
        //MR8:重复输入数组
        final Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double transformResult8 = entropy.entropy_m(transformInput8);
        //MR9:复合转换一致性
        final Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double transformResult9 = entropy.entropy_m(transformInput9);
        //MR10:单调性检验
        final Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double transformResult10 = entropy.entropy_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        final Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double transformResult11 = entropy.entropy_m(transformInput11);
        //MR12:数值取反变换
        final Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double transformResult12 = entropy.entropy_m(transformInput12);
        //MR13:微小增量调整
        final Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double transformResult13 = entropy.entropy_m(transformInput13);
        //MR14:移除元素的效果（移除最大值）
        final Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double transformResult14 = entropy.entropy_m(transformInput14);
        //MR15:类三角函数的周期性
//        final Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double transformResult15 = entropy.entropy_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        final Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double transformResult16 = entropy.entropy_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        final Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double transformResult19 = entropy.entropy_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        final Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double transformResult20 = entropy.entropy_m(transformInput20);
        //MR22:应用恒等变换
        final Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double transformResult22 = entropy.entropy_m(transformInput22);
//        //----------------------------------------------------------
//        //OR1:和应该保持不变
        assertEquals(originalResult, transformResult1, 0.0001);
        //OR2:源输出和加3等于后续输入
//        assertEquals(originalResult + 3, transformResult2, delta);
        //OR3_1:和应该减小或保持不变
        assertTrue(originalResult <= transformResult3_1);
        //OR3_2:应该保持不变
        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(originalResult == transformResult4);
        //OR5:源输出和乘以2等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
        assertEquals(originalResult, transformResult6, 0.0001);
        //OR7_1:源输出数组等于后续输出数组
        assertEquals(originalResult, transformResult7_1, 0.0001);
        //OR7_2:源输出数组等于后续输出数组
        assertEquals(originalResult, transformResult7_2, 0.0001);
        //OR8:源输出等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertTrue(originalResult >= transformResult9);
        //OR10:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult9);
        //OR11:源输出等于后续输出
//        assertTrue(originalResult == transformResult11);
        //OR12:源输出数组等于后续数组
//        assertTrue(originalResult <= transformResult9);
        //OR13:源输出等于等于后续输出
        assertTrue(originalResult <= transformResult13);
        //OR14:源输出等于等于后续输出
//        assertTrue(originalResult == transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出等于等于后续输出
//        assertTrue(originalResult >= transformResult16);
        //OR19:源输出等于等于后续输出
//        assertTrue(originalResult >= transformResult19);
        //OR20:源输出等于后续输出
//        assertTrue(originalResult == transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testCase1() {
        final Double[] originalInput = {1.2, 3.45, 6.789};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);

    }

    @Test
    public void testCase2() {
        final Double[] originalInput = {7.38, 6.59, 4.44};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        final Double[] originalInput = {0.25, 1.69, 4.38, 5.12};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        final Double[] originalInput = {7.001, 3.14, 2.22};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        final Double[] originalInput = {5.04, 7.23, 6.14, 5.55};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        final Double[] originalInput = {7.66, 2.13, 4.06, 8.15};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        final Double[] originalInput = {5.65, 9.86};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        final Double[] originalInput = {100.56, 200.34, 400.56};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        final Double[] originalInput = {5.69, 7.69, 8.69};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        final Double[] originalInput = {5.16, 7.95, 7.33};
        double originalResult = entropy.entropy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}