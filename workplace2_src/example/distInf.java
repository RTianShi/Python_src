package example;

public class distInf {//返回两个数组之之间差值的最大值

    public static double distInf_m(Double[] p1, Double[] p2) {
        double max = 0;
        for (int i = 0; i < p1.length; i++) {
            max = Math.max(max, Math.abs(p1[i] - p2[i]));
        }
        return max;
    }
}