import example.find_euc_Dist;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class find_euc_DistTest {

    private void applyMR_Assert(Integer[] originalInput1_1, Integer[] originalInput1_2, double originalResult) {
//MR1:数组元置换（打乱顺序）
        Integer[] transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1_1);
        Integer[] transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput1_2);
        double transformResult1 = find_euc_Dist.find_euc_Dist_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        Integer[] transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1_1);
        Integer[] transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput1_2);
        double transformResult2 = find_euc_Dist.find_euc_Dist_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_1);
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_2);
        double transformResult3_1 = find_euc_Dist.find_euc_Dist_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_1);
        Integer[] transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_2);
        double transformResult3_2 = find_euc_Dist.find_euc_Dist_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput1_2);
        Integer[] transformInput4_3 = new Integer[transformInput4_1.length];
        Integer[] transformInput4_4 = new Integer[transformInput4_2.length];
        for (int i = 0; i < transformInput4_1.length; i++) {
            transformInput4_3[i] = transformInput4_1[i].intValue();
            transformInput4_4[i] = transformInput4_2[i].intValue();
        }
        double transformResult4 = find_euc_Dist.find_euc_Dist_m(transformInput4_3, transformInput4_4);
        //MR5:数组缩放变换
        Integer[] transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1_1, 2);
        Integer[] transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput1_2, 2);
        double transformResult5 = find_euc_Dist.find_euc_Dist_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        Integer[] transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1_1);
        Integer[] transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput1_2);
        double transformResult6 = find_euc_Dist.find_euc_Dist_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_1);
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_2);
        double transformResult7_1 = find_euc_Dist.find_euc_Dist_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_3 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_1);
        Integer[] transformInput7_4 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_2);
        double transformResult7_2 = find_euc_Dist.find_euc_Dist_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        Integer[] transformInput8_1 = MetamorphicTestGenerator1.applyMR8(originalInput1_1);
        Integer[] transformInput8_2 = MetamorphicTestGenerator1.applyMR8(originalInput1_2);
        double transformResult8 = find_euc_Dist.find_euc_Dist_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        Integer[] transformInput9_1 = MetamorphicTestGenerator1.applyMR9(originalInput1_1, 1);
        Integer[] transformInput9_2 = MetamorphicTestGenerator1.applyMR9(originalInput1_2, 1);
        double transformResult9 = find_euc_Dist.find_euc_Dist_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        Integer[] transformInput10_1 = MetamorphicTestGenerator1.applyMR10(originalInput1_1);
        Integer[] transformInput10_2 = MetamorphicTestGenerator1.applyMR10(originalInput1_2);
        double transformResult10 = find_euc_Dist.find_euc_Dist_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11_1 = MetamorphicTestGenerator1.applyMR11(originalInput1_1);
        Integer[] transformInput11_2 = MetamorphicTestGenerator1.applyMR11(originalInput1_2);
        double transformResult11 = find_euc_Dist.find_euc_Dist_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        Integer[] transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1_1);
        Integer[] transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput1_2);
        double transformResult12 = find_euc_Dist.find_euc_Dist_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput1_2);
        Integer[] transformInput13_3 = new Integer[transformInput13_1.length];
        Integer[] transformInput13_4 = new Integer[transformInput13_2.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_3[i] = transformInput13_1[i].intValue();
            transformInput13_4[i] = transformInput13_2[i].intValue();
        }
        double transformResult13 = find_euc_Dist.find_euc_Dist_m(transformInput13_3, transformInput13_4);
        //MR14:移除元素的效果（移除最大值）
