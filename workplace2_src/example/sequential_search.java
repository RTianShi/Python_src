package example;

public class sequential_search {//顺序搜索算法，返回元素索引

    public static int sequential_search_m(Integer[] a, Integer key) {
        int i;
        for (i = 0; i < a.length; i++) {
            if (a[i] == key) {
                return i;
            }
        }
        return -1;
    }
}