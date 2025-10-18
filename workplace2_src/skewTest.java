import example.skew;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class skewTest {

    private void applyMR_Assert(Double[] originalInput, double originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1 = MetamorphicTestGenerator4.applyMR1(originalInput);
        double transformResult1 = skew.skew_m(transformInput1);
        //MR2:数组元素常数加法
        Double[] transformInput2 = MetamorphicTestGenerator4.applyMR2(originalInput);
        double transformResult2 = skew.skew_m(transformInput2);
        //MR3_1:加入单位元不变性（加法的单位元0）
        Double[] transformInput3_1 = MetamorphicTestGenerator4.applyMR3_1(originalInput);
        double transformResult3_1 = skew.skew_m(transformInput3_1);
        //MR3_2:加入单位元不变性（乘法的单位元1）
        Double[] transformInput3_2 = MetamorphicTestGenerator4.applyMR3_2(originalInput);
        double transformResult3_2 = skew.skew_m(transformInput3_2);
        //MR4:数组元素取倒数
        Double[] transformInput4 = MetamorphicTestGenerator4.applyMR4(originalInput);
        double transformResult4 = skew.skew_m(transformInput4);
        //MR5:数组缩放变换
        Double[] transformInput5 = MetamorphicTestGenerator4.applyMR5(originalInput, 2);
        double transformResult5 = skew.skew_m(transformInput5);
        //MR6:数组反转变换
        Double[] transformInput6 = MetamorphicTestGenerator4.applyMR6(originalInput);
        double transformResult6 = skew.skew_m(transformInput6);
        //MR7_1:中立操作的恒等变换（所有元素乘以1）
        Double[] transformInput7_1 = MetamorphicTestGenerator4.applyMR7_1(originalInput);
        double transformResult7_1 = skew.skew_m(transformInput7_1);
        //MR7_2:中立操作的恒等变换（所有元素加上0）
        Double[] transformInput7_2 = MetamorphicTestGenerator4.applyMR7_2(originalInput);
        double transformResult7_2 = skew.skew_m(transformInput7_2);
        //MR8:重复输入数组
        Double[] transformInput8 = MetamorphicTestGenerator4.applyMR8(originalInput);
        double transformResult8 = skew.skew_m(transformInput8);
        //MR9:复合转换一致性
        Double[] transformInput9 = MetamorphicTestGenerator4.applyMR9(originalInput, 3);
        double transformResult9 = skew.skew_m(transformInput9);
        //MR10:单调性检验
        Double[] transformInput10 = MetamorphicTestGenerator4.applyMR10(originalInput);
        double transformResult10 = skew.skew_m(transformInput10);
        //MR11:边界值替换(把最大值替换成0)
        Double[] transformInput11 = MetamorphicTestGenerator4.applyMR11(originalInput);
        double transformResult11 = skew.skew_m(transformInput11);
        //MR12:数值取反变换
        Double[] transformInput12 = MetamorphicTestGenerator4.applyMR12(originalInput);
        double transformResult12 = skew.skew_m(transformInput12);
        //MR13:微小增量调整
        Double[] transformInput13 = MetamorphicTestGenerator4.applyMR13(originalInput);
        double transformResult13 = skew.skew_m(transformInput13);
        //MR14:移除元素的效果（移除最大值）
        Double[] transformInput14 = MetamorphicTestGenerator4.applyMR14(originalInput);
        double transformResult14 = skew.skew_m(transformInput14);
        //MR15:类三角函数的周期性
//        Double[] transformInput15 = MetamorphicTestGenerator4.applyMR15(originalInput);
//        double transformResult15 =  skew. skew_m(transformInput15 );
        //MR16:重复值稳健性(复制输入中的一个元素)
        Double[] transformInput16 = MetamorphicTestGenerator4.applyMR16(originalInput);
        double transformResult16 = skew.skew_m(transformInput16);
        //MR19:输入重复（元素复制）将元素a重复多次插入序列中
        Double[] transformInput19 = MetamorphicTestGenerator4.applyMR19(originalInput, 2);
        double transformResult19 = skew.skew_m(transformInput19);
        //MR20:边界值灵敏度（给最小值增加一个极小值）
        Double[] transformInput20 = MetamorphicTestGenerator4.applyMR20(originalInput);
        double transformResult20 = skew.skew_m(transformInput20);
        //MR22:应用恒等变换
        Double[] transformInput22 = MetamorphicTestGenerator4.applyMR22(originalInput);
        double transformResult22 = skew.skew_m(transformInput22);
        //----------------------------------------------------------
        double delta = 0.0001; // Delta for floating-point comparison
//        //OR1:和应该保持不变
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult1);
        assertEquals(originalResult, transformResult1, delta);
        //OR2:源输出和加上n*3等于后续输入
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult2);
//        assertTrue(originalResult >= transformResult2);
        //OR3_1:源输出加1等于后续输出
//        assertTrue(originalResult >= transformResult3_1);
        //OR3_2:和应该保持不变
//        assertTrue(originalResult >= transformResult3_2);
        //OR4:和应该增大
//        assertTrue(originalResult >= transformResult4);
        //OR5:源输出等于后续输出
        assertTrue(originalResult <= transformResult5);
        //OR6:源输出等于后续输出
        assertEquals(originalResult, transformResult6, delta);
        //OR7_1:源输出和等于后续输出和s
        assertTrue(originalResult == transformResult7_1);
        //OR7_2:源输出和等于后续输出和
        assertTrue(originalResult == transformResult7_2);
        //OR8:源输出*2等于后续输出
        assertTrue(originalResult <= transformResult8);
        //OR9:源输出等于后续输出
        assertTrue(originalResult <= transformResult9);
        //OR10:源输出小于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult10);
//        assertTrue(originalResult >= transformResult10);
        //OR11:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult11);
        //OR12:源输出等于后续输出
//        assertTrue(originalResult >= transformResult12);
        //OR13:源输出大于等于后续输出
//        System.out.println("转换前的数组应该是：" + originalResult);
//        System.out.println("转换后的数组应该是：" + transformResult13);
//        assertTrue(originalResult >= transformResult13);
        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult14);
        //OR15:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult15);
        //OR16:源输出小于等于后续输出
//        assertTrue(originalResult >= transformResult16);
        //OR19:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult19);
        //OR20:源输出小于等于后续输出
        assertTrue(originalResult <= transformResult20);
        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);
    }

    @Test
    public void testSkewCase1() {
        Double[] originalInput = {2.56, 3.56, 4.56};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase2() {
        Double[] originalInput = {5.57, 5.58, 5.59};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase3() {
        Double[] originalInput = {6.00, 7.00, 8.00};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase4() {
        Double[] originalInput = {4.25, 5.25, 6.25};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase5() {
        Double[] originalInput = {-1.25, -1.35, -1.45};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase6() {
        Double[] originalInput = {-1.11, 0.99, 3.456, 7.89};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase7() {
        Double[] originalInput = {-10.85, -11.25, -12.35};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase8() {
        Double[] originalInput = {4.55, 2.56, 4.55};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase9() {
        Double[] originalInput = {7.135, 8.135, 9.135};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testSkewCase10() {
        Double[] originalInput = {8.88, 10.88, 12.88};
        double originalResult = skew.skew_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}