package example;

public class square {//返回每个数组的平方元素

    public static Double[] square_m(Double[] data) {
        for (int i = 0; i < data.length; i++) {
            data[i] = data[i] * data[i];
        }
        return data;
    }
}