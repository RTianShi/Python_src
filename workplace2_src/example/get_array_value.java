package example;

public class get_array_value {//从整数数组 a 中获取第 k 个元素,并且检查是否越界

    public static int get_array_value_m(Integer[] a, Integer k) {
        if (k - 1 >= a.length || k - 1 < 0) {
            return -100000;
        } else {
            return a[k - 1];
        }
    }
}