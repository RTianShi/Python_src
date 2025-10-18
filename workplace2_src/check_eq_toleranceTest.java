import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class check_eq_toleranceTest {

    private void applyMR_Assert(Double[] originalInput1_1, Double[] originalInput1_2, boolean originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        boolean transformResult1 = check_eq_tolerance.check_eq_tolerance_m(transformInput1_1, transformInput1_2, 1e-9);
        //MR2:数组元素常数加法
        Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
        boolean transformResult2 = check_eq_tolerance.check_eq_tolerance_m(transformInput2_1, transformInput2_2, 1e-9);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_1);
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_1(originalInput1_2);
        boolean transformResult3_1 = check_eq_tolerance.check_eq_tolerance_m(transformInput3_1, transformInput3_2, 1e-9);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_3 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_1);
        Double[] transformInput3_4 = MetamorphicTestGenerator4.applyMR3_2(originalInput1_2);
        boolean transformResult3_2 = check_eq_tolerance.check_eq_tolerance_m(transformInput3_3, transformInput3_4, 1e-9);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator4.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator4.applyMR4(originalInput1_2);
        boolean transformResult4 = check_eq_tolerance.check_eq_tolerance_m(transformInput4_1, transformInput4_2, 1e-9);
        //MR5:数组缩放变换
        Double[] transformInput5_1 = MetamorphicTestGenerator4.applyMR5(originalInput1_1, 2);
        Double[] transformInput5_2 = MetamorphicTestGenerator4.applyMR5(originalInput1_2, 2);
        boolean transformResult5 = check_eq_tolerance.check_eq_tolerance_m(transformInput5_1, transformInput5_2, 1e-9);
        //MR6:数组反转变换
        Double[] transformInput6_1 = MetamorphicTestGenerator4.applyMR6(originalInput1_1);
        Double[] transformInput6_2 = MetamorphicTestGenerator4.applyMR6(originalInput1_2);
        boolean transformResult6 = check_eq_tolerance.check_eq_tolerance_m(transformInput6_1, transformInput6_2, 1e-9);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_1);
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_1(originalInput1_2);
        boolean transformResult7_1 = check_eq_tolerance.check_eq_tolerance_m(transformInput7_1, transformInput7_2, 1e-9);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_3 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_1);
        Double[] transformInput7_4 = MetamorphicTestGenerator4.applyMR7_2(originalInput1_2);
        boolean transformResult7_2 = check_eq_tolerance.check_eq_tolerance_m(transformInput7_3, transformInput7_4, 1e-9);
        //MR8:重复输入数组
        Double[] transformInput8_1 = MetamorphicTestGenerator4.applyMR8(originalInput1_1);
        Double[] transformInput8_2 = MetamorphicTestGenerator4.applyMR8(originalInput1_2);
        boolean transformResult8 = check_eq_tolerance.check_eq_tolerance_m(transformInput8_1, transformInput8_2, 1e-9);
        //MR9:复合转换一致性
        Double[] transformInput9_1 = MetamorphicTestGenerator4.applyMR9(originalInput1_1, 1);
        Double[] transformInput9_2 = MetamorphicTestGenerator4.applyMR9(originalInput1_2, 1);
        boolean transformResult9 = check_eq_tolerance.check_eq_tolerance_m(transformInput9_1, transformInput9_2, 1e-9);
        //MR10:单调性检验
        Double[] transformInput10_1 = MetamorphicTestGenerator4.applyMR10(originalInput1_1);
        Double[] transformInput10_2 = MetamorphicTestGenerator4.applyMR10(originalInput1_2);
        boolean transformResult10 = check_eq_tolerance.check_eq_tolerance_m(transformInput10_1, transformInput10_2, 1e-9);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11_1 = MetamorphicTestGenerator4.applyMR11(originalInput1_1);
        Double[] transformInput11_2 = MetamorphicTestGenerator4.applyMR11(originalInput1_2);
        boolean transformResult11 = check_eq_tolerance.check_eq_tolerance_m(transformInput11_1, transformInput11_2, 1e-9);
        //MR12:数值取反变换
        Double[] transformInput12_1 = MetamorphicTestGenerator4.applyMR12(originalInput1_1);
        Double[] transformInput12_2 = MetamorphicTestGenerator4.applyMR12(originalInput1_2);
        boolean transformResult12 = check_eq_tolerance.check_eq_tolerance_m(transformInput12_1, transformInput12_2, 1e-9);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator4.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator4.applyMR13(originalInput1_2);
        boolean transformResult13 = check_eq_tolerance.check_eq_tolerance_m(transformInput13_1, transformInput13_2, 1e-9);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14_1 = MetamorphicTestGenerator4.applyMR14(originalInput1_1);
        Double[] transformInput14_2 = MetamorphicTestGenerator4.applyMR14(originalInput1_2);
        boolean transformResult14 = check_eq_tolerance.check_eq_tolerance_m(transformInput14_1, transformInput14_2, 1e-9);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator4.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator4.applyMR15(originalInput1_2);
        boolean transformResult15 = check_eq_tolerance.check_eq_tolerance_m(transformInput15_1, transformInput15_2, 1e-9);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16_1 = MetamorphicTestGenerator4.applyMR16(originalInput1_1);
        Double[] transformInput16_2 = MetamorphicTestGenerator4.applyMR16(originalInput1_2);
        boolean transformResult16 = check_eq_tolerance.check_eq_tolerance_m(transformInput16_1, transformInput16_2, 1e-9);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19_1 = MetamorphicTestGenerator4.applyMR19(originalInput1_1, 2);
        Double[] transformInput19_2 = MetamorphicTestGenerator4.applyMR19(originalInput1_2, 2);
        boolean transformResult19 = check_eq_tolerance.check_eq_tolerance_m(transformInput19_1, transformInput19_2, 1e-9);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator4.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator4.applyMR20(originalInput1_2);
        boolean transformResult20 = check_eq_tolerance.check_eq_tolerance_m(transformInput20_1, transformInput20_2, 1e-9);
        //MR22:应用恒等变换
        Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
        Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
        boolean transformResult22 = check_eq_tolerance.check_eq_tolerance_m(transformInput22_1, transformInput22_2, 1e-9);
