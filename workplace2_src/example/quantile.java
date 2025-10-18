package example;

public class quantile {//计算排序数组的分位数，phi介于0到1之间

    public static double quantile_m(Double[] sortedElements, Double phi) {
        int n = sortedElements.length;
        double index = phi * (n - 1);
        int lhs = (int) index;
        double delta = index - lhs;
        double result;
        if (n == 0) {
            return 0.0;
        }
        if (lhs == n - 1) {
            result = sortedElements[lhs];
        } else {
            result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1];
        }
        return result;
    }
}