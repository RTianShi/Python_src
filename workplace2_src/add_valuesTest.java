import org.junit.Test;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertTrue;

public class add_valuesTest {
    private void applyMR_Assert(Integer[] originalInput, int originalResult) {

//        //MR1:Swap the first and last elements（交换第一个元素和最后一个元素）
//        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
//        int transformResult1 = add_values.add_values_m(transformInput1);
//        //MR2:By moving all elements one position to the left(将元素向左移动一个位置)
//        Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
//        int transformResult2 = add_values.add_values_m(transformInput2);
//        //OR1:和应该保持不变
//        assertTrue(originalResult == transformResult1);
//        //OR2:
//        assertTrue(originalResult == transformResult2);

        List<AssertionError> errors = new ArrayList<>();

        //MR1:数组元置换（打乱顺序）
//        Integer[] transformInput1 = MetamorphicTestGenerator1.applyMR1(originalInput);
//        int transformResult1 = add_values.add_values_m(transformInput1);
        // MR2: 数组元素常数加法
        try {
            Integer[] transformInput2 = MetamorphicTestGenerator1.applyMR2(originalInput);
            int transformResult2 = add_values.add_values_m(transformInput2);
            assertTrue(originalResult + originalInput.length * 3 == transformResult2);
            logKill("MR2", false);
        } catch (AssertionError e) {
            logKill("MR2", true);
            throw e;
        }

        // MR3_1: 加法单位元0
        try {
            Integer[] transformInput3_1 = MetamorphicTestGenerator1.applyMR3_1(originalInput);
            int transformResult3_1 = add_values.add_values_m(transformInput3_1);
            assertTrue(originalResult == transformResult3_1);
            logKill("MR3_1", false);
        } catch (AssertionError e) {
            logKill("MR3_1", true);
            throw e;
        }

        // MR3_2: 乘法单位元1
        try {
            Integer[] transformInput3_2 = MetamorphicTestGenerator1.applyMR3_2(originalInput);
            int transformResult3_2 = add_values.add_values_m(transformInput3_2);
            assertTrue(originalResult + 1 == transformResult3_2);
            logKill("MR3_2", false);
        } catch (AssertionError e) {
            logKill("MR3_2", true);
            throw e;
        }

        // MR4: 取倒数后转int
        try {
            Double[] transformInput4 = MetamorphicTestGenerator1.applyMR4(originalInput);
            Integer[] transformInput4_1 = new Integer[transformInput4.length];
            for (int i = 0; i < transformInput4.length; i++) {
                transformInput4_1[i] = transformInput4[i].intValue();
            }
            int transformResult4 = add_values.add_values_m(transformInput4_1);
            assertTrue(originalResult >= transformResult4);
            logKill("MR4", false);
        } catch (AssertionError e) {
            logKill("MR4", true);
            throw e;
        }

        // MR5: 缩放变换 *2
        try {
            Integer[] transformInput5 = MetamorphicTestGenerator1.applyMR5(originalInput, 2);
            int transformResult5 = add_values.add_values_m(transformInput5);
            assertTrue(originalResult * 2 == transformResult5);
            logKill("MR5", false);
        } catch (AssertionError e) {
            logKill("MR5", true);
            throw e;
        }

        // MR6: 反转
        try {
            Integer[] transformInput6 = MetamorphicTestGenerator1.applyMR6(originalInput);
            int transformResult6 = add_values.add_values_m(transformInput6);
            assertTrue(originalResult == transformResult6);
            logKill("MR6", false);
        } catch (AssertionError e) {
            logKill("MR6", true);
            throw e;
        }

        // MR7_1: 所有元素乘1
        try {
            Integer[] transformInput7_1 = MetamorphicTestGenerator1.applyMR7_1(originalInput);
            int transformResult7_1 = add_values.add_values_m(transformInput7_1);
            assertTrue(originalResult == transformResult7_1);
            logKill("MR7_1", false);
        } catch (AssertionError e) {
            logKill("MR7_1", true);
            throw e;
        }

        // MR7_2: 所有元素加0
        try {
            Integer[] transformInput7_2 = MetamorphicTestGenerator1.applyMR7_2(originalInput);
            int transformResult7_2 = add_values.add_values_m(transformInput7_2);
            assertTrue(originalResult == transformResult7_2);
            logKill("MR7_2", false);
        } catch (AssertionError e) {
            logKill("MR7_2", true);
            throw e;
        }

        // MR8: 重复整个数组
        try {
            Integer[] transformInput8 = MetamorphicTestGenerator1.applyMR8(originalInput);
            int transformResult8 = add_values.add_values_m(transformInput8);
            assertTrue(originalResult * 2 == transformResult8);
            logKill("MR8", false);
        } catch (AssertionError e) {
            logKill("MR8", true);
            throw e;
        }

        // MR9: 重复3次
        try {
            Integer[] transformInput9 = MetamorphicTestGenerator1.applyMR9(originalInput, 3);
            int transformResult9 = add_values.add_values_m(transformInput9);
            assertTrue(originalResult * 3 == transformResult9);
            logKill("MR9", false);
        } catch (AssertionError e) {
            logKill("MR9", true);
            throw e;
        }

        // MR10: 单调增加
        try {
            Integer[] transformInput10 = MetamorphicTestGenerator1.applyMR10(originalInput);
            int transformResult10 = add_values.add_values_m(transformInput10);
            assertTrue(originalResult <= transformResult10);
            logKill("MR10", false);
        } catch (AssertionError e) {
            logKill("MR10", true);
            throw e;
        }

        // MR11: 最大值替换为0
        try {
            Integer[] transformInput11 = MetamorphicTestGenerator1.applyMR11(originalInput);
            int transformResult11 = add_values.add_values_m(transformInput11);
            assertTrue(originalResult >= transformResult11);
            logKill("MR11", false);
        } catch (AssertionError e) {
            logKill("MR11", true);
            throw e;
        }

        // MR12: 所有元素取负
        try {
            Integer[] transformInput12 = MetamorphicTestGenerator1.applyMR12(originalInput);
            int transformResult12 = add_values.add_values_m(transformInput12);
            assertTrue(-originalResult == transformResult12);
            logKill("MR12", false);
        } catch (AssertionError e) {
            logKill("MR12", true);
            throw e;
        }

        // MR13: 微调增量
        try {
            Double[] transformInput13 = MetamorphicTestGenerator1.applyMR13(originalInput);
            Integer[] transformInput13_1 = new Integer[transformInput13.length];
            for (int i = 0; i < transformInput13.length; i++) {
                transformInput13_1[i] = transformInput13[i].intValue();
            }
            double transformResult13 = add_values.add_values_m(transformInput13_1);
            assertTrue(originalResult <= transformResult13);
            logKill("MR13", false);
        } catch (AssertionError e) {
            logKill("MR13", true);
            throw e;
        }

        // MR14: 移除最大值
        try {
            Integer[] transformInput14 = MetamorphicTestGenerator1.applyMR14(originalInput);
            int transformResult14 = add_values.add_values_m(transformInput14);
            assertTrue(originalResult >= transformResult14);
            logKill("MR14", false);
        } catch (AssertionError e) {
            logKill("MR14", true);
            throw e;
        }

        // MR16: 随机复制一个元素
//        try {
//            Integer[] transformInput16 = MetamorphicTestGenerator1.applyMR16(originalInput);
//            int transformResult16 = add_values.add_values_m(transformInput16);
//            assertTrue(true); // 不能准确预期，只执行
//            logKill("MR16", false);
//        } catch (AssertionError e) {
//            logKill("MR16", true);
//            throw e;
//        }

        // MR20: 最小值+极小值
        try {
            Double[] transformInput20 = MetamorphicTestGenerator1.applyMR20(originalInput);
            Integer[] transformInput20_1 = new Integer[transformInput20.length];
            for (int i = 0; i < transformInput20_1.length; i++) {
                transformInput20_1[i] = transformInput20[i].intValue();
            }
            double transformResult20 = add_values.add_values_m(transformInput20_1);
            assertTrue(originalResult <= transformResult20);
            logKill("MR20", false);
        } catch (AssertionError e) {
            logKill("MR20", true);
            throw e;
        }

        // MR22: 恒等变换
        try {
            Integer[] transformInput22 = MetamorphicTestGenerator1.applyMR22(originalInput);
            int transformResult22 = add_values.add_values_m(transformInput22);
            assertTrue(originalResult == transformResult22);
            logKill("MR22", false);
        } catch (AssertionError e) {
            logKill("MR22", true);
            throw e;
        }
    }


