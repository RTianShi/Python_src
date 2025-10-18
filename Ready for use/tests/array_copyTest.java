import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertTrue;

public class array_copyTest {
    private void applyMR_Assert(int[] originalInput, int[] originalResult) {

        //MR1:数组元置换（打乱顺序）
//        int[] transformInput1 = MetamorphicTestGenerator2.applyMR1(originalInput);
//        int[] transformResult1 = array_copy.array_copy_m(transformInput1, 3);
        //MR2:数组元素常数加法
//        int[] transformInput2 = MetamorphicTestGenerator2.applyMR2(originalInput);
//        int[] transformResult2 = array_copy.array_copy_m(transformInput2, k);
        //MR3_1:加入单位元不变性（加法的单位元0）
//        int[] transformInput3_1 = MetamorphicTestGenerator2.applyMR3_1(originalInput);
//        int[] transformResult3_1 = array_copy.array_copy_m(transformInput3_1, k);
        //MR3_2:加入单位元不变性（乘法的单位元1）
//        int[] transformInput3_2 = MetamorphicTestGenerator2.applyMR3_2(originalInput);
//        int[] transformResult3_2 = array_copy.array_copy_m(transformInput3_2, k);
//        //MR4:数组元素取倒数
//        Double[] transformInput4 = MetamorphicTestGenerator2.applyMR4(originalInput);
//        int[] transformInput4_1 = new int[transformInput4.length];
//        for (int i = 0; i < transformInput4.length; i++) {
//            transformInput4_1[i] = transformInput4[i].intValue();
//        }
//        int[] transformResult4 = array_copy.array_copy_m(transformInput4_1, 2);
//        //MR5:数组缩放变换
//        int[] transformInput5 = MetamorphicTestGenerator2.applyMR5(originalInput, 2);
//        int[] transformResult5 = array_copy.array_copy_m(transformInput5, 2);
//        //MR6:数组反转变换
//        int[] transformInput6 = MetamorphicTestGenerator2.applyMR6(originalInput);
//        int[] transformResult6 = array_copy.array_copy_m(transformInput6, 2);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        int[] transformInput7_1 = MetamorphicTestGenerator2.applyMR7_1(originalInput);
        int[] transformResult7_1 = array_copy.array_copy_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        int[] transformInput7_2 = MetamorphicTestGenerator2.applyMR7_2(originalInput);
        int[] transformResult7_2 = array_copy.array_copy_m(transformInput7_2);
//        //MR8:重复输入数组
//        int[] transformInput8 = MetamorphicTestGenerator2.applyMR8(originalInput);
//        int[] transformResult8 = array_copy.array_copy_m(transformInput8, 2);
//        //MR9:复合转换一致性
//        int[] transformInput9 = MetamorphicTestGenerator2.applyMR9(originalInput, 3);
//        int[] transformResult9 = array_copy.array_copy_m(transformInput9, 2);
//        //MR10:单调性检验
//        int[] transformInput10 = MetamorphicTestGenerator2.applyMR10(originalInput);
//        int[] transformResult10 = array_copy.array_copy_m(transformInput10, 2);
//        //MR11:边界值替换(把最大值替换成0)
//        int[] transformInput11 = MetamorphicTestGenerator2.applyMR11(originalInput);
//        int[] transformResult11 = array_copy.array_copy_m(transformInput11, 2);
//        //MR12:数值取反变换
//        int[] transformInput12 = MetamorphicTestGenerator2.applyMR12(originalInput);
//        int[] transformResult12 = array_copy.array_copy_m(transformInput12, 2);
//        //MR13:微小增量调整
//        Double[] transformInput13 = MetamorphicTestGenerator2.applyMR13(originalInput);
//        int[] transformInput13_1 = new int[transformInput13.length];
//        for (int i = 0; i < transformInput13_1.length; i++) {
//            transformInput13_1[i] = transformInput13[i].intValue();
//        }
//        int[] transformResult13 = array_copy.array_copy_m(transformInput13_1, 2);
//        //MR14:移除元素的效果（移除最大值）
//        int[] transformInput14 = MetamorphicTestGenerator2.applyMR14(originalInput);
//        int[] transformResult14 = array_copy.array_copy_m(transformInput14, 2);
//        //MR15:类三角函数的周期性
////        int[] transformInput15 = MetamorphicTestGenerator2.applyMR15(originalInput);
////        int transformResult15 = array_copy.array_copy_m(transformInput15);
//        //MR16:重复值稳健性(复制输入中的一个元素)
//        int[] transformInput16 = MetamorphicTestGenerator2.applyMR16(originalInput);
//        int[] transformResult16 = array_copy.array_copy_m(transformInput16, 2);
//        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
////        int[] transformInput19 = MetamorphicTestGenerator2.applyMR19(originalInput, 2);
////        int transformResult19 = array_copy.array_copy_m(transformInput19);
//        //MR20:边界值灵敏度（给最小值增加一个极小值）
//        Double[] transformInput20 = MetamorphicTestGenerator2.applyMR20(originalInput);
//        int[] transformInput20_1 = new int[transformInput20.length];
//        for (int i = 0; i < transformInput20_1.length; i++) {
//            transformInput20_1[i] = transformInput20[i].intValue();
//        }
//        int[] transformResult20 = array_copy.array_copy_m(transformInput20_1, 2);
        //MR22:应用恒等变换
        int[] transformInput22 = MetamorphicTestGenerator2.applyMR22(originalInput);
        int[] transformResult22 = array_copy.array_copy_m(transformInput22);
        //----------------------------------------------------------
        //OR1:和应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult1));
        //OR2:源输出和加上n*3等于后续输入
//        assertTrue(Arrays.equals(originalResult, transformResult2));
        //OR3_1:数组应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_1));
        //OR3_2:数组应该保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult3_2));
        //OR4:和应该减少或保持不变
//        assertTrue(Arrays.equals(originalResult, transformResult4));
        //OR5:源输出和乘以2等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult5));
        //OR6:源输出和等于后续输出和
//        assertTrue(originalResult == transformResult6);
        //OR7_1:源输出数组和后续输出数组保持不变
        assertTrue(Arrays.equals(originalResult, transformResult7_1));
        //OR7_2:源输出数组和后续输出数组保持不变
        assertTrue(Arrays.equals(originalResult, transformResult7_2));
        //OR8:源输出*2等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult8));
        //OR9:源输出*3等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult9));
        //OR10:源输出小于等于后续输出
//        assertTrue(Arrays.equals(originalResult, transformResult10));
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


    @Test
    public void testCase1() {
        int[] originalInput = {1, 3, 2, 6, 9};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase2() {
        int[] originalInput = {2, 1, 4, 4, 2};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        int[] originalInput = {4, -2, 4, 6, 2};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        int[] originalInput = {9, 2, 1, 5, 3, 2};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        int[] originalInput = {-1, 9, 1, -3, -3};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        int[] originalInput = {8, 3, 2, 6, 2, 3};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        int[] originalInput = {1, 2, 3, 4, -5, 6};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        int[] originalInput = {1, 2, 4, 2, 7, 5};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        int[] originalInput = {1, 1, 2, 4, 1, 2};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        int[] originalInput = {-2, 3, 1, 4, 7};
        int[] originalResult = array_copy.array_copy_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}