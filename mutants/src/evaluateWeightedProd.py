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


def x_evaluateWeightedProd__mutmut_orig(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_1(values, weigths, begin, length):

    product = None
    for i in range(begin, begin + length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_2(values, weigths, begin, length):

    product = 2
    for i in range(begin, begin + length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_3(values, weigths, begin, length):

    product = 1
    for i in range(None, begin + length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_4(values, weigths, begin, length):

    product = 1
    for i in range(begin, None):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_5(values, weigths, begin, length):

    product = 1
    for i in range(begin + length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_6(values, weigths, begin, length):

    product = 1
    for i in range(begin, ):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_7(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin - length):
        product *= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_8(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product = math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_9(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product /= math.pow(values[i], weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_10(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(None, weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_11(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(values[i], None)

    return product


def x_evaluateWeightedProd__mutmut_12(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(weigths[i])

    return product


def x_evaluateWeightedProd__mutmut_13(values, weigths, begin, length):

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(values[i], )

    return product

x_evaluateWeightedProd__mutmut_mutants : ClassVar[MutantDict] = {
'x_evaluateWeightedProd__mutmut_1': x_evaluateWeightedProd__mutmut_1, 
    'x_evaluateWeightedProd__mutmut_2': x_evaluateWeightedProd__mutmut_2, 
    'x_evaluateWeightedProd__mutmut_3': x_evaluateWeightedProd__mutmut_3, 
    'x_evaluateWeightedProd__mutmut_4': x_evaluateWeightedProd__mutmut_4, 
    'x_evaluateWeightedProd__mutmut_5': x_evaluateWeightedProd__mutmut_5, 
    'x_evaluateWeightedProd__mutmut_6': x_evaluateWeightedProd__mutmut_6, 
    'x_evaluateWeightedProd__mutmut_7': x_evaluateWeightedProd__mutmut_7, 
    'x_evaluateWeightedProd__mutmut_8': x_evaluateWeightedProd__mutmut_8, 
    'x_evaluateWeightedProd__mutmut_9': x_evaluateWeightedProd__mutmut_9, 
    'x_evaluateWeightedProd__mutmut_10': x_evaluateWeightedProd__mutmut_10, 
    'x_evaluateWeightedProd__mutmut_11': x_evaluateWeightedProd__mutmut_11, 
    'x_evaluateWeightedProd__mutmut_12': x_evaluateWeightedProd__mutmut_12, 
    'x_evaluateWeightedProd__mutmut_13': x_evaluateWeightedProd__mutmut_13
}

def evaluateWeightedProd(*args, **kwargs):
    result = _mutmut_trampoline(x_evaluateWeightedProd__mutmut_orig, x_evaluateWeightedProd__mutmut_mutants, args, kwargs)
    return result 

evaluateWeightedProd.__signature__ = _mutmut_signature(x_evaluateWeightedProd__mutmut_orig)
x_evaluateWeightedProd__mutmut_orig.__name__ = 'x_evaluateWeightedProd'
