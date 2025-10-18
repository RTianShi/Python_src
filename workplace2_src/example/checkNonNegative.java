package example;

public class checkNonNegative {//检查数组中是不是没有负数

    public static boolean checkNonNegative_m(final double[] in) {
        for (int i = 0; i < in.length; i++) {
            if (in[i] < 0) {
                return false;
            }
        }
        return true;
    }
}