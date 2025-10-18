import static org.junit.Assert.assertTrue;

public class aa {
    private void applyMR_Assert(Double[] originalInput1_1, Double[] originalInput1_2, boolean originalResult) {
        //MR1:数组元置换（打乱顺序）
        Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
        Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
        boolean transformResult1 = check_eq_tolerance.check_eq_tolerance_m(transformInput1_1, transformInput1_2, 1e-9);
        //MR2:数组元素常数加法
        Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
        Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
        boolean transformResult2 = check_eq_tolerance.check_eq_tolerance_m(transformInput2_1, transformInput2_2, 1e-9);


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

        //OR22:源输出等于后续输出
        assertTrue(originalResult == transformResult22);


    }

    private void applyMR_Assert1(Double[] originalInput1_1, Double[] originalInput1_2, boolean originalResult) {


        System.out.println("\n"); // 输出 mutant 名称 + 换行
        boolean hasFailed = false;
        final double delta = 1e-9; // Delta for floating-point comparison

        // MR1:数组元置换（打乱顺序）
        try {
            Double[] transformInput1_1 = MetamorphicTestGenerator4.applyMR1(originalInput1_1);
            Double[] transformInput1_2 = MetamorphicTestGenerator4.applyMR1(originalInput1_2);
            boolean transformResult1 = check_eq_tolerance.check_eq_tolerance_m(transformInput1_1, transformInput1_2, delta);
            // OR1:和应该保持不变
            // assertTrue(originalResult == transformResult1);
        } catch (Throwable e) {
            System.out.println("MR1 killed mutant");
            hasFailed = true;
        }

        // MR2:数组元素常数加法
        try {
            Double[] transformInput2_1 = MetamorphicTestGenerator4.applyMR2(originalInput1_1);
            Double[] transformInput2_2 = MetamorphicTestGenerator4.applyMR2(originalInput1_2);
            boolean transformResult2 = check_eq_tolerance.check_eq_tolerance_m(transformInput2_1, transformInput2_2, delta);
            // OR2:源输出等于后续输出
            assertTrue("MR2失败", originalResult == transformResult2);
        } catch (Throwable e) {
            System.out.println("MR2 killed mutant");
            hasFailed = true;
        }


        // MR22:应用恒等变换
        try {
            Double[] transformInput22_1 = MetamorphicTestGenerator4.applyMR22(originalInput1_1);
            Double[] transformInput22_2 = MetamorphicTestGenerator4.applyMR22(originalInput1_2);
            boolean transformResult22 = check_eq_tolerance.check_eq_tolerance_m(transformInput22_1, transformInput22_2, delta);
            // OR22:源输出等于后续输出
            assertTrue("MR22失败", originalResult == transformResult22);
        } catch (Throwable e) {
            System.out.println("MR22 killed mutant");
            hasFailed = true;
        }

        // 最后统一判断是否有任何 MR 失败
        if (hasFailed) {
            throw new AssertionError("Some MR(s) failed, mutant killed.");
        }
    }


}
