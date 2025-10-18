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
def x_find_max1__mutmut_orig(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_1(a):

    max1 = None

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_2(a):

    max1 = a[0] - a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_3(a):

    max1 = a[1] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_4(a):

    max1 = a[0] + a[2]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_5(a):

    max1 = a[0] + a[1]

    for i in range(None, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_6(a):

    max1 = a[0] + a[1]

    for i in range(0, None):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_7(a):

    max1 = a[0] + a[1]

    for i in range(len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_8(a):

    max1 = a[0] + a[1]

    for i in range(0, ):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_9(a):

    max1 = a[0] + a[1]

    for i in range(1, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_10(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) + 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_11(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 2):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_12(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] - a[i + 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_13(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i - 0] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_14(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 1] > max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_15(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] >= max1:
            max1 = a[i] + a[i + 1]

    return max1
def x_find_max1__mutmut_16(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = None

    return max1
def x_find_max1__mutmut_17(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] - a[i + 1]

    return max1
def x_find_max1__mutmut_18(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i - 1]

    return max1
def x_find_max1__mutmut_19(a):

    max1 = a[0] + a[1]

    for i in range(0, len(max1) - 1):
        if a[i] + a[i + 0] > max1:
            max1 = a[i] + a[i + 2]

    return max1

x_find_max1__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_max1__mutmut_1': x_find_max1__mutmut_1, 
    'x_find_max1__mutmut_2': x_find_max1__mutmut_2, 
    'x_find_max1__mutmut_3': x_find_max1__mutmut_3, 
    'x_find_max1__mutmut_4': x_find_max1__mutmut_4, 
    'x_find_max1__mutmut_5': x_find_max1__mutmut_5, 
    'x_find_max1__mutmut_6': x_find_max1__mutmut_6, 
    'x_find_max1__mutmut_7': x_find_max1__mutmut_7, 
    'x_find_max1__mutmut_8': x_find_max1__mutmut_8, 
    'x_find_max1__mutmut_9': x_find_max1__mutmut_9, 
    'x_find_max1__mutmut_10': x_find_max1__mutmut_10, 
    'x_find_max1__mutmut_11': x_find_max1__mutmut_11, 
    'x_find_max1__mutmut_12': x_find_max1__mutmut_12, 
    'x_find_max1__mutmut_13': x_find_max1__mutmut_13, 
    'x_find_max1__mutmut_14': x_find_max1__mutmut_14, 
    'x_find_max1__mutmut_15': x_find_max1__mutmut_15, 
    'x_find_max1__mutmut_16': x_find_max1__mutmut_16, 
    'x_find_max1__mutmut_17': x_find_max1__mutmut_17, 
    'x_find_max1__mutmut_18': x_find_max1__mutmut_18, 
    'x_find_max1__mutmut_19': x_find_max1__mutmut_19
}

def find_max1(*args, **kwargs):
    result = _mutmut_trampoline(x_find_max1__mutmut_orig, x_find_max1__mutmut_mutants, args, kwargs)
    return result 

find_max1.__signature__ = _mutmut_signature(x_find_max1__mutmut_orig)
x_find_max1__mutmut_orig.__name__ = 'x_find_max1'
