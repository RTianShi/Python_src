package example;

public class set_min_val {//最小值阈值处理，它会将数组中所有小于给定阈值 k 的值替换为 k

    public static Integer[] set_min_val_m(Integer[] a, Integer k) {
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] < k) {
                a[i] = k;
            }
        }
        return a;
    }
}