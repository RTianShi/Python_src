package example;

public class find_max {//找到数组中最大值

    public static int find_max_m(Integer[] a) {
        int max = a[0];
        for (int i = 0; i < a.length; i++) {
            if (a[i] > max) {
                max = a[i];
            }
        }
        return max;
    }
}