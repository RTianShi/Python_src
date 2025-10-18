package example;

public class s_add {//将两个整数数组 array1 和 array2 进行按元素相加

    public static void s_add_m(int[] array1, int[] array2) {
        for (int index = 0; index < array1.length; index++) {
            array1[index] += array2[index];
        }
    }
}
