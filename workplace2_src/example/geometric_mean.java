package example;

public class geometric_mean {//计算数组的几何平均数，把数组元素相乘然后开n次方根

    public static double geometric_mean_m(Integer[] a) {
        long product = 1;
        for (int i = 0; i < a.length; i++) {
            product *= a[i];
        }
        return Math.pow(product, (double) 1 / a.length);
    }
}