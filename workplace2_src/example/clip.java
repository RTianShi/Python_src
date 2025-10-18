package example;

public class clip {//截断数组，规定最小值和最大值

    public static int[] clip_m(Integer[] a, Integer lowerLim, Integer upperLim) {
        int[] r = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            if (a[i] < lowerLim) {
                r[i] = lowerLim;
            } else {
                if (a[i] > upperLim) {
                    r[i] = upperLim;
                } else {
                    r[i] = a[i];
                }
            }
        }
        return r;
    }
}