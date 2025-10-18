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
def x_weightedRMS__mutmut_orig(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_1(data, weights):

    sumOfProducts = None
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_2(data, weights):

    sumOfProducts = 1
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_3(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = None

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_4(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 1

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_5(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(None, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_6(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, None):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_7(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_8(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, ):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_9(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(1, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_10(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts = data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_11(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts -= data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_12(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] / weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_13(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = None

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_14(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] / weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_15(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] / data[i] * weights[i]

    return sumOfProducts / sumOfSquaredProducts
def x_weightedRMS__mutmut_16(data, weights):

    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return sumOfProducts * sumOfSquaredProducts

x_weightedRMS__mutmut_mutants : ClassVar[MutantDict] = {
'x_weightedRMS__mutmut_1': x_weightedRMS__mutmut_1, 
    'x_weightedRMS__mutmut_2': x_weightedRMS__mutmut_2, 
    'x_weightedRMS__mutmut_3': x_weightedRMS__mutmut_3, 
    'x_weightedRMS__mutmut_4': x_weightedRMS__mutmut_4, 
    'x_weightedRMS__mutmut_5': x_weightedRMS__mutmut_5, 
    'x_weightedRMS__mutmut_6': x_weightedRMS__mutmut_6, 
    'x_weightedRMS__mutmut_7': x_weightedRMS__mutmut_7, 
    'x_weightedRMS__mutmut_8': x_weightedRMS__mutmut_8, 
    'x_weightedRMS__mutmut_9': x_weightedRMS__mutmut_9, 
    'x_weightedRMS__mutmut_10': x_weightedRMS__mutmut_10, 
    'x_weightedRMS__mutmut_11': x_weightedRMS__mutmut_11, 
    'x_weightedRMS__mutmut_12': x_weightedRMS__mutmut_12, 
    'x_weightedRMS__mutmut_13': x_weightedRMS__mutmut_13, 
    'x_weightedRMS__mutmut_14': x_weightedRMS__mutmut_14, 
    'x_weightedRMS__mutmut_15': x_weightedRMS__mutmut_15, 
    'x_weightedRMS__mutmut_16': x_weightedRMS__mutmut_16
}

def weightedRMS(*args, **kwargs):
    result = _mutmut_trampoline(x_weightedRMS__mutmut_orig, x_weightedRMS__mutmut_mutants, args, kwargs)
    return result 

weightedRMS.__signature__ = _mutmut_signature(x_weightedRMS__mutmut_orig)
x_weightedRMS__mutmut_orig.__name__ = 'x_weightedRMS'
