package example;

public class find_max2 {//计算所有相邻两元素的最大值

    public static int find_max2_m(Integer[] a) {
        int max = a[0] + a[1];
        for (int i = 0; i < a.length - 1; i++) {
            if (a[i] + a[i + 1] > max) {
                max = a[i] + a[i + 1];
            }
        }
        return max;
    }
}