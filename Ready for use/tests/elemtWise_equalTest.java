import example.elemtWise_equal;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertTrue;

public class elemtWise_equalTest {

    private void applyMR_Assert(Integer[] originalInput1_1, Integer[] originalInput1_2, boolean[] originalResult) {
        //MR1:数组元置换（打乱顺序）
        Integer[] transformInput1_1 = MetamorphicTestGenerator1.applyMR1(originalInput1_1);
        Integer[] transformInput1_2 = MetamorphicTestGenerator1.applyMR1(originalInput1_2);
        boolean[] transformResult1 = elemtWise_equal.elemtWise_equal_m(transformInput1_1, transformInput1_2);
        //MR2:数组元素常数加法
        Integer[] transformInput2_1 = MetamorphicTestGenerator1.applyMR2(originalInput1_1);
        Integer[] transformInput2_2 = MetamorphicTestGenerator1.applyMR2(originalInput1_2);
        boolean[] transformResult2 = elemtWise_equal.elemtWise_equal_m(transformInput2_1, transformInput2_2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_1);
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_1(originalInput1_2);
        boolean[] transformResult3_1 = elemtWise_equal.elemtWise_equal_m(transformInput3_1, transformInput3_2);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_3 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_1);
        Integer[] transformInput3_4 = MetamorphicTestGenerator1.applyMR3_2(originalInput1_2);
        boolean[] transformResult3_2 = elemtWise_equal.elemtWise_equal_m(transformInput3_3, transformInput3_4);
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator1.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator1.applyMR4(originalInput1_2);
        Integer[] transformInput4_3 = new Integer[transformInput4_1.length];
        Integer[] transformInput4_4 = new Integer[transformInput4_2.length];
        for (int i = 0; i < transformInput4_1.length; i++) {
            transformInput4_3[i] = transformInput4_1[i].intValue();
            transformInput4_4[i] = transformInput4_2[i].intValue();
        }
        boolean[] transformResult4 = elemtWise_equal.elemtWise_equal_m(transformInput4_3, transformInput4_4);
        //MR5:数组缩放变换
        Integer[] transformInput5_1 = MetamorphicTestGenerator1.applyMR5(originalInput1_1, 2);
        Integer[] transformInput5_2 = MetamorphicTestGenerator1.applyMR5(originalInput1_2, 2);
        boolean[] transformResult5 = elemtWise_equal.elemtWise_equal_m(transformInput5_1, transformInput5_2);
        //MR6:数组反转变换
        Integer[] transformInput6_1 = MetamorphicTestGenerator1.applyMR6(originalInput1_1);
        Integer[] transformInput6_2 = MetamorphicTestGenerator1.applyMR6(originalInput1_2);
        boolean[] transformResult6 = elemtWise_equal.elemtWise_equal_m(transformInput6_1, transformInput6_2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_1);
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_1(originalInput1_2);
        boolean[] transformResult7_1 = elemtWise_equal.elemtWise_equal_m(transformInput7_1, transformInput7_2);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_3 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_1);
        Integer[] transformInput7_4 = MetamorphicTestGenerator1.applyMR7_2(originalInput1_2);
        boolean[] transformResult7_2 = elemtWise_equal.elemtWise_equal_m(transformInput7_3, transformInput7_4);
        //MR8:重复输入数组
        Integer[] transformInput8_1 = MetamorphicTestGenerator1.applyMR8(originalInput1_1);
        Integer[] transformInput8_2 = MetamorphicTestGenerator1.applyMR8(originalInput1_2);
        boolean[] transformResult8 = elemtWise_equal.elemtWise_equal_m(transformInput8_1, transformInput8_2);
        //MR9:复合转换一致性
        Integer[] transformInput9_1 = MetamorphicTestGenerator1.applyMR9(originalInput1_1, 1);
        Integer[] transformInput9_2 = MetamorphicTestGenerator1.applyMR9(originalInput1_2, 1);
        boolean[] transformResult9 = elemtWise_equal.elemtWise_equal_m(transformInput9_1, transformInput9_2);
        //MR10:单调性检验
        Integer[] transformInput10_1 = MetamorphicTestGenerator1.applyMR10(originalInput1_1);
        Integer[] transformInput10_2 = MetamorphicTestGenerator1.applyMR10(originalInput1_2);
        boolean[] transformResult10 = elemtWise_equal.elemtWise_equal_m(transformInput10_1, transformInput10_2);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11_1 = MetamorphicTestGenerator1.applyMR11(originalInput1_1);
        Integer[] transformInput11_2 = MetamorphicTestGenerator1.applyMR11(originalInput1_2);
        boolean[] transformResult11 = elemtWise_equal.elemtWise_equal_m(transformInput11_1, transformInput11_2);
        //MR12:数值取反变换
        Integer[] transformInput12_1 = MetamorphicTestGenerator1.applyMR12(originalInput1_1);
        Integer[] transformInput12_2 = MetamorphicTestGenerator1.applyMR12(originalInput1_2);
        boolean[] transformResult12 = elemtWise_equal.elemtWise_equal_m(transformInput12_1, transformInput12_2);
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator1.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator1.applyMR13(originalInput1_2);
        Integer[] transformInput13_3 = new Integer[transformInput13_1.length];
        Integer[] transformInput13_4 = new Integer[transformInput13_2.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_3[i] = transformInput13_1[i].intValue();
            transformInput13_4[i] = transformInput13_2[i].intValue();
        }
        boolean[] transformResult13 = elemtWise_equal.elemtWise_equal_m(transformInput13_3, transformInput13_4);
        //MR14:移除元素的效果（移除最大值）
        Integer[] transformInput14_1 = MetamorphicTestGenerator1.applyMR14(originalInput1_1);
        Integer[] transformInput14_2 = MetamorphicTestGenerator1.applyMR14(originalInput1_2);
        boolean[] transformResult14 = elemtWise_equal.elemtWise_equal_m(transformInput14_1, transformInput14_2);
        //MR15:类三角函数的周期性
        Double[] transformInput15_1 = MetamorphicTestGenerator1.applyMR15(originalInput1_1);
        Double[] transformInput15_2 = MetamorphicTestGenerator1.applyMR15(originalInput1_2);
        Integer[] transformInput15_3 = new Integer[transformInput15_1.length];
        Integer[] transformInput15_4 = new Integer[transformInput15_2.length];
        for (int i = 0; i < transformInput15_1.length; i++) {
            transformInput15_3[i] = transformInput15_1[i].intValue();
            transformInput15_4[i] = transformInput15_2[i].intValue();
        }
        boolean[] transformResult15 = elemtWise_equal.elemtWise_equal_m(transformInput15_3, transformInput15_4);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16_1 = MetamorphicTestGenerator1.applyMR16(originalInput1_1);
        Integer[] transformInput16_2 = MetamorphicTestGenerator1.applyMR16(originalInput1_2);
        boolean[] transformResult16 = elemtWise_equal.elemtWise_equal_m(transformInput16_1, transformInput16_2);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Integer[] transformInput19_1 = MetamorphicTestGenerator1.applyMR19(originalInput1_1, 2);
        Integer[] transformInput19_2 = MetamorphicTestGenerator1.applyMR19(originalInput1_2, 2);
        boolean[] transformResult19 = elemtWise_equal.elemtWise_equal_m(transformInput19_1, transformInput19_2);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator1.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator1.applyMR20(originalInput1_2);
        Integer[] transformInput20_3 = new Integer[transformInput20_1.length];
        Integer[] transformInput20_4 = new Integer[transformInput20_2.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_3[i] = transformInput20_1[i].intValue();
            transformInput20_4[i] = transformInput20_2[i].intValue();
        }
        boolean[] transformResult20 = elemtWise_equal.elemtWise_equal_m(transformInput20_3, transformInput20_4);
        //MR22:应用恒等变换
        Integer[] transformInput22_1 = MetamorphicTestGenerator1.applyMR22(originalInput1_1);
        Integer[] transformInput22_2 = MetamorphicTestGenerator1.applyMR22(originalInput1_2);
        boolean[] transformResult22 = elemtWise_equal.elemtWise_equal_m(transformInput22_1, transformInput22_2);
