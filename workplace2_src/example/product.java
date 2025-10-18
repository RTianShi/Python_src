package example;

public class product {//计算数组中所有元素的乘积

    public static double product_m(Double[] elements) {
        int size = elements.length;
        double product = 1;
        for (int i = size; --i >= 0; ) {
            product *= elements[i];
        }
        return product;
    }
}