    //----------------------------------------------------------

//        //OR1:和应该保持不变
//        assertTrue(originalResult == transformResult1);
    //OR2:源输出和加上n*3等于后续输入
//        assertTrue(originalResult + originalInput.length * 3 == transformResult2);
    //OR3_1:和应该保持不变
//        assertTrue(originalResult == transformResult3_1);
//        //OR3_2:和应该保持不变
//        assertTrue(originalResult + 1 == transformResult3_2);
//        //OR4:和应该减少或保持不变
//        assertTrue(originalResult >= transformResult4);
//        //OR5:源输出和乘以2等于后续输出
//        assertTrue(originalResult * 2 == transformResult5);
//        //OR6:源输出和等于后续输出和
//        assertTrue(originalResult == transformResult6);
//        //OR7_1:源输出和等于后续输出和
//        assertTrue(originalResult == transformResult7_1);
//        //OR7_2:源输出和等于后续输出和
//        assertTrue(originalResult == transformResult7_2);
//        //OR8:源输出*2等于后续输出
//        assertTrue(originalResult * 2 == transformResult8);
//        //OR9:源输出*3等于后续输出
//        assertTrue(originalResult * 3 == transformResult9);
//        //OR10:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult10);
//        //OR11:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult11);
//        //OR12:源输出负数等于后续输出
//        assertTrue(-originalResult == transformResult12);
//        //OR13:源输出小于等于后续输出
//        assertTrue(originalResult <= transformResult13);
//        //OR14:源输出大于等于后续输出
//        assertTrue(originalResult >= transformResult14);
//        //OR15:源输出大于等于后续输出
////        assertTrue(originalResult >= transformResult15);
//        //OR16:源输出小于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
////        assertTrue(originalResult <= transformResult16);
//        //OR19:源输出小于等于后续输出（数组中存在负数，可能复制了一个负数，和可能变大也可能变小）
////        assertTrue(originalResult <= transformResult16);
//        //OR20:源输出小于等于后续输出
//        //assertTrue(originalResult <= transformResult20);
//        //OR22:源输出等于后续输出
//        assertTrue(originalResult == transformResult22);


