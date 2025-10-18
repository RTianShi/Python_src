package example;

public class insertion_sort {//插入排序算法，生序排序

    public static Integer[] insertion_sort_m(Integer[] array) {
        for (int i = 1; i < array.length; i++) {
            int j = i;
            int B = array[i];
            while (j > 0 && array[j - 1] > B) {
                array[j] = array[j - 1];
                j--;
            }
            array[j] = B;
        }
        return array;
    }
}