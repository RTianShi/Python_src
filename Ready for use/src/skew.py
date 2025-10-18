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


def x_skew__mutmut_orig(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_1(data):

    suma = None
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_2(data):

    suma = 1
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_3(data):

    suma = 0
    sumPD = None
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_4(data):

    suma = 0
    sumPD = 1
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_5(data):

    suma = 0
    sumPD = 0
    sumSq = None

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_6(data):

    suma = 0
    sumPD = 0
    sumSq = 1

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_7(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(None, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_8(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, None):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_9(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_10(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, ):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_11(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(1, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_12(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma = data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_13(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma -= data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_14(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq = data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_15(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq -= data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_16(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] / data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_17(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = None
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_18(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma * len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_19(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = None

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_20(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt(None)

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_21(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) * len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_22(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq + mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_23(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean / suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_24(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(None, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_25(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, None):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_26(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_27(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, ):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_28(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(1, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_29(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD = math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_30(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD -= math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_31(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(None, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_32(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, None)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_33(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_34(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, )

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_35(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] + mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_36(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 4)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_37(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = None

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_38(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD * len(data)

    return moment3 / (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_39(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 * (standardDeviation * standardDeviation * standardDeviation)


def x_skew__mutmut_40(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation * standardDeviation / standardDeviation)


def x_skew__mutmut_41(data):

    suma = 0
    sumPD = 0
    sumSq = 0

    for i in range(0, len(data)):
        suma += data[i]
        sumSq += data[i] * data[i]

    mean = suma / len(data)
    standardDeviation = math.sqrt((sumSq - mean * suma) / len(data))

    for i in range(0, len(data)):
        sumPD += math.pow(data[i] - mean, 3)

    moment3 = sumPD / len(data)

    return moment3 / (standardDeviation / standardDeviation * standardDeviation)

x_skew__mutmut_mutants : ClassVar[MutantDict] = {
'x_skew__mutmut_1': x_skew__mutmut_1, 
    'x_skew__mutmut_2': x_skew__mutmut_2, 
    'x_skew__mutmut_3': x_skew__mutmut_3, 
    'x_skew__mutmut_4': x_skew__mutmut_4, 
    'x_skew__mutmut_5': x_skew__mutmut_5, 
    'x_skew__mutmut_6': x_skew__mutmut_6, 
    'x_skew__mutmut_7': x_skew__mutmut_7, 
    'x_skew__mutmut_8': x_skew__mutmut_8, 
    'x_skew__mutmut_9': x_skew__mutmut_9, 
    'x_skew__mutmut_10': x_skew__mutmut_10, 
    'x_skew__mutmut_11': x_skew__mutmut_11, 
    'x_skew__mutmut_12': x_skew__mutmut_12, 
    'x_skew__mutmut_13': x_skew__mutmut_13, 
    'x_skew__mutmut_14': x_skew__mutmut_14, 
    'x_skew__mutmut_15': x_skew__mutmut_15, 
    'x_skew__mutmut_16': x_skew__mutmut_16, 
    'x_skew__mutmut_17': x_skew__mutmut_17, 
    'x_skew__mutmut_18': x_skew__mutmut_18, 
    'x_skew__mutmut_19': x_skew__mutmut_19, 
    'x_skew__mutmut_20': x_skew__mutmut_20, 
    'x_skew__mutmut_21': x_skew__mutmut_21, 
    'x_skew__mutmut_22': x_skew__mutmut_22, 
    'x_skew__mutmut_23': x_skew__mutmut_23, 
    'x_skew__mutmut_24': x_skew__mutmut_24, 
    'x_skew__mutmut_25': x_skew__mutmut_25, 
    'x_skew__mutmut_26': x_skew__mutmut_26, 
    'x_skew__mutmut_27': x_skew__mutmut_27, 
    'x_skew__mutmut_28': x_skew__mutmut_28, 
    'x_skew__mutmut_29': x_skew__mutmut_29, 
    'x_skew__mutmut_30': x_skew__mutmut_30, 
    'x_skew__mutmut_31': x_skew__mutmut_31, 
    'x_skew__mutmut_32': x_skew__mutmut_32, 
    'x_skew__mutmut_33': x_skew__mutmut_33, 
    'x_skew__mutmut_34': x_skew__mutmut_34, 
    'x_skew__mutmut_35': x_skew__mutmut_35, 
    'x_skew__mutmut_36': x_skew__mutmut_36, 
    'x_skew__mutmut_37': x_skew__mutmut_37, 
    'x_skew__mutmut_38': x_skew__mutmut_38, 
    'x_skew__mutmut_39': x_skew__mutmut_39, 
    'x_skew__mutmut_40': x_skew__mutmut_40, 
    'x_skew__mutmut_41': x_skew__mutmut_41
}

def skew(*args, **kwargs):
    result = _mutmut_trampoline(x_skew__mutmut_orig, x_skew__mutmut_mutants, args, kwargs)
    return result 

skew.__signature__ = _mutmut_signature(x_skew__mutmut_orig)
x_skew__mutmut_orig.__name__ = 'x_skew'
