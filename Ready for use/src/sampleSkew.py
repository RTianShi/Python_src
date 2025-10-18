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


def x_sampleSkew__mutmut_orig(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_1(size, moment3, sampleVariance):
    n = None
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_2(size, moment3, sampleVariance):
    n = size
    s = None
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_3(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(None)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_4(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = None
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_5(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 / n
    return n * m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_6(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 * ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_7(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n / m3 / ((n - 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_8(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s * s / s)


def x_sampleSkew__mutmut_9(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s / s * s)


def x_sampleSkew__mutmut_10(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) / s * s * s)


def x_sampleSkew__mutmut_11(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) / (n - 2) * s * s * s)


def x_sampleSkew__mutmut_12(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n + 1) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_13(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 2) * (n - 2) * s * s * s)


def x_sampleSkew__mutmut_14(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n + 2) * s * s * s)


def x_sampleSkew__mutmut_15(size, moment3, sampleVariance):
    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 3) * s * s * s)

x_sampleSkew__mutmut_mutants : ClassVar[MutantDict] = {
'x_sampleSkew__mutmut_1': x_sampleSkew__mutmut_1, 
    'x_sampleSkew__mutmut_2': x_sampleSkew__mutmut_2, 
    'x_sampleSkew__mutmut_3': x_sampleSkew__mutmut_3, 
    'x_sampleSkew__mutmut_4': x_sampleSkew__mutmut_4, 
    'x_sampleSkew__mutmut_5': x_sampleSkew__mutmut_5, 
    'x_sampleSkew__mutmut_6': x_sampleSkew__mutmut_6, 
    'x_sampleSkew__mutmut_7': x_sampleSkew__mutmut_7, 
    'x_sampleSkew__mutmut_8': x_sampleSkew__mutmut_8, 
    'x_sampleSkew__mutmut_9': x_sampleSkew__mutmut_9, 
    'x_sampleSkew__mutmut_10': x_sampleSkew__mutmut_10, 
    'x_sampleSkew__mutmut_11': x_sampleSkew__mutmut_11, 
    'x_sampleSkew__mutmut_12': x_sampleSkew__mutmut_12, 
    'x_sampleSkew__mutmut_13': x_sampleSkew__mutmut_13, 
    'x_sampleSkew__mutmut_14': x_sampleSkew__mutmut_14, 
    'x_sampleSkew__mutmut_15': x_sampleSkew__mutmut_15
}

def sampleSkew(*args, **kwargs):
    result = _mutmut_trampoline(x_sampleSkew__mutmut_orig, x_sampleSkew__mutmut_mutants, args, kwargs)
    return result 

sampleSkew.__signature__ = _mutmut_signature(x_sampleSkew__mutmut_orig)
x_sampleSkew__mutmut_orig.__name__ = 'x_sampleSkew'
