import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertTrue;

public class dec_arrayTest {

    private void applyMR_Assert(Integer[] originalInput, Integer k, Integer[] originalResult) {
        //MR1:数组元置换（打乱顺序）
        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
        Integer[] transformResult1 = dec_array.dec_array_m(transformInput1, k);
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalInput));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformInput1));
        //MR2:数组元素常数加法
        Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
        Integer[] transformResult2 = dec_array.dec_array_m(transformInput2, k);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput);
        Integer[] transformResult3_1 = dec_array.dec_array_m(transformInput3_1, k);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput);
        Integer[] transformResult3_2 = dec_array.dec_array_m(transformInput3_2, k);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput);
        Integer[] transformInput4_1 = new Integer[transformInput4.length];
        for (int i = 0; i < transformInput4.length; i++) {
            transformInput4_1[i] = transformInput4[i].intValue();
        }
        Integer[] transformResult4 = dec_array.dec_array_m(transformInput4_1, k);
        //MR5:数组缩放变换
        Integer[] transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2);
        Integer[] transformResult5 = dec_array.dec_array_m(transformInput5, k);
        //MR6:数组反转变换
        Integer[] transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput);
        Integer[] transformResult6 = dec_array.dec_array_m(transformInput6, k);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput);
        Integer[] transformResult7_1 = dec_array.dec_array_m(transformInput7_1, k);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput);
        Integer[] transformResult7_2 = dec_array.dec_array_m(transformInput7_2, k);
        //MR8:重复输入数组
        Integer[] transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput);
        Integer[] transformResult8 = dec_array.dec_array_m(transformInput8, k);
        //MR9:复合转换一致性
        Integer[] transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3);
        Integer[] transformResult9 = dec_array.dec_array_m(transformInput9, k);
        //MR10:单调性检验
        Integer[] transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput);
        Integer[] transformResult10 = dec_array.dec_array_m(transformInput10, k);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput);
        Integer[] transformResult11 = dec_array.dec_array_m(transformInput11, k);
        //MR12:数值取反变换
        Integer[] transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput);
        Integer[] transformResult12 = dec_array.dec_array_m(transformInput12, k);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput);
        Integer[] transformInput13_1 = new Integer[transformInput13.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_1[i] = transformInput13[i].intValue();
        }
        Integer[] transformResult13 = dec_array.dec_array_m(transformInput13_1, k);
        //MR14:移除元素的效果（移除最大值）
        Integer[] transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput);
        Integer[] transformResult14 = dec_array.dec_array_m(transformInput14, k);
        //MR15:类三角函数的周期性
//        Integer[] transformInput15 = MetamorphicTestGenerator1.applyMR15(originalInput);
//        Integer[] transformResult15 = dec_array.dec_array_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput);
        Integer[] transformResult16 = dec_array.dec_array_m(transformInput16, k);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
//        Integer[] transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2);
//        Integer[] transformResult19 = dec_array.dec_array_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput);
        Integer[] transformInput20_1 = new Integer[transformInput20.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_1[i] = transformInput20[i].intValue();
        }
        Integer[] transformResult20 = dec_array.dec_array_m(transformInput20_1, k);
        //MR22:应用恒等变换
        Integer[] transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput);
        Integer[] transformResult22 = dec_array.dec_array_m(transformInput22, k);
        //----------------------------------------------------------
        //OR1:和应该保持不变
//        System.out.println("转换前的输出应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的输出应该是：" + Arrays.toString(transformResult1));
        assertArraySumEqual(originalResult, transformResult1);
        //OR2:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult2);
        //OR3_1:数组应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_1));
        //OR3_2:数组应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_2));
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
//        assertTrue(Arrays.equals(originalResult, transformResult8));
        //OR9:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult9);
        //OR10:和应该增加或保持不变
        assertArraySumIncreasedOrEqual(originalResult, transformResult10);
        //OR11:源输出大于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult11));
        //OR12:源输出负数等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult12));
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
        //assertTrue(originalResult <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(Arrays.equals(originalResult, transformResult22));
    }

    private void assertArraySumIncreasedOrEqual(Integer[] original, Integer[] transformed) {
        assertTrue(sum(transformed) >= sum(original));
    }

    private void assertArraySumDecreasedOrEqual(Integer[] original, Integer[] transformed) {
        assertTrue(sum(transformed) <= sum(original));
    }

    private void assertArraySumEqual(Integer[] original, Integer[] transformed) {
        assertTrue(sum(transformed) == sum(original));
    }

    private int sum(Integer[] array) {
        int sum = 0;
        for (int value : array) {
            sum += value;
        }
        return sum;
    }

    @Test
    public void testCase1() {
        Integer[] originalInput = {1, 2, 3, 4, 5};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = -5;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase2() {
        Integer[] originalInput = {7, 7, 7};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase3() {
        Integer[] originalInput = {6, 6, 6};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase4() {
        Integer[] originalInput = {5, 5, 5};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase5() {
        Integer[] originalInput = {1, 1, 1};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 0;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase6() {
        Integer[] originalInput = {100, 80, 60, 40, 20};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = -1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase7() {
        Integer[] originalInput = {5, 15, 25};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = -1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase8() {
        Integer[] originalInput = {4, 4, 4, 4, 4};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase9() {
        Integer[] originalInput = {8, 6, 4};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = -1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }

    @Test
    public void testCase10() {
        Integer[] originalInput = {2, 2, 2};
        Integer[] originalInput1 = Arrays.copyOf(originalInput, originalInput.length);
        Integer k = 1;
        Integer[] originalResult = dec_array.dec_array_m(originalInput, k);
        applyMR_Assert(originalInput1, k, originalResult);
    }
}