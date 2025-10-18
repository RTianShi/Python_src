import math
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x_kurtosis__mutmut_orig(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_1(data):
    suma = None
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_2(data):
    suma = 1
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_3(data):
    suma = 0
    sumPD = None
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_4(data):
    suma = 0
    sumPD = 1
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_5(data):
    suma = 0
    sumPD = 0
    sumSq = None

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_6(data):
    suma = 0
    sumPD = 0
    sumSq = 1

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_7(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(None, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_8(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, None):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_9(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_10(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, ):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_11(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(1, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_12(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma = data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_13(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma -= data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_14(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq = data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_15(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq -= data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_16(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] / data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_17(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = None

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_18(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma * len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_19(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = None

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_20(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt(None)

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_21(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) * len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_22(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq + mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_23(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean / suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_24(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(None, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_25(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, None):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_26(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_27(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, ):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_28(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(1, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_29(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD = math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_30(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD -= math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_31(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(None, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_32(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, None)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_33(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_34(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, )

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_35(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] + mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_36(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 5)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_37(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = None

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_38(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD * len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_39(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 - moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_40(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return +3 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_41(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -4 + moment4 / (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_42(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 * (standarDeviation * standarDeviation * standarDeviation * standarDeviation)


def x_kurtosis__mutmut_43(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation * standarDeviation / standarDeviation)


def x_kurtosis__mutmut_44(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation * standarDeviation / standarDeviation * standarDeviation)


def x_kurtosis__mutmut_45(data):
    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)

    standarDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment4 = sumPD / len(data)

    return -3 + moment4 / (standarDeviation / standarDeviation * standarDeviation * standarDeviation)

x_kurtosis__mutmut_mutants : ClassVar[MutantDict] = {
'x_kurtosis__mutmut_1': x_kurtosis__mutmut_1, 
    'x_kurtosis__mutmut_2': x_kurtosis__mutmut_2, 
    'x_kurtosis__mutmut_3': x_kurtosis__mutmut_3, 
    'x_kurtosis__mutmut_4': x_kurtosis__mutmut_4, 
    'x_kurtosis__mutmut_5': x_kurtosis__mutmut_5, 
    'x_kurtosis__mutmut_6': x_kurtosis__mutmut_6, 
    'x_kurtosis__mutmut_7': x_kurtosis__mutmut_7, 
    'x_kurtosis__mutmut_8': x_kurtosis__mutmut_8, 
    'x_kurtosis__mutmut_9': x_kurtosis__mutmut_9, 
    'x_kurtosis__mutmut_10': x_kurtosis__mutmut_10, 
    'x_kurtosis__mutmut_11': x_kurtosis__mutmut_11, 
    'x_kurtosis__mutmut_12': x_kurtosis__mutmut_12, 
    'x_kurtosis__mutmut_13': x_kurtosis__mutmut_13, 
    'x_kurtosis__mutmut_14': x_kurtosis__mutmut_14, 
    'x_kurtosis__mutmut_15': x_kurtosis__mutmut_15, 
    'x_kurtosis__mutmut_16': x_kurtosis__mutmut_16, 
    'x_kurtosis__mutmut_17': x_kurtosis__mutmut_17, 
    'x_kurtosis__mutmut_18': x_kurtosis__mutmut_18, 
    'x_kurtosis__mutmut_19': x_kurtosis__mutmut_19, 
    'x_kurtosis__mutmut_20': x_kurtosis__mutmut_20, 
    'x_kurtosis__mutmut_21': x_kurtosis__mutmut_21, 
    'x_kurtosis__mutmut_22': x_kurtosis__mutmut_22, 
    'x_kurtosis__mutmut_23': x_kurtosis__mutmut_23, 
    'x_kurtosis__mutmut_24': x_kurtosis__mutmut_24, 
    'x_kurtosis__mutmut_25': x_kurtosis__mutmut_25, 
    'x_kurtosis__mutmut_26': x_kurtosis__mutmut_26, 
    'x_kurtosis__mutmut_27': x_kurtosis__mutmut_27, 
    'x_kurtosis__mutmut_28': x_kurtosis__mutmut_28, 
    'x_kurtosis__mutmut_29': x_kurtosis__mutmut_29, 
    'x_kurtosis__mutmut_30': x_kurtosis__mutmut_30, 
    'x_kurtosis__mutmut_31': x_kurtosis__mutmut_31, 
    'x_kurtosis__mutmut_32': x_kurtosis__mutmut_32, 
    'x_kurtosis__mutmut_33': x_kurtosis__mutmut_33, 
    'x_kurtosis__mutmut_34': x_kurtosis__mutmut_34, 
    'x_kurtosis__mutmut_35': x_kurtosis__mutmut_35, 
    'x_kurtosis__mutmut_36': x_kurtosis__mutmut_36, 
    'x_kurtosis__mutmut_37': x_kurtosis__mutmut_37, 
    'x_kurtosis__mutmut_38': x_kurtosis__mutmut_38, 
    'x_kurtosis__mutmut_39': x_kurtosis__mutmut_39, 
    'x_kurtosis__mutmut_40': x_kurtosis__mutmut_40, 
    'x_kurtosis__mutmut_41': x_kurtosis__mutmut_41, 
    'x_kurtosis__mutmut_42': x_kurtosis__mutmut_42, 
    'x_kurtosis__mutmut_43': x_kurtosis__mutmut_43, 
    'x_kurtosis__mutmut_44': x_kurtosis__mutmut_44, 
    'x_kurtosis__mutmut_45': x_kurtosis__mutmut_45
}

def kurtosis(*args, **kwargs):
    result = _mutmut_trampoline(x_kurtosis__mutmut_orig, x_kurtosis__mutmut_mutants, args, kwargs)
    return result 

kurtosis.__signature__ = _mutmut_signature(x_kurtosis__mutmut_orig)
x_kurtosis__mutmut_orig.__name__ = 'x_kurtosis'
