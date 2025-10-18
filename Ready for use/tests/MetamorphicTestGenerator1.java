import java.util.Arrays;
import java.util.Collections;

public class MetamorphicTestGenerator1 {

    //    // MR1: Swap the first and last elements（交换第一个元素和最后一个元素）
//    public static Integer[] applyMR1(Integer[] input) {
//        Integer[] transformed = Arrays.copyOf(input, input.length);
//        int a = transformed[0];
//        transformed[0] = transformed[input.length - 1];
//        transformed[input.length - 1] = a;
//        return transformed;
//    }
//
//    //MR2: By moving all elements one position to the left(将元素向左移动一个位置)
//
//    public static Integer[] applyMR2(Integer[] input) {
//        Integer[] transformed = Arrays.copyOf(input, input.length);
//        int a = transformed[0];
//        for (int i = 0; i < input.length - 1; i++) {
//            transformed[i] = transformed[i + 1];
//        }
//        transformed[input.length - 1] = a;
//        return transformed;
//    }
//MR1:数组元置换（打乱顺序）
// MR2:数组元素常数加法
// MR3_1:加入单位元不变性（加法的单位元0）
// MR3_2:加入单位元不变性（乘法的单位元1）
// MR4:数组元素取倒数
// MR5:数组缩放变换
// MR6:数组反转变换
//MR7_1:中立操作的恒等变换（所有元素乘以1）
//MR7_2:中立操作的恒等变换（所有元素加上0）
//MR8:重复输入数组
//MR9:复合转换一致性
//MR10:单调性检验
//MR11:边界值替换(把最大值替换成0)
//MR12:数值取反变换
//MR13:微小增量调整
//MR14:移除元素的效果（移除最大值）
//MR15:类三角函数的周期性
//MR16:重复值稳健性(复制输入中的一个元素)
//MR19:输入重复（元素复制）将元素a重复多次插入序列中
//MR20:边界值灵敏度（给最小值增加一个极小值）
//MR22:应用恒等变换
//-------------------------------------------------------------------------
    //MR1:数组元置换（打乱顺序）
    public static Integer[] applyMR1(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        Collections.shuffle(Arrays.asList(transformed));
        return transformed;
    }

    // MR2:数组元素常数加法
    public static Integer[] applyMR2(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = transformed[i] + 3;
        }

        return transformed;
    }

    //MR3_1:加入单位元不变性（加法的单位元0）
    public static Integer[] applyMR3_1(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length + 1);
        transformed[transformed.length - 1] = 0;
        return transformed;
    }

    //MR3_2:加入单位元不变性（乘法的单位元1）
    public static Integer[] applyMR3_2(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length + 1);
        transformed[transformed.length - 1] = 1;
        return transformed;
    }

    //MR4:数组元素取倒数
    public static Double[] applyMR4(Integer[] input) {
        Double[] transformed = new Double[input.length];
        for (int i = 0; i < input.length; i++) {
            if (input[i] == 0) {
                transformed[i] = 0.0; // Avoid division by zero
            } else {
                transformed[i] = 1.0 / input[i];
            }
        }
        return transformed;
    }

    //MR5:数组缩放变换
    public static Integer[] applyMR5(Integer[] input, Integer constant) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] *= constant;
        }
        return transformed;
    }

    //MR6:数组反转变换
    public static Integer[] applyMR6(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        Collections.reverse(Arrays.asList(transformed));
        return transformed;
    }

    //MR7_1:中立操作的恒等变换（所有元素乘以1）
    public static Integer[] applyMR7_1(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = transformed[i] * 1;
        }
        return transformed;
    }

    //MR7_2:中立操作的恒等变换（所有元素加上0）
    public static Integer[] applyMR7_2(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = transformed[i] + 0;
        }
        return transformed;
    }

    //MR8:重复输入数组
    public static Integer[] applyMR8(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length * 2);
        for (int i = 0; i < transformed.length / 2; i++) {
            transformed[transformed.length / 2 + i] = transformed[i];
        }
        return transformed;
    }

    //MR9:复合转换一致性
    public static Integer[] applyMR9(Integer[] input, Integer constant) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] *= constant;
        }
        Arrays.sort(transformed);
        return transformed;
    }

    //MR10:单调性检验
    public static Integer[] applyMR10(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        int count = 0;
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = transformed[i] + count;
            count++;

        }
        return transformed;
    }

    //MR11:边界值替换(把最大值替换成0)
    public static Integer[] applyMR11(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        int maxIndex = 0;
        for (int i = 0; i < transformed.length; i++) {
            if (transformed[i] > transformed[maxIndex]) {
                maxIndex = i;
            }
        }
        transformed[maxIndex] = 0;
        return transformed;
    }

    //MR12:数值取反变换
    public static Integer[] applyMR12(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = -transformed[i];
        }
        return transformed;
    }

    //MR13:微小增量调整
    public static Double[] applyMR13(Integer[] input) {
        Double[] transformed = new Double[input.length];
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = input[i] + 1e-10;
        }
        return transformed;
    }

    //MR14:移除元素的效果（移除最大值）
    public static Integer[] applyMR14(Integer[] input) {
        int max = 0, count = 0, index = 0;
        for (int i = 0; i < input.length; i++) {
            if (max < input[i]) {
                max = input[i];
            }
        }
        for (int num : input) {
            if (num == max) {
                count++;
            }
        }
        Integer[] transformed = new Integer[input.length - count];
        for (int num : input) {
            if (num != max) {
                transformed[index] = num;
                index++;
            }
        }
        return transformed;
    }

    //MR15:类三角函数的周期性
    public static Double[] applyMR15(Integer[] input) {
        Double transformed[] = new Double[input.length];
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = Math.PI - input[i];
        }
        return transformed;
    }

    //MR16:重复值稳健性(复制输入中的一个元素)
    public static Integer[] applyMR16(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length + 1);
        transformed[input.length] = transformed[0];
        return transformed;
    }

    //MR19:输入重复（元素复制）将元素a重复多次插入序列中
    public static Integer[] applyMR19(Integer[] input, int count) {
        Integer[] transformed = Arrays.copyOf(input, input.length + count);
        for (int i = 0; i < count; i++) {
            transformed[input.length + i] = transformed[0];
        }
        return transformed;
    }

    //MR20:边界值灵敏度（给最小值增加一个极小值）
    public static Double[] applyMR20(Integer[] input) {
        Double[] transformed = new Double[input.length];
        double min = 1000.0;
        for (int i = 0; i < transformed.length; i++) {
            transformed[i] = input[i].doubleValue();
            if (transformed[i] < min) {
                min = transformed[i];
            }
        }
        for (int i = 0; i < transformed.length; i++) {
            if (min == transformed[i]) {
                transformed[i] = transformed[i] + 1e-10;
            }
        }

        return transformed;
    }

    //MR22:应用恒等变换
    public static Integer[] applyMR22(Integer[] input) {
        Integer[] transformed = Arrays.copyOf(input, input.length);
        return transformed;
    }


}