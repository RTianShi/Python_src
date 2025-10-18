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
def x_find_diff__mutmut_orig(a, b):
    c = []
    for i in range(0, len(a)):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_1(a, b):
    c = None
    for i in range(0, len(a)):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_2(a, b):
    c = []
    for i in range(None, len(a)):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_3(a, b):
    c = []
    for i in range(0, None):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_4(a, b):
    c = []
    for i in range(len(a)):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_5(a, b):
    c = []
    for i in range(0, ):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_6(a, b):
    c = []
    for i in range(1, len(a)):
        c[i] = a[i] - b[i]
    return c
def x_find_diff__mutmut_7(a, b):
    c = []
    for i in range(0, len(a)):
        c[i] = None
    return c
def x_find_diff__mutmut_8(a, b):
    c = []
    for i in range(0, len(a)):
        c[i] = a[i] + b[i]
    return c

x_find_diff__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_diff__mutmut_1': x_find_diff__mutmut_1, 
    'x_find_diff__mutmut_2': x_find_diff__mutmut_2, 
    'x_find_diff__mutmut_3': x_find_diff__mutmut_3, 
    'x_find_diff__mutmut_4': x_find_diff__mutmut_4, 
    'x_find_diff__mutmut_5': x_find_diff__mutmut_5, 
    'x_find_diff__mutmut_6': x_find_diff__mutmut_6, 
    'x_find_diff__mutmut_7': x_find_diff__mutmut_7, 
    'x_find_diff__mutmut_8': x_find_diff__mutmut_8
}

def find_diff(*args, **kwargs):
    result = _mutmut_trampoline(x_find_diff__mutmut_orig, x_find_diff__mutmut_mutants, args, kwargs)
    return result 

find_diff.__signature__ = _mutmut_signature(x_find_diff__mutmut_orig)
x_find_diff__mutmut_orig.__name__ = 'x_find_diff'
