import example.s_add;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class s_addTest {
    private void applyMR_Assert(int[] originalInput1_1, int[] originalInput1_2, int[] originalResult) {
//MR1:数组元置换（打乱顺序）
        int[] transformInput1_1 = MetamorphicTestGenerator2.applyMR1(originalInput1_1);
        int[] transformInput1_2 = MetamorphicTestGenerator2.applyMR1(originalInput1_2);
        s_add.s_add_m(transformInput1_1, transformInput1_2);
        int[] transformResult1 = transformInput1_1;
        //MR2:数组元素常数加法
        int[] transformInput2_1 = MetamorphicTestGenerator2.applyMR2(originalInput1_1);
        int[] transformInput2_2 = MetamorphicTestGenerator2.applyMR2(originalInput1_2);
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_1));
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput1_2));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_1));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput2_2));
        s_add.s_add_m(transformInput2_1, transformInput2_2);
        int[] transformResult2 = transformInput2_1;
        //MR3_1:加入单位元不变性（加法的单位元0）
        int[] transformInput3_1 = MetamorphicTestGenerator2.applyMR3_1(originalInput1_1);
        int[] transformInput3_2 = MetamorphicTestGenerator2.applyMR3_1(originalInput1_2);
        s_add.s_add_m(transformInput3_1, transformInput3_2);
        int[] transformResult3_1 = transformInput3_1;
        //MR3_2:加入单位元不变性（乘法的单位元1）
        int[] transformInput3_3 = MetamorphicTestGenerator2.applyMR3_2(originalInput1_1);
        int[] transformInput3_4 = MetamorphicTestGenerator2.applyMR3_2(originalInput1_2);
        s_add.s_add_m(transformInput3_3, transformInput3_4);
        int[] transformResult3_2 = transformInput3_3;
        //MR4:数组元素取倒数
        Double[] transformInput4_1 = MetamorphicTestGenerator2.applyMR4(originalInput1_1);
        Double[] transformInput4_2 = MetamorphicTestGenerator2.applyMR4(originalInput1_2);
        int[] transformInput4_3 = new int[transformInput4_1.length];
        int[] transformInput4_4 = new int[transformInput4_2.length];
        for (int i = 0; i < transformInput4_1.length; i++) {
            transformInput4_3[i] = transformInput4_1[i].intValue();
            transformInput4_4[i] = transformInput4_2[i].intValue();
        }
        s_add.s_add_m(transformInput4_3, transformInput4_4);
        int[] transformResult4 = transformInput4_3;
        //MR5:数组缩放变换
        int[] transformInput5_1 = MetamorphicTestGenerator2.applyMR5(originalInput1_1, 2);
        int[] transformInput5_2 = MetamorphicTestGenerator2.applyMR5(originalInput1_2, 2);
        s_add.s_add_m(transformInput5_1, transformInput5_2);
        int[] transformResult5 = transformInput5_1;
        //MR6:数组反转变换
        int[] transformInput6_1 = MetamorphicTestGenerator2.applyMR6(originalInput1_1);
        int[] transformInput6_2 = MetamorphicTestGenerator2.applyMR6(originalInput1_2);
        s_add.s_add_m(transformInput6_1, transformInput6_2);
        int[] transformResult6 = transformInput6_1;
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        int[] transformInput7_1 = MetamorphicTestGenerator2.applyMR7_1(originalInput1_1);
        int[] transformInput7_2 = MetamorphicTestGenerator2.applyMR7_1(originalInput1_2);
        s_add.s_add_m(transformInput7_1, transformInput7_2);
        int[] transformResult7_1 = transformInput7_1;
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        int[] transformInput7_3 = MetamorphicTestGenerator2.applyMR7_2(originalInput1_1);
        int[] transformInput7_4 = MetamorphicTestGenerator2.applyMR7_2(originalInput1_2);
        s_add.s_add_m(transformInput7_3, transformInput7_4);
        int[] transformResult7_2 = transformInput7_3;
        //MR8:重复输入数组
        int[] transformInput8_1 = MetamorphicTestGenerator2.applyMR8(originalInput1_1);
        int[] transformInput8_2 = MetamorphicTestGenerator2.applyMR8(originalInput1_2);
        s_add.s_add_m(transformInput8_1, transformInput8_2);
        int[] transformResult8 = transformInput8_1;
        //MR9:复合转换一致性
        int[] transformInput9_1 = MetamorphicTestGenerator2.applyMR9(originalInput1_1, 1);
        int[] transformInput9_2 = MetamorphicTestGenerator2.applyMR9(originalInput1_2, 1);
        s_add.s_add_m(transformInput9_1, transformInput9_2);
        int[] transformResult9 = transformInput9_1;
        //MR10:单调性检验
        int[] transformInput10_1 = MetamorphicTestGenerator2.applyMR10(originalInput1_1);
        int[] transformInput10_2 = MetamorphicTestGenerator2.applyMR10(originalInput1_2);
        s_add.s_add_m(transformInput10_1, transformInput10_2);
        int[] transformResult10 = transformInput10_1;
        //MR11:边界值替换(把最大值替换成0)
        int[] transformInput11_1 = MetamorphicTestGenerator2.applyMR11(originalInput1_1);
        int[] transformInput11_2 = MetamorphicTestGenerator2.applyMR11(originalInput1_2);
        s_add.s_add_m(transformInput11_1, transformInput11_2);
        int[] transformResult11 = transformInput11_1;
        //MR12:数值取反变换
        int[] transformInput12_1 = MetamorphicTestGenerator2.applyMR12(originalInput1_1);
        int[] transformInput12_2 = MetamorphicTestGenerator2.applyMR12(originalInput1_2);
        s_add.s_add_m(transformInput12_1, transformInput12_2);
        int[] transformResult12 = transformInput12_1;
        //MR13:微小增量调整
        Double[] transformInput13_1 = MetamorphicTestGenerator2.applyMR13(originalInput1_1);
        Double[] transformInput13_2 = MetamorphicTestGenerator2.applyMR13(originalInput1_2);
        int[] transformInput13_3 = new int[transformInput13_1.length];
        int[] transformInput13_4 = new int[transformInput13_2.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_3[i] = transformInput13_1[i].intValue();
            transformInput13_4[i] = transformInput13_2[i].intValue();
        }
        s_add.s_add_m(transformInput13_3, transformInput13_4);
        int[] transformResult13 = transformInput13_3;
