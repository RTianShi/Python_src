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
def x_reverse__mutmut_orig(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_1(a):
    r = None
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_2(a):
    r = len(a)
    cnt = None

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_3(a):
    r = len(a)
    cnt = 1

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_4(a):
    r = len(a)
    cnt = 0

    for i in range(None, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_5(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, None, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_6(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, None):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_7(a):
    r = len(a)
    cnt = 0

    for i in range(-1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_8(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_9(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, ):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_10(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) + 1, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_11(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 2, -1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_12(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, +1, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_13(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -2, -1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_14(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, +1):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_15(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -2):
        r[cnt] = a[i]
        cnt += 1

    return r
def x_reverse__mutmut_16(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = None
        cnt += 1

    return r
def x_reverse__mutmut_17(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt = 1

    return r
def x_reverse__mutmut_18(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt -= 1

    return r
def x_reverse__mutmut_19(a):
    r = len(a)
    cnt = 0

    for i in range(len(a) - 1, -1, -1):
        r[cnt] = a[i]
        cnt += 2

    return r

x_reverse__mutmut_mutants : ClassVar[MutantDict] = {
'x_reverse__mutmut_1': x_reverse__mutmut_1, 
    'x_reverse__mutmut_2': x_reverse__mutmut_2, 
    'x_reverse__mutmut_3': x_reverse__mutmut_3, 
    'x_reverse__mutmut_4': x_reverse__mutmut_4, 
    'x_reverse__mutmut_5': x_reverse__mutmut_5, 
    'x_reverse__mutmut_6': x_reverse__mutmut_6, 
    'x_reverse__mutmut_7': x_reverse__mutmut_7, 
    'x_reverse__mutmut_8': x_reverse__mutmut_8, 
    'x_reverse__mutmut_9': x_reverse__mutmut_9, 
    'x_reverse__mutmut_10': x_reverse__mutmut_10, 
    'x_reverse__mutmut_11': x_reverse__mutmut_11, 
    'x_reverse__mutmut_12': x_reverse__mutmut_12, 
    'x_reverse__mutmut_13': x_reverse__mutmut_13, 
    'x_reverse__mutmut_14': x_reverse__mutmut_14, 
    'x_reverse__mutmut_15': x_reverse__mutmut_15, 
    'x_reverse__mutmut_16': x_reverse__mutmut_16, 
    'x_reverse__mutmut_17': x_reverse__mutmut_17, 
    'x_reverse__mutmut_18': x_reverse__mutmut_18, 
    'x_reverse__mutmut_19': x_reverse__mutmut_19
}

def reverse(*args, **kwargs):
    result = _mutmut_trampoline(x_reverse__mutmut_orig, x_reverse__mutmut_mutants, args, kwargs)
    return result 

reverse.__signature__ = _mutmut_signature(x_reverse__mutmut_orig)
x_reverse__mutmut_orig.__name__ = 'x_reverse'
