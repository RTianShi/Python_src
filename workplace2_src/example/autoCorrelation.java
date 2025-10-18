package example;

public class autoCorrelation {//计算给定数据序列 data 在指定 时间滞后（lag） 下的自相关系数。

    public static double autoCorrelation_m(Double[] data, Integer lag, Double mean, Double variance) {
        int N = data.length;
        double run = 0;
        for (int i = lag; i < N; ++i) {
            run += (data[i] - mean) * (data[i - lag] - mean);
        }
        return run / (N - lag) / variance;
    }
}