//        //MR14:移除元素的效果（移除最大值）
//        int[] transformInput14_1 = MetamorphicTestGenerator2.applyMR14(originalInput1_1);
//        int[] transformInput14_2 = MetamorphicTestGenerator2.applyMR14(originalInput1_2);
//        s_add.s_add_m(transformInput14_1, transformInput14_2);
//        int[] transformResult14 = transformInput14_1;
        //MR15:类三角函数的周期性
//        int[] transformInput15_1 = MetamorphicTestGenerator2.applyMR15(originalInput1_1);
//        int[] transformInput15_2 = MetamorphicTestGenerator2.applyMR15(originalInput1_2);
//        int[] transformResult15 = s_add.s_add_m(transformInput15_1, transformInput15_2);
        //MR16:重复值稳健性(复制输入中的一个元素)
        int[] transformInput16_1 = MetamorphicTestGenerator2.applyMR16(originalInput1_1);
        int[] transformInput16_2 = MetamorphicTestGenerator2.applyMR16(originalInput1_2);
        s_add.s_add_m(transformInput16_1, transformInput16_2);
        int[] transformResult16 = transformInput16_1;
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        int[] transformInput19_1 = MetamorphicTestGenerator2.applyMR19(originalInput1_1, 2);
        int[] transformInput19_2 = MetamorphicTestGenerator2.applyMR19(originalInput1_2, 2);
        s_add.s_add_m(transformInput19_1, transformInput19_2);
        int[] transformResult19 = transformInput19_1;
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20_1 = MetamorphicTestGenerator2.applyMR20(originalInput1_1);
        Double[] transformInput20_2 = MetamorphicTestGenerator2.applyMR20(originalInput1_2);
        int[] transformInput20_3 = new int[transformInput20_1.length];
        int[] transformInput20_4 = new int[transformInput20_2.length];
        for (int i = 0; i < transformInput4_1.length; i++) {
            transformInput20_3[i] = transformInput20_1[i].intValue();
            transformInput20_4[i] = transformInput20_2[i].intValue();
        }
        s_add.s_add_m(transformInput20_3, transformInput20_4);
        int[] transformResult20 = transformInput20_3;
        //MR22:应用恒等变换
        int[] transformInput22_1 = MetamorphicTestGenerator2.applyMR22(originalInput1_1);
        int[] transformInput22_2 = MetamorphicTestGenerator2.applyMR22(originalInput1_2);
        s_add.s_add_m(transformInput22_1, transformInput22_2);
        int[] transformResult22 = transformInput22_1;
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
        //OR1:和应该保持不变
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult1));
        assertArraySumEqual(originalResult, transformResult1);
        //OR2:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:数组应该保持不变
        assertArraySumEqual(originalResult, transformResult3_1);
        //OR3_2:数组应该保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult3_2);
        //OR4:和应该减少或保持不变
        assertArraySumDecreasedOrEqual(originalResult, transformResult4);
        //OR5:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult5);
        //OR6:源输出和等于后续输出和
        assertArraySumEqual(originalResult, transformResult6);
        //OR7_1:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_1);
        //OR7_2:源输出数组和后续输出数组保持不变
        assertArraySumEqual(originalResult, transformResult7_2);
        //OR8:源输出*2等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult8);
        //OR9:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult9);
        //OR10:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult11);
        //OR12:源输出大于后续输出
        assertArraySumDecreasedOrEqual(originalResult, transformResult12);
        //OR13:源输出小于等于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult13);
        //OR14:源输出大于等于等于后续输出
