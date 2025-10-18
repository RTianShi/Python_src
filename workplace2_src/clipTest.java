import example.clip;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class clipTest {
    private void applyMR_Assert(Integer[] originalInput, int[] originalResult) {

        //MR1:数组元置换（打乱顺序）
        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
        int[] transformResult1 = clip.clip_m(transformInput1, 1, 5);
        //MR2:数组元素常数加法
        Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
        int[] transformResult2 = clip.clip_m(transformInput2, 1, 5);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput);
        int[] transformResult3_1 = clip.clip_m(transformInput3_1, 1, 5);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput);
        int[] transformResult3_2 = clip.clip_m(transformInput3_2, 1, 5);
        //MR4:数组元素取倒数
//        Double[] transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput);
//        Integer[] transformInput4_1 = new Integer[transformInput4.length];
//        for (int i = 0; i < transformInput4.length; i++) {
//            transformInput4_1[i] = transformInput4[i].intValue();
//        }
//        int[] transformResult4 = clip.clip_m(transformInput4_1);
        //MR5:数组缩放变换
        Integer[] transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2);
        int[] transformResult5 = clip.clip_m(transformInput5, 1, 5);
        //MR6:数组反转变换
        Integer[] transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput);
        int[] transformResult6 = clip.clip_m(transformInput6, 1, 5);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput);
        int[] transformResult7_1 = clip.clip_m(transformInput7_1, 1, 5);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput);
        int[] transformResult7_2 = clip.clip_m(transformInput7_2, 1, 5);
        //MR8:重复输入数组
        Integer[] transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput);
        int[] transformResult8 = clip.clip_m(transformInput8, 1, 5);
        //MR9:复合转换一致性
        Integer[] transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3);
        int[] transformResult9 = clip.clip_m(transformInput9, 1, 5);
        //MR10:单调性检验
        Integer[] transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput);
        int[] transformResult10 = clip.clip_m(transformInput10, 1, 5);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput);
        int[] transformResult11 = clip.clip_m(transformInput11, 1, 5);
        //MR12:数值取反变换
//        Integer[] transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput);
//        int[] transformResult12 = clip.clip_m(transformInput12);
        //MR13:微小增量调整
//        Double[] transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput);
//        Integer[] transformInput13_1 = new Integer[transformInput13.length];
//        for (int i = 0; i < transformInput13_1.length; i++) {
//            transformInput13_1[i] = transformInput13[i].intValue();
//        }
//        double transformResult13 = clip.clip_m(transformInput13_1);
        //MR14:移除元素的效果（移除最大值）
        Integer[] transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput);
        int[] transformResult14 = clip.clip_m(transformInput14, 1, 5);
        //MR15:类三角函数的周期性
//        Integer[] transformInput15 = MetamorphicTestGenerator1.applyMR15(originalInput);
//        int[] transformResult15 = clip.clip_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput);
        int[] transformResult16 = clip.clip_m(transformInput16, 1, 5);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Integer[] transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2);
        int[] transformResult19 = clip.clip_m(transformInput19, 1, 5);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput);
        Integer[] transformInput20_1 = new Integer[transformInput20.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_1[i] = transformInput20[i].intValue();
        }
        int[] transformResult20 = clip.clip_m(transformInput20_1, 1, 5);
        //MR22:应用恒等变换
        Integer[] transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput);
        int[] transformResult22 = clip.clip_m(transformInput22, 1, 5);
        //----------------------------------------------------------
//        //OR1:和应该保持不变
        assertTrue(sum(originalResult) == sum(transformResult1));
        //OR2:源输出和小于等于后续输入
        assertTrue(sum(originalResult) <= sum(transformResult2));
        //OR3_1:和应该增大
        assertTrue(sum(originalResult) <= sum(transformResult3_1));
        //OR3_2:和应该增大
        assertTrue(sum(originalResult) <= sum(transformResult3_2));
        //OR4:和应该减少或保持不变
//        assertTrue(originalResult >= transformResult4);
        //OR5:源输出小于等于后续输出
        assertTrue(sum(originalResult) <= sum(transformResult5));
        //OR6:源输出和等于后续输出和
        assertTrue(sum(originalResult) == sum(transformResult6));
        //OR7_1:源输出和等于后续输出和
        assertTrue(sum(originalResult) == sum(transformResult7_1));
        //OR7_2:源输出和等于后续输出和
        assertTrue(sum(originalResult) == sum(transformResult7_2));
        //OR8:源输出小于等于后续输出
        assertTrue(sum(originalResult) <= sum(transformResult8));
        //OR9:源输出小于等于后续输出
        assertTrue(sum(originalResult) <= sum(transformResult9));
        //OR10:源输出小于等于后续输出
        assertTrue(sum(originalResult) <= sum(transformResult10));
        //OR11:源输出大于等于后续输出
        assertTrue(sum(originalResult) >= sum(transformResult11));
        //OR12:源输出负数等于后续输出
//        assertTrue(-originalResult == transformResult12);
//        OR13:源输出小于等于等于后续输出
//        assertTrue(originalResult <= transformResult13);
        //OR14:源输出大于等于等于后续输出
        assertTrue(sum(originalResult) >= sum(transformResult14));
        //OR15:源输出大于等于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于等于后续输出
        assertTrue(sum(originalResult) <= sum(transformResult16));
        //OR19:源输出小于等于等于后续输出
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformResult19));
        assertTrue(sum(originalResult) <= sum(transformResult19));
        //OR20:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + Arrays.toString(originalResult));
//        System.out.println("转换后的数组应该是：" + Arrays.toString(transformResult20));
        assertTrue(sum(originalResult) == sum(transformResult20));
        //OR22:源输出等于后续输出
        assertTrue(sum(originalResult) == sum(transformResult22));
    }

    private double sum(int[] array) {
        int sum = 0;
        for (int value : array) {
            sum += value;
        }
        return sum;
    }


    @Test
    public void testCase1() {
        Integer[] originalInput = {1, 3, 2, 6, 9};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase2() {
        Integer[] originalInput = {2, 1, 4, 4, 2};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        Integer[] originalInput = {4, -2, 4, 6, 2};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        Integer[] originalInput = {9, 2, 1, 5, 3, 2};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        Integer[] originalInput = {-1, 9, 1, -3, -3};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        Integer[] originalInput = {8, 3, 2, 6, 2, 3};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        Integer[] originalInput = {1, 2, 3, 4, -5, 6};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        Integer[] originalInput = {1, 2, 4, 2, 7, 5};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        Integer[] originalInput = {1, 1, 2, 4, 1, 2};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        Integer[] originalInput = {-2, 3, 1, 4, 7};
        int[] originalResult = clip.clip_m(originalInput, 1, 5);
        applyMR_Assert(originalInput, originalResult);
    }
}