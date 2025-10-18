package example;

public class checkPositive {//检查数组中是不是只有正数

    public static boolean checkPositive_m(final double[] in) {
        for (int i = 0; i < in.length; i++) {
            if (in[i] <= 0) {
                return false;
            }
        }
        return true;
    }
}