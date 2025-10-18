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
def x_count_non_zeroes__mutmut_orig(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_1(a):
    cnt = None
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_2(a):
    cnt = 1
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_3(a):
    cnt = 0
    for i in range(None, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_4(a):
    cnt = 0
    for i in range(0, None):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_5(a):
    cnt = 0
    for i in range(len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_6(a):
    cnt = 0
    for i in range(0, ):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_7(a):
    cnt = 0
    for i in range(1, len(a)):
        if a[i] != 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_8(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] == 0:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_9(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 1:
            cnt += 1

    return cnt
def x_count_non_zeroes__mutmut_10(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt = 1

    return cnt
def x_count_non_zeroes__mutmut_11(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt -= 1

    return cnt
def x_count_non_zeroes__mutmut_12(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 2

    return cnt

x_count_non_zeroes__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_non_zeroes__mutmut_1': x_count_non_zeroes__mutmut_1, 
    'x_count_non_zeroes__mutmut_2': x_count_non_zeroes__mutmut_2, 
    'x_count_non_zeroes__mutmut_3': x_count_non_zeroes__mutmut_3, 
    'x_count_non_zeroes__mutmut_4': x_count_non_zeroes__mutmut_4, 
    'x_count_non_zeroes__mutmut_5': x_count_non_zeroes__mutmut_5, 
    'x_count_non_zeroes__mutmut_6': x_count_non_zeroes__mutmut_6, 
    'x_count_non_zeroes__mutmut_7': x_count_non_zeroes__mutmut_7, 
    'x_count_non_zeroes__mutmut_8': x_count_non_zeroes__mutmut_8, 
    'x_count_non_zeroes__mutmut_9': x_count_non_zeroes__mutmut_9, 
    'x_count_non_zeroes__mutmut_10': x_count_non_zeroes__mutmut_10, 
    'x_count_non_zeroes__mutmut_11': x_count_non_zeroes__mutmut_11, 
    'x_count_non_zeroes__mutmut_12': x_count_non_zeroes__mutmut_12
}

def count_non_zeroes(*args, **kwargs):
    result = _mutmut_trampoline(x_count_non_zeroes__mutmut_orig, x_count_non_zeroes__mutmut_mutants, args, kwargs)
    return result 

count_non_zeroes.__signature__ = _mutmut_signature(x_count_non_zeroes__mutmut_orig)
x_count_non_zeroes__mutmut_orig.__name__ = 'x_count_non_zeroes'
