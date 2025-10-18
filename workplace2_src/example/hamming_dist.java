package example;

public class hamming_dist {//判断两个数组中相同位置不同元素的个数

    public static int hamming_dist_m(Integer[] a, Integer[] b) {
        int cnt = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                cnt++;
            }
        }
        return cnt;
    }
}