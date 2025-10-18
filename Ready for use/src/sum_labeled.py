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
def x_sum_labeled__mutmut_orig(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_1(a, i, j):

    if i < 0 or i >= len(a) or j < 0 and j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_2(a, i, j):

    if i < 0 or i >= len(a) and j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_3(a, i, j):

    if i < 0 and i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_4(a, i, j):

    if i <= 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_5(a, i, j):

    if i < 1 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_6(a, i, j):

    if i < 0 or i > len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_7(a, i, j):

    if i < 0 or i >= len(a) or j <= 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_8(a, i, j):

    if i < 0 or i >= len(a) or j < 1 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_9(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j > len(a):
        return -1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_10(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return +1000
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_11(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1001
    else:
        return a[i] + a[j] / 2
def x_sum_labeled__mutmut_12(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] - a[j] / 2
def x_sum_labeled__mutmut_13(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] * 2
def x_sum_labeled__mutmut_14(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 3

x_sum_labeled__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_labeled__mutmut_1': x_sum_labeled__mutmut_1, 
    'x_sum_labeled__mutmut_2': x_sum_labeled__mutmut_2, 
    'x_sum_labeled__mutmut_3': x_sum_labeled__mutmut_3, 
    'x_sum_labeled__mutmut_4': x_sum_labeled__mutmut_4, 
    'x_sum_labeled__mutmut_5': x_sum_labeled__mutmut_5, 
    'x_sum_labeled__mutmut_6': x_sum_labeled__mutmut_6, 
    'x_sum_labeled__mutmut_7': x_sum_labeled__mutmut_7, 
    'x_sum_labeled__mutmut_8': x_sum_labeled__mutmut_8, 
    'x_sum_labeled__mutmut_9': x_sum_labeled__mutmut_9, 
    'x_sum_labeled__mutmut_10': x_sum_labeled__mutmut_10, 
    'x_sum_labeled__mutmut_11': x_sum_labeled__mutmut_11, 
    'x_sum_labeled__mutmut_12': x_sum_labeled__mutmut_12, 
    'x_sum_labeled__mutmut_13': x_sum_labeled__mutmut_13, 
    'x_sum_labeled__mutmut_14': x_sum_labeled__mutmut_14
}

def sum_labeled(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_labeled__mutmut_orig, x_sum_labeled__mutmut_mutants, args, kwargs)
    return result 

sum_labeled.__signature__ = _mutmut_signature(x_sum_labeled__mutmut_orig)
x_sum_labeled__mutmut_orig.__name__ = 'x_sum_labeled'