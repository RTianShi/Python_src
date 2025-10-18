package example;

public class euc_Dist {//计算欧几里得距离，衡量两个向量的空间距离（元素差平方后相加在开根号）

    public static double euc_Dist_m(double[] array1, double[] array2) {
        double Sum = 0.0;
        for (int i = 0; i < array1.length; i++) {
            Sum = Sum + Math.pow((array1[i] - array2[i]), 2.0);
        }
        return Math.sqrt(Sum);
    }

}
