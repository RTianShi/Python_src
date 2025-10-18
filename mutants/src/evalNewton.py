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
def x_evalNewton__mutmut_orig(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_1(a, c, z):

    n = None
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_2(a, c, z):

    n = len(c) + 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_3(a, c, z):

    n = len(c) - 2
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_4(a, c, z):

    n = len(c) - 1
    value = None

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_5(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(None, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_6(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, None, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_7(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, None):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_8(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(-1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_9(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_10(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, ):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_11(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n + 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_12(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 2, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_13(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, +1, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_14(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -2, -1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_15(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, +1):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_16(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -2):
        value = a[i] + (z - c[i]) * value

    return value
def x_evalNewton__mutmut_17(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = None

    return value
def x_evalNewton__mutmut_18(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] - (z - c[i]) * value

    return value
def x_evalNewton__mutmut_19(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) / value

    return value
def x_evalNewton__mutmut_20(a, c, z):

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z + c[i]) * value

    return value

x_evalNewton__mutmut_mutants : ClassVar[MutantDict] = {
'x_evalNewton__mutmut_1': x_evalNewton__mutmut_1, 
    'x_evalNewton__mutmut_2': x_evalNewton__mutmut_2, 
    'x_evalNewton__mutmut_3': x_evalNewton__mutmut_3, 
    'x_evalNewton__mutmut_4': x_evalNewton__mutmut_4, 
    'x_evalNewton__mutmut_5': x_evalNewton__mutmut_5, 
    'x_evalNewton__mutmut_6': x_evalNewton__mutmut_6, 
    'x_evalNewton__mutmut_7': x_evalNewton__mutmut_7, 
    'x_evalNewton__mutmut_8': x_evalNewton__mutmut_8, 
    'x_evalNewton__mutmut_9': x_evalNewton__mutmut_9, 
    'x_evalNewton__mutmut_10': x_evalNewton__mutmut_10, 
    'x_evalNewton__mutmut_11': x_evalNewton__mutmut_11, 
    'x_evalNewton__mutmut_12': x_evalNewton__mutmut_12, 
    'x_evalNewton__mutmut_13': x_evalNewton__mutmut_13, 
    'x_evalNewton__mutmut_14': x_evalNewton__mutmut_14, 
    'x_evalNewton__mutmut_15': x_evalNewton__mutmut_15, 
    'x_evalNewton__mutmut_16': x_evalNewton__mutmut_16, 
    'x_evalNewton__mutmut_17': x_evalNewton__mutmut_17, 
    'x_evalNewton__mutmut_18': x_evalNewton__mutmut_18, 
    'x_evalNewton__mutmut_19': x_evalNewton__mutmut_19, 
    'x_evalNewton__mutmut_20': x_evalNewton__mutmut_20
}

def evalNewton(*args, **kwargs):
    result = _mutmut_trampoline(x_evalNewton__mutmut_orig, x_evalNewton__mutmut_mutants, args, kwargs)
    return result 

evalNewton.__signature__ = _mutmut_signature(x_evalNewton__mutmut_orig)
x_evalNewton__mutmut_orig.__name__ = 'x_evalNewton'
