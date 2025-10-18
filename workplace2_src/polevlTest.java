import example.polevl;
import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class polevlTest {

    private void applyMR_Assert(Double x, Double[] originalInput, Integer N, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double transformResult1 = polevl.polevl_m(x, transformInput1, N);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double transformResult2 = polevl.polevl_m(x, transformInput2, N);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double transformResult3_1 = polevl.polevl_m(x, transformInput3_1, N);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double transformResult3_2 = polevl.polevl_m(x, transformInput3_2, N);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double transformResult4 = polevl.polevl_m(x, transformInput4, N);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double transformResult5 = polevl.polevl_m(x, transformInput5, N);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double transformResult6 = polevl.polevl_m(x, transformInput6, N);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double transformResult7_1 = polevl.polevl_m(x, transformInput7_1, N);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double transformResult7_2 = polevl.polevl_m(x, transformInput7_2, N);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double transformResult8 = polevl.polevl_m(x, transformInput8, N);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double transformResult9 = polevl.polevl_m(x, transformInput9, N);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double transformResult10 = polevl.polevl_m(x, transformInput10, N);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double transformResult11 = polevl.polevl_m(x, transformInput11, N);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double transformResult12 = polevl.polevl_m(x, transformInput12, N);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double transformResult13 = polevl.polevl_m(x, transformInput13, N);
        //MR14:移除元素的效果（移除最大值）
//        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
//        double transformResult14 = polevl.polevl_m(x,transformInput14,N);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double transformResult15 = polevl.polevl_m(x,transformInput15,N);
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double transformResult16 = polevl.polevl_m(x, transformInput16, N);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double transformResult19 = polevl.polevl_m(x, transformInput19, N);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double transformResult20 = polevl.polevl_m(x, transformInput20, N);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double transformResult22 = polevl.polevl_m(x, transformInput22, N);
        //----------------------------------------------------------
        double delta = 1e-9; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        assertTrue(originalResult == transformResult1);
        //OR2:源输出和加上n*3等于后续输入
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult2);
        assertTrue(originalResult <= transformResult2);
        //OR3_1:源输出加1等于后续输出
        assertTrue(originalResult <= transformResult3_1);
        //OR3_2:和应该保持不变
        assertTrue(originalResult <= transformResult3_2);
        //OR4:和应该增大
        assertTrue(originalResult >= transformResult4);
        //OR5:源输出等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出等于后续输出
//        assertEquals(originalResult, transformResult6, delta);
        //OR7_1:源输出和等于后续输出和
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出和等于后续输出和
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出*2等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出等于后续输出
//        assertTrue(originalResult <= transformResult9);
        //OR10:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult10);
        //OR11:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult11);
        //OR12:源输出等于后续输出
//        assertTrue(originalResult >= transformResult12);
        //OR13:源输出大于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult13);
        assertTrue(originalResult <= transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult16);
        //OR19:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult19);
        //OR20:源输出小于等于后续输出
//        assertEquals(originalResult, transformResult20, delta);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testPolevl_1() {
        Double x = 0.0;
        Double[] originalInput = {1.5, 2.2, 3.8, 4.3, 5.7};
        Integer N = 3;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_2() {
        Double x = 1.5;
        Double[] originalInput = {1.1, 2.2, 3.3, 4.4, 5.5};
        Integer N = 2;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_3() {
        Double x = -1.0;
        Double[] originalInput = {1.1, 1.1, 1.1, 1.1, 1.1};
        Integer N = 3;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_4() {
        Double x = 2.718;
        Double[] originalInput = {2.1, 3.12, 4.5, 5.07, 6.8};
        Integer N = 3;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_5() {
        Double x = 0.5;
        Double[] originalInput = {1.01, 1.02, 1.03, 1.04, 1.05};
        Integer N = 1;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_6() {
        Double x = -0.25;
        Double[] originalInput = {10.0, 20.0, 30.0, 40.0};
        Integer N = 2;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_7() {
        Double x = 1.0;
        Double[] originalInput = {2.1, 3.12, 4.5, 5.07, 6.8};
        Integer N = 3;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_8() {
        Double x = 0.75;
        Double[] originalInput = {1.01, 1.02, 1.03, 1.04, 1.05};
        Integer N = 3;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_9() {
        Double x = 4.5;
        Double[] originalInput = {2.12, 2.14, 2.16, 2.18};
        Integer N = 2;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }

    @Test
    public void testPolevl_10() {
        Double x = 3.141;
        Double[] originalInput = {1.112, 2.112, 3.112, 4.112};
        Integer N = 2;
        double originalResult = polevl.polevl_m(x, originalInput, N);
        applyMR_Assert(x, originalInput, N, originalResult);
    }
}