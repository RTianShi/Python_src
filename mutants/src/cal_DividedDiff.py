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
def x_cal_DividedDiff__mutmut_orig(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_1(x, y):
    divdiff = None
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_2(x, y):
    divdiff = y.copy()
    n = None
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_3(x, y):
    divdiff = y.copy()
    n = len(x)
    a = None

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_4(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[1]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_5(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(None, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_6(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, None):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_7(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_8(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, ):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_9(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(2, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_10(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(None, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_11(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, None):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_12(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_13(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, ):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_14(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(1, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_15(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n + i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_16(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = None
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_17(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] + x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_18(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j - i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_19(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = None

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_20(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] + divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_21(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j - 1] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_22(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 2] - divdiff[j] / denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_23(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] * denominator

        a[i] = divdiff[0]
    return a
def x_cal_DividedDiff__mutmut_24(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = None
    return a
def x_cal_DividedDiff__mutmut_25(x, y):
    divdiff = y.copy()
    n = len(x)
    a = [divdiff[0]]

    for i in range(1, n):
        for j in range(0, n - i):
            denominator = x[j + i] - x[j]
            divdiff[j] = divdiff[j + 1] - divdiff[j] / denominator

        a[i] = divdiff[1]
    return a

x_cal_DividedDiff__mutmut_mutants : ClassVar[MutantDict] = {
'x_cal_DividedDiff__mutmut_1': x_cal_DividedDiff__mutmut_1, 
    'x_cal_DividedDiff__mutmut_2': x_cal_DividedDiff__mutmut_2, 
    'x_cal_DividedDiff__mutmut_3': x_cal_DividedDiff__mutmut_3, 
    'x_cal_DividedDiff__mutmut_4': x_cal_DividedDiff__mutmut_4, 
    'x_cal_DividedDiff__mutmut_5': x_cal_DividedDiff__mutmut_5, 
    'x_cal_DividedDiff__mutmut_6': x_cal_DividedDiff__mutmut_6, 
    'x_cal_DividedDiff__mutmut_7': x_cal_DividedDiff__mutmut_7, 
    'x_cal_DividedDiff__mutmut_8': x_cal_DividedDiff__mutmut_8, 
    'x_cal_DividedDiff__mutmut_9': x_cal_DividedDiff__mutmut_9, 
    'x_cal_DividedDiff__mutmut_10': x_cal_DividedDiff__mutmut_10, 
    'x_cal_DividedDiff__mutmut_11': x_cal_DividedDiff__mutmut_11, 
    'x_cal_DividedDiff__mutmut_12': x_cal_DividedDiff__mutmut_12, 
    'x_cal_DividedDiff__mutmut_13': x_cal_DividedDiff__mutmut_13, 
    'x_cal_DividedDiff__mutmut_14': x_cal_DividedDiff__mutmut_14, 
    'x_cal_DividedDiff__mutmut_15': x_cal_DividedDiff__mutmut_15, 
    'x_cal_DividedDiff__mutmut_16': x_cal_DividedDiff__mutmut_16, 
    'x_cal_DividedDiff__mutmut_17': x_cal_DividedDiff__mutmut_17, 
    'x_cal_DividedDiff__mutmut_18': x_cal_DividedDiff__mutmut_18, 
    'x_cal_DividedDiff__mutmut_19': x_cal_DividedDiff__mutmut_19, 
    'x_cal_DividedDiff__mutmut_20': x_cal_DividedDiff__mutmut_20, 
    'x_cal_DividedDiff__mutmut_21': x_cal_DividedDiff__mutmut_21, 
    'x_cal_DividedDiff__mutmut_22': x_cal_DividedDiff__mutmut_22, 
    'x_cal_DividedDiff__mutmut_23': x_cal_DividedDiff__mutmut_23, 
    'x_cal_DividedDiff__mutmut_24': x_cal_DividedDiff__mutmut_24, 
    'x_cal_DividedDiff__mutmut_25': x_cal_DividedDiff__mutmut_25
}

def cal_DividedDiff(*args, **kwargs):
    result = _mutmut_trampoline(x_cal_DividedDiff__mutmut_orig, x_cal_DividedDiff__mutmut_mutants, args, kwargs)
    return result 

cal_DividedDiff.__signature__ = _mutmut_signature(x_cal_DividedDiff__mutmut_orig)
x_cal_DividedDiff__mutmut_orig.__name__ = 'x_cal_DividedDiff'