//        assertArraySumDecreasedOrEqual(originalResult, transformResult14);
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult16));
        assertArraySumIncreasedOrEqual(originalResult, transformResult16);
        //OR19:源输出小于等于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
        assertArraySumIncreasedOrEqual(originalResult, transformResult19);
        //OR20:源输出小于等于后续输出
        assertArraySumIncreasedOrEqual(originalResult, transformResult20);
        //OR22:源输出等于后续输出
        assertArraySumEqual(originalResult, transformResult22);
    }

    private void assertArraySumIncreasedOrEqual(int[] original, int[] transformed) {
        assertTrue(sum(transformed) >= sum(original));
    }

    private void assertArraySumDecreasedOrEqual(int[] original, int[] transformed) {
        assertTrue(sum(transformed) <= sum(original));
    }

    private void assertArraySumEqual(int[] original, int[] transformed) {
        double delta = 1e-9;
        assertEquals(sum(transformed), sum(original), delta);
    }

    private int sum(int[] array) {
        int sum = 0;
        for (int value : array) {
            sum += value;
        }
        return sum;
    }


    @Test
    public void testSAddCase1() {
        int[] array1 = {1, 2, 3};
        int[] array2 = {4, 5, 6};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase2() {
        int[] array1 = {10, 20, 30, 40};
        int[] array2 = {1, 2, 3, 4};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase3() {
        int[] array1 = {15, 25, 35};
        int[] array2 = {20, 25, 30};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase4() {
        int[] array1 = {5, 10, 15, 20};
        int[] array2 = {5, 10, 15, 20};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase5() {
        int[] array1 = {0, 2, 4};
        int[] array2 = {1, 3, 5};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase6() {
        int[] array1 = {7, 8};
        int[] array2 = {9, 10};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase7() {
        int[] array1 = {5, 10, 15};
        int[] array2 = {5, 10, 15};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase8() {
        int[] array1 = {100, 200};
        int[] array2 = {300, 400};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase9() {
        int[] array1 = {1, 21, 1, 10};
        int[] array2 = {1, 1, 1, 1};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }

    @Test
    public void testSAddCase10() {
        int[] array1 = {30, 35, 40, 45};
        int[] array2 = {20, 25, 30, 35};
        int[] array3 = Arrays.copyOf(array1, array1.length);
        s_add.s_add_m(array1, array2);//源输出结果在array1
        applyMR_Assert(array3, array2, array1);

    }
}