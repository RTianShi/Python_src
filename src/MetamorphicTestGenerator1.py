import random
import math
from typing import List

class MetamorphicTestGenerator1:

    # MR1: 数组元置换（打乱顺序）
    @staticmethod
    def applyMR1(input_list: List[int]) -> List[int]:
        transformed = input_list.copy()
        random.shuffle(transformed)
        return transformed

    # MR2: 数组元素常数加法
    @staticmethod
    def applyMR2(input_list: List[int]) -> List[int]:
        return [x + 3 for x in input_list]

    # MR3_1: 加入单位元不变性（加法的单位元0）
    @staticmethod
    def applyMR3_1(input_list: List[int]) -> List[int]:
        return input_list + [0]

    # MR3_2: 加入单位元不变性（乘法的单位元1）
    @staticmethod
    def applyMR3_2(input_list: List[int]) -> List[int]:
        return input_list + [1]

    # MR4: 数组元素取倒数
    @staticmethod
    def applyMR4(input_list: List[int]) -> List[float]:
        return [0.0 if x == 0 else 1.0 / x for x in input_list]

    # MR5: 数组缩放变换
    @staticmethod
    def applyMR5(input_list: List[int], constant: int) -> List[int]:
        return [x * constant for x in input_list]

    # MR6: 数组反转变换
    @staticmethod
    def applyMR6(input_list: List[int]) -> List[int]:
        return list(reversed(input_list))

    # MR7_1: 中立操作的恒等变换（所有元素乘以1）
    @staticmethod
    def applyMR7_1(input_list: List[int]) -> List[int]:
        return [x * 1 for x in input_list]

    # MR7_2: 中立操作的恒等变换（所有元素加上0）
    @staticmethod
    def applyMR7_2(input_list: List[int]) -> List[int]:
        return [x + 0 for x in input_list]

    # MR8: 重复输入数组
    @staticmethod
    def applyMR8(input_list: List[int]) -> List[int]:
        return input_list + input_list

    # MR9: 复合转换一致性
    @staticmethod
    def applyMR9(input_list: List[int], constant: int) -> List[int]:
        transformed = [x * constant for x in input_list]
        return sorted(transformed)

    # MR10: 单调性检验
    @staticmethod
    def applyMR10(input_list: List[int]) -> List[int]:
        transformed = input_list.copy()
        count = 0
        for i in range(len(transformed)):
            transformed[i] = transformed[i] + count
            count += 1
        return transformed

    # MR11: 边界值替换(把最大值替换成0)
    @staticmethod
    def applyMR11(input_list: List[int]) -> List[int]:
        transformed = input_list.copy()
        max_index = transformed.index(max(transformed))
        transformed[max_index] = 0
        return transformed

    # MR12: 数值取反变换
    @staticmethod
    def applyMR12(input_list: List[int]) -> List[int]:
        return [-x for x in input_list]

    # MR13: 微小增量调整
    @staticmethod
    def applyMR13(input_list: List[int]) -> List[float]:
        return [x + 1e-10 for x in input_list]

    # MR14: 移除元素的效果（移除最大值）
    @staticmethod
    def applyMR14(input_list: List[int]) -> List[int]:
        max_value = max(input_list)
        return [x for x in input_list if x != max_value]

    # MR15: 类三角函数的周期性
    @staticmethod
    def applyMR15(input_list: List[int]) -> List[float]:
        return [math.pi - x for x in input_list]

    # MR16: 重复值稳健性(复制输入中的一个元素)
    @staticmethod
    def applyMR16(input_list: List[int]) -> List[int]:
        return input_list + [input_list[0]]

    # MR19: 输入重复（元素复制）将元素a重复多次插入序列中
    @staticmethod
    def applyMR19(input_list: List[int], count: int) -> List[int]:
        return input_list + [input_list[0]] * count

    # MR20: 边界值灵敏度（给最小值增加一个极小值）
    @staticmethod
    def applyMR20(input_list: List[int]) -> List[float]:
        min_value = min(input_list)
        return [x + 1e-10 if x == min_value else float(x) for x in input_list]

    # MR22: 应用恒等变换
    @staticmethod
    def applyMR22(input_list: List[int]) -> List[int]:
        return input_list.copy()
