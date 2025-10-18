public class check_eq_tolerance {//检查两个数组是否在给定的误差范围内相等

    public static boolean check_eq_tolerance_m(Double[] a, Double[] b, Double tol) {
        if (a.length != b.length) {
            return false;
        }
        for (int i = 0; i < a.length; i++) {
            if (Math.abs(a[i] - b[i]) >= tol) {
                return false;
            }
        }
        return true;
    }
}