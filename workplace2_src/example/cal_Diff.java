package example;

public class cal_Diff {//计算两个数组之间的逐元素差值

    public static double[] cal_Diff_m(final double[] x, final double[] y) {
        final double[] z = new double[x.length];
        for (int i = 0; i < x.length; ++i) {
            z[i] = y[i] - x[i++];
        }
        return z;
    }
}