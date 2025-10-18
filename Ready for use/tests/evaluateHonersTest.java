import example.evaluateHoners;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class evaluateHonersTest {

    private void applyMR_Assert(Double[] originalInput, Double argument, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double transformResult1 = evaluateHoners.evaluateHoners_m(transformInput1, argument);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double transformResult2 = evaluateHoners.evaluateHoners_m(transformInput2, argument);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double transformResult3_1 = evaluateHoners.evaluateHoners_m(transformInput3_1, argument);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double transformResult3_2 = evaluateHoners.evaluateHoners_m(transformInput3_2, argument);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double transformResult4 = evaluateHoners.evaluateHoners_m(transformInput4, argument);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double transformResult5 = evaluateHoners.evaluateHoners_m(transformInput5, argument);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double transformResult6 = evaluateHoners.evaluateHoners_m(transformInput6, argument);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double transformResult7_1 = evaluateHoners.evaluateHoners_m(transformInput7_1, argument);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double transformResult7_2 = evaluateHoners.evaluateHoners_m(transformInput7_2, argument);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double transformResult8 = evaluateHoners.evaluateHoners_m(transformInput8, argument);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double transformResult9 = evaluateHoners.evaluateHoners_m(transformInput9, argument);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double transformResult10 = evaluateHoners.evaluateHoners_m(transformInput10, argument);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double transformResult11 = evaluateHoners.evaluateHoners_m(transformInput11, argument);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double transformResult12 = evaluateHoners.evaluateHoners_m(transformInput12, argument);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double transformResult13 = evaluateHoners.evaluateHoners_m(transformInput13, argument);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double transformResult14 = evaluateHoners.evaluateHoners_m(transformInput14, argument);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double transformResult15 = evaluateHoners.evaluateHoners_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double transformResult16 = evaluateHoners.evaluateHoners_m(transformInput16, argument);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double transformResult19 = evaluateHoners.evaluateHoners_m(transformInput19, argument);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double transformResult20 = evaluateHoners.evaluateHoners_m(transformInput20, argument);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double transformResult22 = evaluateHoners.evaluateHoners_m(transformInput22, argument);
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
        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        assertTrue(originalResult <= transformResult19);
        //OR20:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testCase1() {
        Double[] originalInput = {1.1, -2.22, 3.333};
        Double argument = 2.5;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);

    }

    @Test
    public void testCase2() {
        Double[] originalInput = {4.56, 4.57, 4.58};
        Double argument = 2.6;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase3() {
        Double[] originalInput = {1.35, 1.46, 1.58, 1.96};
        Double argument = 0.85;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase4() {
        Double[] originalInput = {7.85, 6.33, 4.25};
        Double argument = 2.55;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase5() {
        Double[] originalInput = {1.56, 2.57, 3.58};
        Double argument = 2.0;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase6() {
        Double[] originalInput = {-0.123, 2.456, 4.567};
        Double argument = 3.3;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase7() {
        Double[] originalInput = {-1.85, 6.31, 4.66};
        Double argument = 2.25;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase8() {
        Double[] originalInput = {2.718, 3.141, 0.567};
        Double argument = 0.001;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase9() {
        Double[] originalInput = {4.65, 7.03, 6.08};
        Double argument = 5.0;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }

    @Test
    public void testCase10() {
        Double[] originalInput = {1.29, 0.36, 4.22};
        Double argument = 0.58;
        double originalResult = evaluateHoners.evaluateHoners_m(originalInput, argument);
        applyMR_Assert(originalInput, argument, originalResult);
    }
}