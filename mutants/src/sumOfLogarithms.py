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


def x_sumOfLogarithms__mutmut_orig(elements):
    logsum = 0

    for i in range(0, len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_1(elements):
    logsum = None

    for i in range(0, len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_2(elements):
    logsum = 1

    for i in range(0, len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_3(elements):
    logsum = 0

    for i in range(None, len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_4(elements):
    logsum = 0

    for i in range(0, None):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_5(elements):
    logsum = 0

    for i in range(len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_6(elements):
    logsum = 0

    for i in range(0, ):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_7(elements):
    logsum = 0

    for i in range(1, len(elements)):
        logsum += math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_8(elements):
    logsum = 0

    for i in range(0, len(elements)):
        logsum = math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_9(elements):
    logsum = 0

    for i in range(0, len(elements)):
        logsum -= math.log(elements[i])

    return logsum


def x_sumOfLogarithms__mutmut_10(elements):
    logsum = 0

    for i in range(0, len(elements)):
        logsum += math.log(None)

    return logsum

x_sumOfLogarithms__mutmut_mutants : ClassVar[MutantDict] = {
'x_sumOfLogarithms__mutmut_1': x_sumOfLogarithms__mutmut_1, 
    'x_sumOfLogarithms__mutmut_2': x_sumOfLogarithms__mutmut_2, 
    'x_sumOfLogarithms__mutmut_3': x_sumOfLogarithms__mutmut_3, 
    'x_sumOfLogarithms__mutmut_4': x_sumOfLogarithms__mutmut_4, 
    'x_sumOfLogarithms__mutmut_5': x_sumOfLogarithms__mutmut_5, 
    'x_sumOfLogarithms__mutmut_6': x_sumOfLogarithms__mutmut_6, 
    'x_sumOfLogarithms__mutmut_7': x_sumOfLogarithms__mutmut_7, 
    'x_sumOfLogarithms__mutmut_8': x_sumOfLogarithms__mutmut_8, 
    'x_sumOfLogarithms__mutmut_9': x_sumOfLogarithms__mutmut_9, 
    'x_sumOfLogarithms__mutmut_10': x_sumOfLogarithms__mutmut_10
}

def sumOfLogarithms(*args, **kwargs):
    result = _mutmut_trampoline(x_sumOfLogarithms__mutmut_orig, x_sumOfLogarithms__mutmut_mutants, args, kwargs)
    return result 

sumOfLogarithms.__signature__ = _mutmut_signature(x_sumOfLogarithms__mutmut_orig)
x_sumOfLogarithms__mutmut_orig.__name__ = 'x_sumOfLogarithms'
