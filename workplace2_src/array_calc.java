public class array_calc {//把数组缩小一定倍数

    public static int[] array_calc_m(int[] a, int k) {
        int i;
        int[] b = new int[a.length];
        for (i = 0; i < a.length; i++) {
            b[i] = a[i] / k;
        }
        return b;
    }
}