//        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult1));
        //OR2:源输出和加3等于后续输入
        assertTrue(Arrays.equals(originalResult, transformResult2));
        //OR3_1:和应该减小或保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_1));
        //OR3_2:和应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_2));
        //OR4:和应该减少或保持不变
        assertTrue(Arrays.equals(originalResult, transformResult4));
        //OR5:源输出和乘以2等于后续输出
        assertTrue(Arrays.equals(originalResult, transformResult5));
        //OR6:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult6));
        //OR7_1:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR7_2:源输出和等于后续输出和
        assertTrue(Arrays.equals(originalResult, transformResult7_2));
        //OR8:源输出等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult8));
        //OR9:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换前的数组应该是：" + originalResult * 1);
//        System.out.println("转换前的数组应该是：" + originalResult * 3);
//        System.out.println("转换后的数组应该是：" + transformResult9);
//        assertEquals(originalResult * 3, transformResult9, delta);
        //OR10:源输出小于等于后续输出
        assertTrue(Arrays.equals(originalResult, transformResult10));
        //OR11:源输出大于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult11));
        //OR12:源输出负数等于后续输出
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
        Integer[] originalInput1_1 = {1, 3, 2, 6, 9};
        Integer[] originalInput1_2 = {1, 3, 2, 6, 9};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase2() {
        Integer[] originalInput1_1 = {2, 1, 4, 4, 2};
        Integer[] originalInput1_2 = {2, 1, 4, 4, 2};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase3() {
        Integer[] originalInput1_1 = {4, -2, 4, 6, 2};
        Integer[] originalInput1_2 = {4, -2, 4, 6, 2};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase4() {
        Integer[] originalInput1_1 = {9, 2, 1, 5, 3, 2};
        Integer[] originalInput1_2 = {9, 2, 1, 5, 3, 2};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase5() {
        Integer[] originalInput1_1 = {-1, 9, 1, -3, -3};
        Integer[] originalInput1_2 = {-1, 9, 1, -3, -3};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase6() {
        Integer[] originalInput1_1 = {8, 3, 2, 6, 2, 3};
        Integer[] originalInput1_2 = {8, 3, 2, 6, 2, 3};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase7() {
        Integer[] originalInput1_1 = {1, 2, 3, 4, -5, 6};
        Integer[] originalInput1_2 = {1, 2, 3, 4, -5, 6};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase8() {
        Integer[] originalInput1_1 = {1, 2, 4, 2, 7, 5};
        Integer[] originalInput1_2 = {1, 2, 4, 2, 7, 5};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase9() {
        Integer[] originalInput1_1 = {1, 1, 2, 4, 1, 2};
        Integer[] originalInput1_2 = {1, 1, 2, 4, 1, 2};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }

    @Test
    public void testCase10() {
        Integer[] originalInput1_1 = {-2, 3, 1, 4, 7};
        Integer[] originalInput1_2 = {-2, 3, 1, 4, 7};
        boolean[] originalResult = elemtWise_equal.elemtWise_equal_m(originalInput1_1, originalInput1_2);
        applyMR_Assert(originalInput1_1, originalInput1_2, originalResult);
    }
}

