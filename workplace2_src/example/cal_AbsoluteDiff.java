package example;

public class cal_AbsoluteDiff {//计算数组中的绝对值，返回新数组

    public static double[] cal_AbsoluteDiff_m(Double[] z) {
        if (z == null) {
            return null;
        }
        if (z.length == 0) {
            return null;
        }
        final double[] zAbs = new double[z.length];
        for (int i = 0; i < z.length; ++i) {
            zAbs[i] = Math.abs(z[i]);
        }
        return zAbs;
    }
}