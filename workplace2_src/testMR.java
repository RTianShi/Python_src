import java.util.Arrays;

public class testMR {
    public static Double[] applyMR2(Double[] input) {
        Double[] transformed = Arrays.copyOf(input, input.length + 1);
        transformed[transformed.length - 1] = 0.0;
        return transformed;
    }

    public static void main(String[] args) {
        Double[] input = {3.0, 4.0, 5.0};
        Double[] result = applyMR2(input);
        System.out.println("转换前的数组应该是：" + Arrays.toString(input));
        System.out.println("转换后的数组应该是：" + Arrays.toString(result));
    }

}
