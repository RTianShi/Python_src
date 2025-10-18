import math
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


def x_sum_Power_Deviat__mutmut_orig(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_1(data, k, c):
    suma = None
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_2(data, k, c):
    suma = 1
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_3(data, k, c):
    suma = 0
    for i in range(None, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_4(data, k, c):
    suma = 0
    for i in range(0, None):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_5(data, k, c):
    suma = 0
    for i in range(len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_6(data, k, c):
    suma = 0
    for i in range(0, ):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_7(data, k, c):
    suma = 0
    for i in range(1, len(data)):
        suma += math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_8(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma = math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_9(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma -= math.pow( data[i] - c, k)

    return suma


def x_sum_Power_Deviat__mutmut_10(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( None, k)

    return suma


def x_sum_Power_Deviat__mutmut_11(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, None)

    return suma


def x_sum_Power_Deviat__mutmut_12(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( k)

    return suma


def x_sum_Power_Deviat__mutmut_13(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( data[i] - c, )

    return suma


def x_sum_Power_Deviat__mutmut_14(data, k, c):
    suma = 0
    for i in range(0, len(data)):
        suma += math.pow( data[i] + c, k)

    return suma

x_sum_Power_Deviat__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_Power_Deviat__mutmut_1': x_sum_Power_Deviat__mutmut_1, 
    'x_sum_Power_Deviat__mutmut_2': x_sum_Power_Deviat__mutmut_2, 
    'x_sum_Power_Deviat__mutmut_3': x_sum_Power_Deviat__mutmut_3, 
    'x_sum_Power_Deviat__mutmut_4': x_sum_Power_Deviat__mutmut_4, 
    'x_sum_Power_Deviat__mutmut_5': x_sum_Power_Deviat__mutmut_5, 
    'x_sum_Power_Deviat__mutmut_6': x_sum_Power_Deviat__mutmut_6, 
    'x_sum_Power_Deviat__mutmut_7': x_sum_Power_Deviat__mutmut_7, 
    'x_sum_Power_Deviat__mutmut_8': x_sum_Power_Deviat__mutmut_8, 
    'x_sum_Power_Deviat__mutmut_9': x_sum_Power_Deviat__mutmut_9, 
    'x_sum_Power_Deviat__mutmut_10': x_sum_Power_Deviat__mutmut_10, 
    'x_sum_Power_Deviat__mutmut_11': x_sum_Power_Deviat__mutmut_11, 
    'x_sum_Power_Deviat__mutmut_12': x_sum_Power_Deviat__mutmut_12, 
    'x_sum_Power_Deviat__mutmut_13': x_sum_Power_Deviat__mutmut_13, 
    'x_sum_Power_Deviat__mutmut_14': x_sum_Power_Deviat__mutmut_14
}

def sum_Power_Deviat(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_Power_Deviat__mutmut_orig, x_sum_Power_Deviat__mutmut_mutants, args, kwargs)
    return result 

sum_Power_Deviat.__signature__ = _mutmut_signature(x_sum_Power_Deviat__mutmut_orig)
x_sum_Power_Deviat__mutmut_orig.__name__ = 'x_sum_Power_Deviat'
