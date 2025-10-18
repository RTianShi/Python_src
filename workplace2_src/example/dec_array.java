package example;

public class dec_array {//原数组基础上元素减去k值

    public static Integer[] dec_array_m(Integer[] a, Integer k) {
        int i;
        for (i = 0; i < a.length; i++) {
            a[i] -= k;
        }
        return a;
    }
}