//        Integer[] transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1_1);
//        Integer[] transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput1_2);
//        double transformResult14 = find_euc_Dist.find_euc_Dist_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput1_2);
        Integer[] transformInput15_3 = new Integer[transformInput15_1.length];
        Integer[] transformInput15_4 = new Integer[transformInput15_2.length];
        for (int i = 0; i < transformInput15_1.length; i++) {
            transformInput15_3[i] = transformInput15_1[i].intValue();
            transformInput15_4[i] = transformInput15_2[i].intValue();
        }
        double transformResult15 = find_euc_Dist.find_euc_Dist_m(transformInput15_3, transformInput15_4);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1_1);
        Integer[] transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput1_2);
        double transformResult16 = find_euc_Dist.find_euc_Dist_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Integer[] transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1_1, 2);
        Integer[] transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput1_2, 2);
        double transformResult19 = find_euc_Dist.find_euc_Dist_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput1_2);
        Integer[] transformInput20_3 = new Integer[transformInput20_1.length];
        Integer[] transformInput20_4 = new Integer[transformInput20_2.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_3[i] = transformInput20_1[i].intValue();
            transformInput20_4[i] = transformInput20_2[i].intValue();
        }
        double transformResult20 = find_euc_Dist.find_euc_Dist_m(transformInput20_3, transformInput20_4);
        //MR22:应用恒等变换
        Integer[] transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1_1);
        Integer[] transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput1_2);
        double transformResult22 = find_euc_Dist.find_euc_Dist_m(transformInput22_1, transformInput22_2);
//        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult1, 2)));
        //OR2:源输出等于后续输出
        assertEquals(originalResult, transformResult2, delta);
        //OR3_1:和应该保持不变
        assertTrue(originalResult == transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult == transformResult3_2);
        //OR4:和应该减少或保持不变
//        assertTrue(originalResult == transformResult4);
        //OR5:源输出和等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出和等于后续输出和
        assertTrue(originalResult == transformResult6);
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出等于后续输出
//        assertTrue(originalResult == transformResult9);
        //OR10:源输出等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出等于后续输出
//        assertTrue(originalResult == transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult == transformResult12);
        //OR13:源输出等于后续输出
//        assertEquals(originalResult, transformResult13, delta);
        //OR14:源输出等于后续输出
//        assertTrue(originalResult == transformResult14);
        //OR15:源输出等于后续输出
//        assertTrue(originalResult == transformResult15);
        //OR16:源输出等于后续输出
        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult19);
        //OR20:源输出大于等于后续输出
//        assertTrue(originalResult == transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testCase1() {
        Integer[] originalInput1_1 = {10, 20, 30, 40, 50};
        Integer[] originalInput1_2 = {6, 7, 8, 9, 10};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);

    }

    @Test
    public void testCase2() {
        Integer[] originalInput1_1 = {10, 9, 8, 7, 6};
        Integer[] originalInput1_2 = {5, 4, 3, 2, 1};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        Integer[] originalInput1_1 = {0, 0, 0, 0, 0};
        Integer[] originalInput1_2 = {1, 1, 1, 1, 1};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        Integer[] originalInput1_1 = {-1, -2, -3, -4, -5};
        Integer[] originalInput1_2 = {5, 4, 3, 2, 1};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        Integer[] originalInput1_1 = {100, 200, 300, 400, 500};
        Integer[] originalInput1_2 = {50, 150, 250, 350, 450};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        Integer[] originalInput1_1 = {-10, -20, -30, -40, -50};
        Integer[] originalInput1_2 = {-5, -15, -25, -35, -45};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        Integer[] originalInput1_1 = {1, 1, 1, 1, 1};
        Integer[] originalInput1_2 = {1, 1, 1, 1, 1};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        Integer[] originalInput1_1 = {5, 6, 7, 8, 9};
        Integer[] originalInput1_2 = {1, 2, 3, 4, 5};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        Integer[] originalInput1_1 = {3, 6, 9, 12, 15};
        Integer[] originalInput1_2 = {1, 2, 3, 4, 5};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        Integer[] originalInput1_1 = {-3, -6, -9, -12, -15};
        Integer[] originalInput1_2 = {3, 6, 9, 12, 15};
        double originalResult = find_euc_Dist.find_euc_Dist_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}