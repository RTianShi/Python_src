package example;

public class find_min {//求数组中的最小值

    public static int find_min_m(Integer[] a) {
        int min = a[0];
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] < min) {
                min = a[i];
            }
        }
        return min;
    }
}