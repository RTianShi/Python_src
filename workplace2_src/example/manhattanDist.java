package example;

public class manhattanDist {//计算曼哈顿距离，对应位置元素差的绝对值的和

    public static double manhattanDist_m(Integer[] a, Integer[] b) {
        int i;
        double sum = 0;
        for (i = 0; i < a.length; i++) {
            sum += Math.abs(a[i] - b[i]);
        }
        return sum;
    }
}