import example.sequential_search;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class sequential_searchTest {

    private void applyMR_Assert(Integer[] originalInput, Integer key, int originalResult) {
        //MR1:数组元置换（打乱顺序）
        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
        int transformResult1 = sequential_search.sequential_search_m(transformInput1, key);
        //MR2:数组元素常数加法
        Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
        int transformResult2 = sequential_search.sequential_search_m(transformInput2, key);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput);
        int transformResult3_1 = sequential_search.sequential_search_m(transformInput3_1, key);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput);
        int transformResult3_2 = sequential_search.sequential_search_m(transformInput3_2, key);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput);
        Integer[] transformInput4_1 = new Integer[transformInput4.length];
        for (int i = 0; i < transformInput4.length; i++) {
            transformInput4_1[i] = transformInput4[i].intValue();
        }
        int transformResult4 = sequential_search.sequential_search_m(transformInput4_1, key);
        //MR5:数组缩放变换
        Integer[] transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2);
        int transformResult5 = sequential_search.sequential_search_m(transformInput5, key);
        //MR6:数组反转变换
        Integer[] transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput);
        int transformResult6 = sequential_search.sequential_search_m(transformInput6, key);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput);
        int transformResult7_1 = sequential_search.sequential_search_m(transformInput7_1, key);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput);
        int transformResult7_2 = sequential_search.sequential_search_m(transformInput7_2, key);
        //MR8:重复输入数组
        Integer[] transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput);
        int transformResult8 = sequential_search.sequential_search_m(transformInput8, key);
        //MR9:复合转换一致性
        Integer[] transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3);
        int transformResult9 = sequential_search.sequential_search_m(transformInput9, key);
        //MR10:单调性检验
        Integer[] transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput);
        int transformResult10 = sequential_search.sequential_search_m(transformInput10, key);
        //MR11:边界值替换(把最大值替换成0)
        Integer[] transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput);
        int transformResult11 = sequential_search.sequential_search_m(transformInput11, key);
        //MR12:数值取反变换
        Integer[] transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput);
        int transformResult12 = sequential_search.sequential_search_m(transformInput12, key);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput);
        Integer[] transformInput13_1 = new Integer[transformInput13.length];
        for (int i = 0; i < transformInput13_1.length; i++) {
            transformInput13_1[i] = transformInput13[i].intValue();
        }
        double transformResult13 = sequential_search.sequential_search_m(transformInput13_1, key);
        //MR14:移除元素的效果（移除最大值）
//        Integer[] transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput);
//        int transformResult14 = sequential_search.sequential_search_m(transformInput14);
        //MR15:类三角函数的周期性
//        Integer[] transformInput15 = MetamorphicTestGenerator1.applyMR15(originalInput);
//        int transformResult15 =    sequential_search.   sequential_search_m(transformInput15);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Integer[] transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput);
        int transformResult16 = sequential_search.sequential_search_m(transformInput16, key);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Integer[] transformInput19 = MetamorphicTestGenerator1.applyMR19(originalInput, 2);
        int transformResult19 = sequential_search.sequential_search_m(transformInput19, key);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput);
        Integer[] transformInput20_1 = new Integer[transformInput20.length];
        for (int i = 0; i < transformInput20_1.length; i++) {
            transformInput20_1[i] = transformInput20[i].intValue();
        }
        double transformResult20 = sequential_search.sequential_search_m(transformInput20_1, key);
        //MR22:应用恒等变换
        Integer[] transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput);
        int transformResult22 = sequential_search.sequential_search_m(transformInput22, key);
        //----------------------------------------------------------
//        //OR1:和应该保持不变
//        assertTrue(originalResult == transformResult1);
        //OR2:源输出和加上n*3等于后续输入
//        assertTrue(originalResult <= transformResult2);
        //OR3_1:源输出加1等于后续输出
//        assertTrue(originalResult >= transformResult3_1);
        //OR3_2:和应该保持不变
//        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该增大
//        assertTrue(originalResult >= transformResult4);
        //OR5:源输出等于后续输出
//        assertTrue(originalResult <= transformResult5);
        //OR6:源输出等于后续输出
//        assertTrue(originalResult == transformResult6);
        //OR7_1:源输出和等于后续输出和
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出和等于后续输出和
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出*2等于后续输出
        assertTrue(originalResult == transformResult8);
        //OR9:源输出等于后续输出
//        assertTrue(originalResult <= transformResult9);
        //OR10:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult10);
        //OR11:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult11);
        //OR12:源输出等于后续输出
//        assertTrue(originalResult >= transformResult12);
        //OR13:源输出大于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult13);
//        assertTrue(originalResult == transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于后续输出
        assertTrue(originalResult == transformResult16);
        //OR19:源输出小于等于后续输出
        assertTrue(originalResult == transformResult19);
        //OR20:源输出小于等于后续输出
//        assertTrue(originalResult == transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testSequentialSearchCase1() {
        Integer[] originalInput = {5, 3, 8, 1, 2};
        Integer key = 2;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase2() {
        Integer[] originalInput = {10, 2, 7, 6, 3};
        Integer key = 1;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase3() {
        Integer[] originalInput = {-1, 0, 1, -2, 3};
        Integer key = 3;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase4() {
        Integer[] originalInput = {20, 15, 25, 5, 10};
        Integer key = 15;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase5() {
        Integer[] originalInput = {-5, -2, -8, -1, -3};
        Integer key = -1;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase6() {
        Integer[] originalInput = {7, 3, 1, 9, 2};
        Integer key = 0;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase7() {
        Integer[] originalInput = {0, 0, 0, 0, 0};
        Integer key = 0;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase8() {
        Integer[] originalInput = {100, 200, 150, 50, 75};
        Integer key = 150;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase9() {
        Integer[] originalInput = {8, 1, 3, 7, 2};
        Integer key = 3;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }

    @Test
    public void testSequentialSearchCase10() {
        Integer[] originalInput = {-10, -20, -5, -15, -25};
        Integer key = -25;
        int originalResult = sequential_search.sequential_search_m(originalInput, key);
        applyMR_Assert(originalInput, key, originalResult);
    }
}