package example;

public class array_copy {//复制数组

    public static int[] array_copy_m(int[] a) {
        int i;
        int[] b = new int[a.length];
        for (i = 0; i < a.length; i++) {
            b[i] = a[i];
        }
        return b;
    }
}