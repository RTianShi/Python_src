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
def x_mean_abs_error__mutmut_orig(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_1(a, b):
    suma = None
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_2(a, b):
    suma = 1
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_3(a, b):
    suma = 0
    for i in range(None, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_4(a, b):
    suma = 0
    for i in range(0, None):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_5(a, b):
    suma = 0
    for i in range(len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_6(a, b):
    suma = 0
    for i in range(0, ):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_7(a, b):
    suma = 0
    for i in range(1, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_8(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma = abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_9(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma -= abs(a[i] - b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_10(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma += abs(None)

    return suma / len(a)
def x_mean_abs_error__mutmut_11(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma += abs(a[i] + b[i])

    return suma / len(a)
def x_mean_abs_error__mutmut_12(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma * len(a)

x_mean_abs_error__mutmut_mutants : ClassVar[MutantDict] = {
'x_mean_abs_error__mutmut_1': x_mean_abs_error__mutmut_1, 
    'x_mean_abs_error__mutmut_2': x_mean_abs_error__mutmut_2, 
    'x_mean_abs_error__mutmut_3': x_mean_abs_error__mutmut_3, 
    'x_mean_abs_error__mutmut_4': x_mean_abs_error__mutmut_4, 
    'x_mean_abs_error__mutmut_5': x_mean_abs_error__mutmut_5, 
    'x_mean_abs_error__mutmut_6': x_mean_abs_error__mutmut_6, 
    'x_mean_abs_error__mutmut_7': x_mean_abs_error__mutmut_7, 
    'x_mean_abs_error__mutmut_8': x_mean_abs_error__mutmut_8, 
    'x_mean_abs_error__mutmut_9': x_mean_abs_error__mutmut_9, 
    'x_mean_abs_error__mutmut_10': x_mean_abs_error__mutmut_10, 
    'x_mean_abs_error__mutmut_11': x_mean_abs_error__mutmut_11, 
    'x_mean_abs_error__mutmut_12': x_mean_abs_error__mutmut_12
}

def mean_abs_error(*args, **kwargs):
    result = _mutmut_trampoline(x_mean_abs_error__mutmut_orig, x_mean_abs_error__mutmut_mutants, args, kwargs)
    return result 

mean_abs_error.__signature__ = _mutmut_signature(x_mean_abs_error__mutmut_orig)
x_mean_abs_error__mutmut_orig.__name__ = 'x_mean_abs_error'
