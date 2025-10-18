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
def x_meanDeviation__mutmut_orig(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_1(elements, mean):
    size = None

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_2(elements, mean):
    size = len(elements)

    suma = None

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_3(elements, mean):
    size = len(elements)

    suma = 1

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_4(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(None , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_5(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , None, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_6(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, None):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_7(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(-1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_8(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_9(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, ):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_10(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size + 1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_11(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-2 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_12(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , +1, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_13(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -2, -1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_14(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, +1):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_15(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -2):
        suma += abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_16(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma = abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_17(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma -= abs(elements[i] - mean)

    return suma / size
def x_meanDeviation__mutmut_18(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(None)

    return suma / size
def x_meanDeviation__mutmut_19(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] + mean)

    return suma / size
def x_meanDeviation__mutmut_20(elements, mean):
    size = len(elements)

    suma = 0

    for i in range(size-1 , -1, -1):
        suma += abs(elements[i] - mean)

    return suma * size

x_meanDeviation__mutmut_mutants : ClassVar[MutantDict] = {
'x_meanDeviation__mutmut_1': x_meanDeviation__mutmut_1, 
    'x_meanDeviation__mutmut_2': x_meanDeviation__mutmut_2, 
    'x_meanDeviation__mutmut_3': x_meanDeviation__mutmut_3, 
    'x_meanDeviation__mutmut_4': x_meanDeviation__mutmut_4, 
    'x_meanDeviation__mutmut_5': x_meanDeviation__mutmut_5, 
    'x_meanDeviation__mutmut_6': x_meanDeviation__mutmut_6, 
    'x_meanDeviation__mutmut_7': x_meanDeviation__mutmut_7, 
    'x_meanDeviation__mutmut_8': x_meanDeviation__mutmut_8, 
    'x_meanDeviation__mutmut_9': x_meanDeviation__mutmut_9, 
    'x_meanDeviation__mutmut_10': x_meanDeviation__mutmut_10, 
    'x_meanDeviation__mutmut_11': x_meanDeviation__mutmut_11, 
    'x_meanDeviation__mutmut_12': x_meanDeviation__mutmut_12, 
    'x_meanDeviation__mutmut_13': x_meanDeviation__mutmut_13, 
    'x_meanDeviation__mutmut_14': x_meanDeviation__mutmut_14, 
    'x_meanDeviation__mutmut_15': x_meanDeviation__mutmut_15, 
    'x_meanDeviation__mutmut_16': x_meanDeviation__mutmut_16, 
    'x_meanDeviation__mutmut_17': x_meanDeviation__mutmut_17, 
    'x_meanDeviation__mutmut_18': x_meanDeviation__mutmut_18, 
    'x_meanDeviation__mutmut_19': x_meanDeviation__mutmut_19, 
    'x_meanDeviation__mutmut_20': x_meanDeviation__mutmut_20
}

def meanDeviation(*args, **kwargs):
    result = _mutmut_trampoline(x_meanDeviation__mutmut_orig, x_meanDeviation__mutmut_mutants, args, kwargs)
    return result 

meanDeviation.__signature__ = _mutmut_signature(x_meanDeviation__mutmut_orig)
x_meanDeviation__mutmut_orig.__name__ = 'x_meanDeviation'
