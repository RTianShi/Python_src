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
def x_pooledMean__mutmut_orig(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_1(data1, data2):
    sum1 = None
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_2(data1, data2):
    sum1 = 1
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_3(data1, data2):
    sum1 = 0
    for i in range(None, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_4(data1, data2):
    sum1 = 0
    for i in range(0, None):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_5(data1, data2):
    sum1 = 0
    for i in range(len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_6(data1, data2):
    sum1 = 0
    for i in range(0, ):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_7(data1, data2):
    sum1 = 0
    for i in range(1, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_8(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 = data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_9(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 -= data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_10(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = None

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_11(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 * len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_12(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = None
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_13(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 1
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_14(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(None, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_15(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, None):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_16(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_17(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, ):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_18(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(1, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_19(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 = data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_20(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 -= data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_21(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = None

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_22(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 * len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_23(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) * (len(data1) + len(data2))
def x_pooledMean__mutmut_24(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 - len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_25(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) / mean1 + len(data2) * mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_26(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) / mean2) / (len(data1) + len(data2))
def x_pooledMean__mutmut_27(data1, data2):
    sum1 = 0
    for i in range(0, len(data1)):
        sum1 += data1[i]

    mean1 = sum1 / len(data1)

    sum2 = 0
    for i in range(0, len(data2)):
        sum2 += data2[i]

    mean2 = sum2 / len(data2)

    return (len(data1) * mean1 + len(data2) * mean2) / (len(data1) - len(data2))

x_pooledMean__mutmut_mutants : ClassVar[MutantDict] = {
'x_pooledMean__mutmut_1': x_pooledMean__mutmut_1, 
    'x_pooledMean__mutmut_2': x_pooledMean__mutmut_2, 
    'x_pooledMean__mutmut_3': x_pooledMean__mutmut_3, 
    'x_pooledMean__mutmut_4': x_pooledMean__mutmut_4, 
    'x_pooledMean__mutmut_5': x_pooledMean__mutmut_5, 
    'x_pooledMean__mutmut_6': x_pooledMean__mutmut_6, 
    'x_pooledMean__mutmut_7': x_pooledMean__mutmut_7, 
    'x_pooledMean__mutmut_8': x_pooledMean__mutmut_8, 
    'x_pooledMean__mutmut_9': x_pooledMean__mutmut_9, 
    'x_pooledMean__mutmut_10': x_pooledMean__mutmut_10, 
    'x_pooledMean__mutmut_11': x_pooledMean__mutmut_11, 
    'x_pooledMean__mutmut_12': x_pooledMean__mutmut_12, 
    'x_pooledMean__mutmut_13': x_pooledMean__mutmut_13, 
    'x_pooledMean__mutmut_14': x_pooledMean__mutmut_14, 
    'x_pooledMean__mutmut_15': x_pooledMean__mutmut_15, 
    'x_pooledMean__mutmut_16': x_pooledMean__mutmut_16, 
    'x_pooledMean__mutmut_17': x_pooledMean__mutmut_17, 
    'x_pooledMean__mutmut_18': x_pooledMean__mutmut_18, 
    'x_pooledMean__mutmut_19': x_pooledMean__mutmut_19, 
    'x_pooledMean__mutmut_20': x_pooledMean__mutmut_20, 
    'x_pooledMean__mutmut_21': x_pooledMean__mutmut_21, 
    'x_pooledMean__mutmut_22': x_pooledMean__mutmut_22, 
    'x_pooledMean__mutmut_23': x_pooledMean__mutmut_23, 
    'x_pooledMean__mutmut_24': x_pooledMean__mutmut_24, 
    'x_pooledMean__mutmut_25': x_pooledMean__mutmut_25, 
    'x_pooledMean__mutmut_26': x_pooledMean__mutmut_26, 
    'x_pooledMean__mutmut_27': x_pooledMean__mutmut_27
}

def pooledMean(*args, **kwargs):
    result = _mutmut_trampoline(x_pooledMean__mutmut_orig, x_pooledMean__mutmut_mutants, args, kwargs)
    return result 

pooledMean.__signature__ = _mutmut_signature(x_pooledMean__mutmut_orig)
x_pooledMean__mutmut_orig.__name__ = 'x_pooledMean'
