import example.euc_Dist;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class euc_DistTest {

    private void applyMR_Assert(double[] originalInput1_1, double[] originalInput1_2, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        double[] transformInput1_1 = MetamorphicTestGenerator3.applyMR1(originalInput1_1);
        double[] transformInput1_2 = MetamorphicTestGenerator3.applyMR1(originalInput1_2);
        double transformResult1 = euc_Dist.euc_Dist_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        double[] transformInput2_1 = MetamorphicTestGenerator3.applyMR2(originalInput1_1);
        double[] transformInput2_2 = MetamorphicTestGenerator3.applyMR2(originalInput1_2);
        double transformResult2 = euc_Dist.euc_Dist_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        double[] transformInput3_1 = MetamorphicTestGenerator3.applyMR3_1(originalInput1_1);
        double[] transformInput3_2 = MetamorphicTestGenerator3.applyMR3_1(originalInput1_2);
        double transformResult3_1 = euc_Dist.euc_Dist_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        double[] transformInput3_3 = MetamorphicTestGenerator3.applyMR3_2(originalInput1_1);
        double[] transformInput3_4 = MetamorphicTestGenerator3.applyMR3_2(originalInput1_2);
        double transformResult3_2 = euc_Dist.euc_Dist_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        double[] transformInput4_1 = MetamorphicTestGenerator3.applyMR4(originalInput1_1);
        double[] transformInput4_2 = MetamorphicTestGenerator3.applyMR4(originalInput1_2);
        double transformResult4 = euc_Dist.euc_Dist_m(transformInput4_1, transformInput4_2);
        //MR5:数组缩放变换
        double[] transformInput5_1 = MetamorphicTestGenerator3.applyMR5(originalInput1_1, 2);
        double[] transformInput5_2 = MetamorphicTestGenerator3.applyMR5(originalInput1_2, 2);
        double transformResult5 = euc_Dist.euc_Dist_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        double[] transformInput6_1 = MetamorphicTestGenerator3.applyMR6(originalInput1_1);
        double[] transformInput6_2 = MetamorphicTestGenerator3.applyMR6(originalInput1_2);
        double transformResult6 = euc_Dist.euc_Dist_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        double[] transformInput7_1 = MetamorphicTestGenerator3.applyMR7_1(originalInput1_1);
        double[] transformInput7_2 = MetamorphicTestGenerator3.applyMR7_1(originalInput1_2);
        double transformResult7_1 = euc_Dist.euc_Dist_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        double[] transformInput7_3 = MetamorphicTestGenerator3.applyMR7_2(originalInput1_1);
        double[] transformInput7_4 = MetamorphicTestGenerator3.applyMR7_2(originalInput1_2);
        double transformResult7_2 = euc_Dist.euc_Dist_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        double[] transformInput8_1 = MetamorphicTestGenerator3.applyMR8(originalInput1_1);
        double[] transformInput8_2 = MetamorphicTestGenerator3.applyMR8(originalInput1_2);
        double transformResult8 = euc_Dist.euc_Dist_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        double[] transformInput9_1 = MetamorphicTestGenerator3.applyMR9(originalInput1_1, 1);
        double[] transformInput9_2 = MetamorphicTestGenerator3.applyMR9(originalInput1_2, 1);
        double transformResult9 = euc_Dist.euc_Dist_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        double[] transformInput10_1 = MetamorphicTestGenerator3.applyMR10(originalInput1_1);
        double[] transformInput10_2 = MetamorphicTestGenerator3.applyMR10(originalInput1_2);
        double transformResult10 = euc_Dist.euc_Dist_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        double[] transformInput11_1 = MetamorphicTestGenerator3.applyMR11(originalInput1_1);
        double[] transformInput11_2 = MetamorphicTestGenerator3.applyMR11(originalInput1_2);
        double transformResult11 = euc_Dist.euc_Dist_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        double[] transformInput12_1 = MetamorphicTestGenerator3.applyMR12(originalInput1_1);
        double[] transformInput12_2 = MetamorphicTestGenerator3.applyMR12(originalInput1_2);
        double transformResult12 = euc_Dist.euc_Dist_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        double[] transformInput13_1 = MetamorphicTestGenerator3.applyMR13(originalInput1_1);
        double[] transformInput13_2 = MetamorphicTestGenerator3.applyMR13(originalInput1_2);
        double transformResult13 = euc_Dist.euc_Dist_m(transformInput13_1, transformInput13_2);
        //MR14:移除元素的效果（移除最大值）
        double[] transformInput14_1 = MetamorphicTestGenerator3.applyMR14(originalInput1_1);
        double[] transformInput14_2 = MetamorphicTestGenerator3.applyMR14(originalInput1_2);
        double transformResult14 = euc_Dist.euc_Dist_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        double[] transformInput15_1 = MetamorphicTestGenerator3.applyMR15(originalInput1_1);
        double[] transformInput15_2 = MetamorphicTestGenerator3.applyMR15(originalInput1_2);
        double transformResult15 = euc_Dist.euc_Dist_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        double[] transformInput16_1 = MetamorphicTestGenerator3.applyMR16(originalInput1_1);
        double[] transformInput16_2 = MetamorphicTestGenerator3.applyMR16(originalInput1_2);
        double transformResult16 = euc_Dist.euc_Dist_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        double[] transformInput19_1 = MetamorphicTestGenerator3.applyMR19(originalInput1_1, 2);
        double[] transformInput19_2 = MetamorphicTestGenerator3.applyMR19(originalInput1_2, 2);
        double transformResult19 = euc_Dist.euc_Dist_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        double[] transformInput20_1 = MetamorphicTestGenerator3.applyMR20(originalInput1_1);
        double[] transformInput20_2 = MetamorphicTestGenerator3.applyMR20(originalInput1_2);
        double transformResult20 = euc_Dist.euc_Dist_m(transformInput20_1, transformInput20_2);
        //MR22:应用恒等变换
        double[] transformInput22_1 = MetamorphicTestGenerator3.applyMR22(originalInput1_1);
        double[] transformInput22_2 = MetamorphicTestGenerator3.applyMR22(originalInput1_2);
        double transformResult22 = euc_Dist.euc_Dist_m(transformInput22_1, transformInput22_2);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertEquals(originalResult, transformResult1, 0.0001);
        //OR2:源输出和加3等于后续输入
        assertEquals(originalResult, transformResult2, delta);
        //OR3_1:和应该减小或保持不变
        assertTrue(originalResult == transformResult3_1);
        //OR3_2:应该保持不变
        assertTrue(originalResult == transformResult3_2);
        //OR4:和应该减少或保持不变
        assertTrue(originalResult >= transformResult4);
        //OR5:源输出和乘以2等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
        assertEquals(originalResult, transformResult6, delta);
        //OR7_1:源输出数组等于后续输出数组
        assertEquals(originalResult, transformResult7_1, delta);
        //OR7_2:源输出数组等于后续输出数组
        assertEquals(originalResult, transformResult7_2, delta);
        //OR8:源输出等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertTrue(originalResult >= transformResult9);
        //OR10:源输出小于等于后续输出
        assertEquals(originalResult, transformResult10, delta);
        //OR11:源输出等于后续输出
//        assertTrue(originalResult == transformResult11);
        //OR12:源输出数组等于后续数组
        assertEquals(originalResult, transformResult12, delta);
        //OR13:源输出等于等于后续输出
        assertEquals(originalResult, transformResult13, delta);
        //OR14:源输出等于等于后续输出
        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出等于等于后续输出
        assertTrue(originalResult <= transformResult16);
        //OR19:源输出等于等于后续输出
        assertTrue(originalResult <= transformResult19);
        //OR20:源输出等于后续输出
        assertEquals(originalResult, transformResult20, delta);
        //OR22:源输出等于后续输出
        assertEquals(originalResult, transformResult22, delta);
    }

    @Test
    public void testCase1() {
        double[] originalInput1_1 = {1.234, 2.56, 3.78};
        double[] originalInput1_2 = {1.234, 2.56, 3.780};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);

    }

    @Test
    public void testCase2() {
        double[] originalInput1_1 = {-1.11, 4.5, 3.001};
        double[] originalInput1_2 = {-1.1101, 4.5001, 3.0011};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        double[] originalInput1_1 = {-1.11, 4.5, 3.001};
        double[] originalInput1_2 = {7.0009, -3.1201, 0.9901};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        double[] originalInput1_1 = {7.001, -3.12, 0.99};
        double[] originalInput1_2 = {7.0009, -3.1201, 0.9901};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        double[] originalInput1_1 = {5.0, -8.765, 1.222};
        double[] originalInput1_2 = {5.0, -8.765, 1.222};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        double[] originalInput1_1 = {5.0, -8.765, 1.222};
        double[] originalInput1_2 = {2.333, 4.444, 1.0};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        double[] originalInput1_1 = {2.333, 4.444, 1.0};
        double[] originalInput1_2 = {2.333, 4.444, 1.0};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        double[] originalInput1_1 = {6.789, 1.23, -5.67};
        double[] originalInput1_2 = {0.1, -3.456, 2.789};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        double[] originalInput1_1 = {6.789, 1.23, -5.67};
        double[] originalInput1_2 = {6.7891, 1.23, -5.6699};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        double[] originalInput1_1 = {0.1, -3.456, 2.789};
        double[] originalInput1_2 = {0.1, -3.456, 2.789};
        double originalResult = euc_Dist.euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}