//        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertTrue(Arrays.equals(formatArray(originalResult, 2), formatArray(transformResult1, 2)));
        //OR2:源输出等于后续输出
        assertTrue(originalResult == transformResult2);
        //OR3_1:和应该保持不变
        assertTrue(originalResult == transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult == transformResult3_2);
        //OR4:和应该减少或保持不变
        assertTrue(originalResult == transformResult4);
        //OR5:源输出和等于后续输出
        assertTrue(originalResult == transformResult5);
        //OR6:源输出和等于后续输出和
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult6);
        assertTrue(originalResult == transformResult6);
        //OR7_1:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出数组等于后续输出数组
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出等于后续输出
        assertTrue(originalResult == transformResult8);
        //OR9:源输出等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
        assertTrue(originalResult == transformResult9);
        //OR10:源输出等于后续输出
        assertTrue(originalResult == transformResult10);
        //OR11:源输出等于后续输出
        assertTrue(originalResult == transformResult11);
        //OR12:源输出数组等于后续数组
        assertTrue(originalResult == transformResult12);
        //OR13:源输出等于后续输出
        assertTrue(originalResult == transformResult13);
        //OR14:源输出等于后续输出
        assertTrue(originalResult == transformResult14);
        //OR15:源输出等于后续输出
        assertTrue(originalResult == transformResult15);
        //OR16:源输出等于后续输出
        assertTrue(originalResult == transformResult16);
        //OR19:源输出小于等于后续输出
        assertTrue(originalResult == transformResult19);
        //OR20:源输出大于等于后续输出
        assertTrue(originalResult == transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testCase1() {
        Double[] originalInput1_1 = {1.0, 2.0, 3.0};
        Double[] originalInput1_2 = {1.0, 2.0, 3.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase2() {
        Double[] originalInput1_1 = {0.0, 2.0, 4.0};
        Double[] originalInput1_2 = {0.0, 2.0, 4.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        Double[] originalInput1_1 = {-1.0, 0.0, 1.0};
        Double[] originalInput1_2 = {-1.0, 0.0, 1.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        Double[] originalInput1_1 = {5.0, 7.0};
        Double[] originalInput1_2 = {5.0, 7.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        Double[] originalInput1_1 = {-2.0, -4.0, -6.0};
        Double[] originalInput1_2 = {-2.0, -4.0, -6.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        Double[] originalInput1_1 = {0.5, 1.5, 2.5};
        Double[] originalInput1_2 = {0.5, 1.5, 2.5};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        Double[] originalInput1_1 = {3.0, 6.0};
        Double[] originalInput1_2 = {3.0, 6.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        Double[] originalInput1_1 = {-1.0, 1.0, 0.0};
        Double[] originalInput1_2 = {-1.0, 1.0, 0.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        Double[] originalInput1_1 = {2.0, 3.0, 4.0, 5.0};
        Double[] originalInput1_2 = {2.0, 3.0, 4.0, 5.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        Double[] originalInput1_1 = {10.0, 20.0, 30.0};
        Double[] originalInput1_2 = {10.0, 20.0, 30.0};
        boolean originalResult = check_eq_tolerance.check_eq_tolerance_m(originalInput1_1, originalInput1_2, 1e-9);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}