    // logKill用来写MR杀死状态日志
    private static final String LOG_FILE = "C:\\Users\\Administrator\\Desktop\\kill result2.txt";

    private static void logKill(String mr, boolean killed) {
        try {
            File file = new File(LOG_FILE);
            file.getParentFile().mkdirs(); // 创建父目录（如果不存在）

            try (FileWriter fw = new FileWriter(file, true);
                 BufferedWriter bw = new BufferedWriter(fw);
                 PrintWriter out = new PrintWriter(bw, true)) {

                out.println("[MR: " + mr + "] EXECUTED");
                out.println("[" + mr + "] " + (killed ? "KILLED" : "SURVIVED"));
                //out.flush();没有用啊
            }
        } catch (IOException e) {
            System.err.println("日志写入失败：" + e.getMessage());
            e.printStackTrace();
        }
    }


    @Test
    public void testCase1() {
        Integer[] originalInput = {1, 3, 2, 6, 9};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase2() {
        Integer[] originalInput = {2, 1, 4, 4, 2};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase3() {
        Integer[] originalInput = {4, -2, 4, 6, 2};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase4() {
        Integer[] originalInput = {9, 2, 1, 5, 3, 2};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase5() {
        Integer[] originalInput = {-1, 9, 1, -3, -3};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase6() {
        Integer[] originalInput = {8, 3, 2, 6, 2, 3};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase7() {
        Integer[] originalInput = {1, 2, 3, 4, -5, 6};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase8() {
        Integer[] originalInput = {1, 2, 4, 2, 7, 5};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase9() {
        Integer[] originalInput = {1, 1, 2, 4, 1, 2};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }

    @Test
    public void testCase10() {
        Integer[] originalInput = {-2, 3, 1, 4, 7};
        int originalResult = add_values.add_values_m(originalInput);
        applyMR_Assert(originalInput, originalResult);
    }
}