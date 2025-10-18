import example.sampleKurtosis;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class sampleKurtosisTest {

    private void applyMR_Assert(Integer size, Double moment4, Double sampleVariance, double originalResult) {

        //IR1
        Integer size_1 = size + 2;
        Double moment4_1 = moment4 + 2.0;
        Double sampleVariance_1 = sampleVariance + 2.0;
        double transformResult1 = sampleKurtosis.sampleKurtosis_m(size_1,moment4_1,sampleVariance_1);

        //IR3
        Double sampleVariance_3 = (double)size;
        Double moment4_3 = moment4;
        Integer size_3 = sampleVariance.intValue();
        double transformResult3 = sampleKurtosis.sampleKurtosis_m(size_3,moment4_3,sampleVariance_3);

        //IR6
        Double size_6_1 = (double)( 1 / size);
        Integer size_6 = size_6_1.intValue();
        Double moment_6 = 1.0 / moment4;
        Double sampleVariance_6 = 1.0 / sampleVariance;
        double transformResult6 = sampleKurtosis.sampleKurtosis_m(size_6,moment_6,sampleVariance_6);


        // Assertions
        double delta = 1e-10; // Delta for floating-point comparison

        // OR1: The sum should increase or remain the same
        assertTrue(transformResult1 >= originalResult);

        // OR3: The sum should remain unchanged
        assertEquals(originalResult, transformResult3, delta);

        // OR6: The sum should decrease or remain the same
        assertTrue(transformResult6 <= originalResult);


    }

    @Test
    public void testSampleKurtosis1() {
        Integer size = 1;
        Double moment4 = 0.1;
        Double sampleVariance = 0.2;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);

    }

    @Test
    public void testSampleKurtosis2() {
        Integer size = 3;
        Double moment4 = 1.5;
        Double sampleVariance = 1.6;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis3() {
        Integer size = -3;
        Double moment4 = 4.52;
        Double sampleVariance = -0.8;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis4() {
        Integer size = 0;
        Double moment4 = 6.5;
        Double sampleVariance = -1.2;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis5() {
        Integer size = 1;
        Double moment4 = 3.3;
        Double sampleVariance = 3.6;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis6() {
        Integer size = 2;
        Double moment4 = -1.3;
        Double sampleVariance = -1.0;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis7() {
        Integer size = -5;
        Double moment4 = -1.0;
        Double sampleVariance = -2.5;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis8() {
        Integer size = 6;
        Double moment4 = 0.0;
        Double sampleVariance = 1.6;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis9() {
        Integer size = 5;
        Double moment4 = 5.5;
        Double sampleVariance = 5.5;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }

    @Test
    public void testSampleKurtosis10() {
        Integer size = 10;
        Double moment4 = 80.66;
        Double sampleVariance = -90.15;
        double originalResult = sampleKurtosis.sampleKurtosis_m(size,moment4,sampleVariance);
        applyMR_Assert(size,moment4,sampleVariance,originalResult);
    }
}