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
def x_covariance__mutmut_orig(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_1(elements1, elements2):
    size = None
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_2(elements1, elements2):
    size = len(elements1)
    sumx = None
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_3(elements1, elements2):
    size = len(elements1)
    sumx = elements1[1]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_4(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = None
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_5(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[1]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_6(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = None

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_7(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 1

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_8(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(None, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_9(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, None):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_10(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_11(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, ):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_12(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(1, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_13(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = None
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_14(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = None

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_15(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx = x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_16(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx -= x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_17(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy = (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_18(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy -= (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_19(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) / (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_20(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x + sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_21(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx * (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_22(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i - 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_23(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 2)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_24(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y + sumy / i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_25(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy * i)
        sumy += y

    return sxy / (size - 1)
def x_covariance__mutmut_26(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy = y

    return sxy / (size - 1)
def x_covariance__mutmut_27(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy -= y

    return sxy / (size - 1)
def x_covariance__mutmut_28(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy * (size - 1)
def x_covariance__mutmut_29(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size + 1)
def x_covariance__mutmut_30(elements1, elements2):
    size = len(elements1)
    sumx = elements1[0]
    sumy = elements2[0]
    sxy = 0

    for i in range(0, size):
        x = elements1[i]
        y = elements2[i]

        sumx += x
        sxy += (x - sumx / (i + 1)) * (y - sumy / i)
        sumy += y

    return sxy / (size - 2)

x_covariance__mutmut_mutants : ClassVar[MutantDict] = {
'x_covariance__mutmut_1': x_covariance__mutmut_1, 
    'x_covariance__mutmut_2': x_covariance__mutmut_2, 
    'x_covariance__mutmut_3': x_covariance__mutmut_3, 
    'x_covariance__mutmut_4': x_covariance__mutmut_4, 
    'x_covariance__mutmut_5': x_covariance__mutmut_5, 
    'x_covariance__mutmut_6': x_covariance__mutmut_6, 
    'x_covariance__mutmut_7': x_covariance__mutmut_7, 
    'x_covariance__mutmut_8': x_covariance__mutmut_8, 
    'x_covariance__mutmut_9': x_covariance__mutmut_9, 
    'x_covariance__mutmut_10': x_covariance__mutmut_10, 
    'x_covariance__mutmut_11': x_covariance__mutmut_11, 
    'x_covariance__mutmut_12': x_covariance__mutmut_12, 
    'x_covariance__mutmut_13': x_covariance__mutmut_13, 
    'x_covariance__mutmut_14': x_covariance__mutmut_14, 
    'x_covariance__mutmut_15': x_covariance__mutmut_15, 
    'x_covariance__mutmut_16': x_covariance__mutmut_16, 
    'x_covariance__mutmut_17': x_covariance__mutmut_17, 
    'x_covariance__mutmut_18': x_covariance__mutmut_18, 
    'x_covariance__mutmut_19': x_covariance__mutmut_19, 
    'x_covariance__mutmut_20': x_covariance__mutmut_20, 
    'x_covariance__mutmut_21': x_covariance__mutmut_21, 
    'x_covariance__mutmut_22': x_covariance__mutmut_22, 
    'x_covariance__mutmut_23': x_covariance__mutmut_23, 
    'x_covariance__mutmut_24': x_covariance__mutmut_24, 
    'x_covariance__mutmut_25': x_covariance__mutmut_25, 
    'x_covariance__mutmut_26': x_covariance__mutmut_26, 
    'x_covariance__mutmut_27': x_covariance__mutmut_27, 
    'x_covariance__mutmut_28': x_covariance__mutmut_28, 
    'x_covariance__mutmut_29': x_covariance__mutmut_29, 
    'x_covariance__mutmut_30': x_covariance__mutmut_30
}

def covariance(*args, **kwargs):
    result = _mutmut_trampoline(x_covariance__mutmut_orig, x_covariance__mutmut_mutants, args, kwargs)
    return result 

covariance.__signature__ = _mutmut_signature(x_covariance__mutmut_orig)
x_covariance__mutmut_orig.__name__ = 'x_covariance'
