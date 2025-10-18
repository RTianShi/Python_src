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
def x_scale__mutmut_orig(val, arr):

    newArr = []

    for i in range(0, len(arr)):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_1(val, arr):

    newArr = None

    for i in range(0, len(arr)):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_2(val, arr):

    newArr = []

    for i in range(None, len(arr)):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_3(val, arr):

    newArr = []

    for i in range(0, None):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_4(val, arr):

    newArr = []

    for i in range(len(arr)):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_5(val, arr):

    newArr = []

    for i in range(0, ):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_6(val, arr):

    newArr = []

    for i in range(1, len(arr)):
        newArr[i] = arr[i] * val

    return newArr
def x_scale__mutmut_7(val, arr):

    newArr = []

    for i in range(0, len(arr)):
        newArr[i] = None

    return newArr
def x_scale__mutmut_8(val, arr):

    newArr = []

    for i in range(0, len(arr)):
        newArr[i] = arr[i] / val

    return newArr

x_scale__mutmut_mutants : ClassVar[MutantDict] = {
'x_scale__mutmut_1': x_scale__mutmut_1, 
    'x_scale__mutmut_2': x_scale__mutmut_2, 
    'x_scale__mutmut_3': x_scale__mutmut_3, 
    'x_scale__mutmut_4': x_scale__mutmut_4, 
    'x_scale__mutmut_5': x_scale__mutmut_5, 
    'x_scale__mutmut_6': x_scale__mutmut_6, 
    'x_scale__mutmut_7': x_scale__mutmut_7, 
    'x_scale__mutmut_8': x_scale__mutmut_8
}

def scale(*args, **kwargs):
    result = _mutmut_trampoline(x_scale__mutmut_orig, x_scale__mutmut_mutants, args, kwargs)
    return result 

scale.__signature__ = _mutmut_signature(x_scale__mutmut_orig)
x_scale__mutmut_orig.__name__ = 'x_scale'
