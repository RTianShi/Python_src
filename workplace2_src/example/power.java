package example;

public class power {//对数组中的每个元素进行幂运算

    public static Double[] power_m(Double[] data, Integer k) {
        for (int i = 0; i < data.length; i++) {
            data[i] = Math.pow(data[i], k);
        }
        return data;
    }
}