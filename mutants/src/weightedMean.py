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
def x_weightedMean__mutmut_orig(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_1(elements, theWeigths):

    size = None
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_2(elements, theWeigths):

    size = len(elements)
    suma = None
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_3(elements, theWeigths):

    size = len(elements)
    suma = 1
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_4(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = None
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_5(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 1
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_6(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(None, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_7(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, None, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_8(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, None):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_9(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(-1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_10(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_11(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, ):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_12(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, +1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_13(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -2, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_14(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, +1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_15(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -2):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_16(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = None
        suma += elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_17(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma = elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_18(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma -= elements[i] * w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_19(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] / w
        weightSum += w
    return suma / weightSum
def x_weightedMean__mutmut_20(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum = w
    return suma / weightSum
def x_weightedMean__mutmut_21(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum -= w
    return suma / weightSum
def x_weightedMean__mutmut_22(elements, theWeigths):

    size = len(elements)
    suma = 0
    weightSum = 0
    for i in range(size, -1, -1):
        w = theWeigths[i]
        suma += elements[i] * w
        weightSum += w
    return suma * weightSum

x_weightedMean__mutmut_mutants : ClassVar[MutantDict] = {
'x_weightedMean__mutmut_1': x_weightedMean__mutmut_1, 
    'x_weightedMean__mutmut_2': x_weightedMean__mutmut_2, 
    'x_weightedMean__mutmut_3': x_weightedMean__mutmut_3, 
    'x_weightedMean__mutmut_4': x_weightedMean__mutmut_4, 
    'x_weightedMean__mutmut_5': x_weightedMean__mutmut_5, 
    'x_weightedMean__mutmut_6': x_weightedMean__mutmut_6, 
    'x_weightedMean__mutmut_7': x_weightedMean__mutmut_7, 
    'x_weightedMean__mutmut_8': x_weightedMean__mutmut_8, 
    'x_weightedMean__mutmut_9': x_weightedMean__mutmut_9, 
    'x_weightedMean__mutmut_10': x_weightedMean__mutmut_10, 
    'x_weightedMean__mutmut_11': x_weightedMean__mutmut_11, 
    'x_weightedMean__mutmut_12': x_weightedMean__mutmut_12, 
    'x_weightedMean__mutmut_13': x_weightedMean__mutmut_13, 
    'x_weightedMean__mutmut_14': x_weightedMean__mutmut_14, 
    'x_weightedMean__mutmut_15': x_weightedMean__mutmut_15, 
    'x_weightedMean__mutmut_16': x_weightedMean__mutmut_16, 
    'x_weightedMean__mutmut_17': x_weightedMean__mutmut_17, 
    'x_weightedMean__mutmut_18': x_weightedMean__mutmut_18, 
    'x_weightedMean__mutmut_19': x_weightedMean__mutmut_19, 
    'x_weightedMean__mutmut_20': x_weightedMean__mutmut_20, 
    'x_weightedMean__mutmut_21': x_weightedMean__mutmut_21, 
    'x_weightedMean__mutmut_22': x_weightedMean__mutmut_22
}

def weightedMean(*args, **kwargs):
    result = _mutmut_trampoline(x_weightedMean__mutmut_orig, x_weightedMean__mutmut_mutants, args, kwargs)
    return result 

weightedMean.__signature__ = _mutmut_signature(x_weightedMean__mutmut_orig)
x_weightedMean__mutmut_orig.__name__ = 'x_weightedMean'
