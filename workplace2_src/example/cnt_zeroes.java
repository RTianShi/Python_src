package example;

public class cnt_zeroes {//看数组中有几个等于0的数

    public static int cnt_zeroes_m(Integer[] a) {
        int cnt = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 0) {
                cnt++;
            }
        }
        return cnt;
    }
}