import example.sampleKurtosis;
import example.sampleSkew;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class sampleSkewTest {

    private void applyMR_Assert(Integer size, Double moment3, double sampleVariance, double originalResult) {

        //IR1
        Integer size_1 = size + 6;
        Double moment3_1 = moment3 + 6.0;
        double sampleVariance_1 = sampleVariance + 6.0;
        double transformResult1 = sampleKurtosis.sampleKurtosis_m(size_1,moment3_1,sampleVariance_1);

        //IR3
        double sampleVariance_3 = (double)size;
        Double moment3_3 = moment3;
        Integer size_3 = (int)sampleVariance;
        double transformResult3 = sampleKurtosis.sampleKurtosis_m(size_3,moment3_3,sampleVariance_3);



        // Assertions
        double delta = 1e-10; // Delta for floating-point comparison

        // OR1: The sum should increase or remain the same
        assertTrue(transformResult1 >= originalResult);

        // OR3: The sum should remain unchanged
        assertEquals(originalResult, transformResult3, delta);


    }

    @Test
    public void testSampleSkew1() {
        Integer size = 11;
        Double moment3 = 3.5;
        double sampleVariance = 4.5;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew2() {
        Integer size = 8;  // Adjusted to a positive value
        Double moment3 = 4.0;  // Adjusted to a realistic positive value
        double sampleVariance = 1.8;  // Adjusted variance
        double originalResult = sampleSkew.sampleSkew_m(size, moment3, sampleVariance);
        applyMR_Assert(size, moment3, sampleVariance, originalResult);
    }

    @Test
    public void testSampleSkew3() {
        Integer size = 12;  // Non-zero and positive for valid skew calculation
        Double moment3 = 6.5;
        double sampleVariance = 2.1;  // Adjusted to a small positive value
        double originalResult = sampleSkew.sampleSkew_m(size, moment3, sampleVariance);
        applyMR_Assert(size, moment3, sampleVariance, originalResult);
    }

    @Test
    public void testSampleSkew4() {
        Integer size = 1;
        Double moment3 = 3.3;
        double sampleVariance = 3.6;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew5() {
        Integer size = 2;
        Double moment3 = -1.3;
        double sampleVariance = -1.0;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew6() {
        Integer size = -5;
        Double moment3 = -1.0;
        double sampleVariance = -2.5;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew7() {
        Integer size = 6;
        Double moment3 = 0.0;
        double sampleVariance = 1.6;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew8() {
        Integer size = 5;
        Double moment3 = 5.5;
        double sampleVariance = 5.5;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew9() {
        Integer size = 10;
        Double moment3 = 80.66;
        double sampleVariance = -90.15;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }

    @Test
    public void testSampleSkew10() {
        Integer size = 5;
        Double moment3 = 11.0;
        double sampleVariance = 12.0;
        double originalResult = sampleSkew.sampleSkew_m(size,moment3,sampleVariance);
        applyMR_Assert(size,moment3,sampleVariance,originalResult);
    }
}