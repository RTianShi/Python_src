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
def x_canberraDist__mutmut_orig(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_1(a, b):

    sum = None

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_2(a, b):

    sum = 1

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_3(a, b):

    sum = 0

    for i in range(None, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_4(a, b):

    sum = 0

    for i in range(0, None):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_5(a, b):

    sum = 0

    for i in range(len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_6(a, b):

    sum = 0

    for i in range(0, ):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_7(a, b):

    sum = 0

    for i in range(1, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_8(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = None
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_9(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(None)
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_10(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] + b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_11(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = None
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_12(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) - abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_13(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(None) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_14(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(None)
        if num == 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_15(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 and denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_16(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num != 0 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_17(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 1 or denom == 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_18(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom != 0:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_19(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 1:
            continue
        sum += num/denom

    return sum
def x_canberraDist__mutmut_20(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            break
        sum += num/denom

    return sum
def x_canberraDist__mutmut_21(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum = num/denom

    return sum
def x_canberraDist__mutmut_22(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum -= num/denom

    return sum
def x_canberraDist__mutmut_23(a, b):

    sum = 0

    for i in range(0, len(a)):
        num = abs(a[i] - b[i])
        denom = abs(a[i]) + abs(b[i])
        if num == 0 or denom == 0:
            continue
        sum += num * denom

    return sum

x_canberraDist__mutmut_mutants : ClassVar[MutantDict] = {
'x_canberraDist__mutmut_1': x_canberraDist__mutmut_1, 
    'x_canberraDist__mutmut_2': x_canberraDist__mutmut_2, 
    'x_canberraDist__mutmut_3': x_canberraDist__mutmut_3, 
    'x_canberraDist__mutmut_4': x_canberraDist__mutmut_4, 
    'x_canberraDist__mutmut_5': x_canberraDist__mutmut_5, 
    'x_canberraDist__mutmut_6': x_canberraDist__mutmut_6, 
    'x_canberraDist__mutmut_7': x_canberraDist__mutmut_7, 
    'x_canberraDist__mutmut_8': x_canberraDist__mutmut_8, 
    'x_canberraDist__mutmut_9': x_canberraDist__mutmut_9, 
    'x_canberraDist__mutmut_10': x_canberraDist__mutmut_10, 
    'x_canberraDist__mutmut_11': x_canberraDist__mutmut_11, 
    'x_canberraDist__mutmut_12': x_canberraDist__mutmut_12, 
    'x_canberraDist__mutmut_13': x_canberraDist__mutmut_13, 
    'x_canberraDist__mutmut_14': x_canberraDist__mutmut_14, 
    'x_canberraDist__mutmut_15': x_canberraDist__mutmut_15, 
    'x_canberraDist__mutmut_16': x_canberraDist__mutmut_16, 
    'x_canberraDist__mutmut_17': x_canberraDist__mutmut_17, 
    'x_canberraDist__mutmut_18': x_canberraDist__mutmut_18, 
    'x_canberraDist__mutmut_19': x_canberraDist__mutmut_19, 
    'x_canberraDist__mutmut_20': x_canberraDist__mutmut_20, 
    'x_canberraDist__mutmut_21': x_canberraDist__mutmut_21, 
    'x_canberraDist__mutmut_22': x_canberraDist__mutmut_22, 
    'x_canberraDist__mutmut_23': x_canberraDist__mutmut_23
}

def canberraDist(*args, **kwargs):
    result = _mutmut_trampoline(x_canberraDist__mutmut_orig, x_canberraDist__mutmut_mutants, args, kwargs)
    return result 

canberraDist.__signature__ = _mutmut_signature(x_canberraDist__mutmut_orig)
x_canberraDist__mutmut_orig.__name__ = 'x_canberraDist'
