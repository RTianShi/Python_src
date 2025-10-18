package example;

public class dot_product {//求数组点积（对应相乘相加）

    public static int dot_product_m(Integer[] a, Integer[] b) {
        int sum = 0;
        int i;
        for (i = 0; i < a.length; i++) {
            sum += a[i] * b[i];
        }
        return sum;
    }
}