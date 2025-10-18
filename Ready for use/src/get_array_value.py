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
def x_get_array_value__mutmut_orig(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_1(a, k):

    if k - 1 >= len(a) and k - 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_2(a, k):

    if k + 1 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_3(a, k):

    if k - 2 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_4(a, k):

    if k - 1 > len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_5(a, k):

    if k - 1 >= len(a) or k + 1 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_6(a, k):

    if k - 1 >= len(a) or k - 2 < 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_7(a, k):

    if k - 1 >= len(a) or k - 1 <= 0:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_8(a, k):

    if k - 1 >= len(a) or k - 1 < 1:
        return -100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_9(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return +100000
    else:
        return a[k-1]
def x_get_array_value__mutmut_10(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return -100001
    else:
        return a[k-1]
def x_get_array_value__mutmut_11(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k + 1]
def x_get_array_value__mutmut_12(a, k):

    if k - 1 >= len(a) or k - 1 < 0:
        return -100000
    else:
        return a[k-2]

x_get_array_value__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_array_value__mutmut_1': x_get_array_value__mutmut_1, 
    'x_get_array_value__mutmut_2': x_get_array_value__mutmut_2, 
    'x_get_array_value__mutmut_3': x_get_array_value__mutmut_3, 
    'x_get_array_value__mutmut_4': x_get_array_value__mutmut_4, 
    'x_get_array_value__mutmut_5': x_get_array_value__mutmut_5, 
    'x_get_array_value__mutmut_6': x_get_array_value__mutmut_6, 
    'x_get_array_value__mutmut_7': x_get_array_value__mutmut_7, 
    'x_get_array_value__mutmut_8': x_get_array_value__mutmut_8, 
    'x_get_array_value__mutmut_9': x_get_array_value__mutmut_9, 
    'x_get_array_value__mutmut_10': x_get_array_value__mutmut_10, 
    'x_get_array_value__mutmut_11': x_get_array_value__mutmut_11, 
    'x_get_array_value__mutmut_12': x_get_array_value__mutmut_12
}

def get_array_value(*args, **kwargs):
    result = _mutmut_trampoline(x_get_array_value__mutmut_orig, x_get_array_value__mutmut_mutants, args, kwargs)
    return result 

get_array_value.__signature__ = _mutmut_signature(x_get_array_value__mutmut_orig)
x_get_array_value__mutmut_orig.__name__ = 'x_get_array_value'
