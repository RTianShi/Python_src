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
def x_sampleKurtosis__mutmut_orig(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_1(size, moment4, sampleVariance):
    n = None
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_2(size, moment4, sampleVariance):
    n = size
    s2 = None
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_3(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = None
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_4(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) + 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_5(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) * ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_6(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n / (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_7(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 / n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_8(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n - 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_9(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 2) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_10(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 / s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_11(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) / s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_12(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) / (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_13(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) / (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_14(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n + 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_15(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 2) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_16(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n + 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_17(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 3) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_18(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n + 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_19(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 4) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_20(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) * ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_21(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) / (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_22(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 / (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_23(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 4.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_24(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n + 1) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_25(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 2) * (n - 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_26(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n + 1) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_27(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 2) / ((n - 2) * (n - 3))
def x_sampleKurtosis__mutmut_28(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) / (n - 3))
def x_sampleKurtosis__mutmut_29(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n + 2) * (n - 3))
def x_sampleKurtosis__mutmut_30(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 3) * (n - 3))
def x_sampleKurtosis__mutmut_31(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n + 3))
def x_sampleKurtosis__mutmut_32(size, moment4, sampleVariance):
    n = size
    s2 = sampleVariance
    m4 = moment4
    return m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2) - 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 4))

x_sampleKurtosis__mutmut_mutants : ClassVar[MutantDict] = {
'x_sampleKurtosis__mutmut_1': x_sampleKurtosis__mutmut_1, 
    'x_sampleKurtosis__mutmut_2': x_sampleKurtosis__mutmut_2, 
    'x_sampleKurtosis__mutmut_3': x_sampleKurtosis__mutmut_3, 
    'x_sampleKurtosis__mutmut_4': x_sampleKurtosis__mutmut_4, 
    'x_sampleKurtosis__mutmut_5': x_sampleKurtosis__mutmut_5, 
    'x_sampleKurtosis__mutmut_6': x_sampleKurtosis__mutmut_6, 
    'x_sampleKurtosis__mutmut_7': x_sampleKurtosis__mutmut_7, 
    'x_sampleKurtosis__mutmut_8': x_sampleKurtosis__mutmut_8, 
    'x_sampleKurtosis__mutmut_9': x_sampleKurtosis__mutmut_9, 
    'x_sampleKurtosis__mutmut_10': x_sampleKurtosis__mutmut_10, 
    'x_sampleKurtosis__mutmut_11': x_sampleKurtosis__mutmut_11, 
    'x_sampleKurtosis__mutmut_12': x_sampleKurtosis__mutmut_12, 
    'x_sampleKurtosis__mutmut_13': x_sampleKurtosis__mutmut_13, 
    'x_sampleKurtosis__mutmut_14': x_sampleKurtosis__mutmut_14, 
    'x_sampleKurtosis__mutmut_15': x_sampleKurtosis__mutmut_15, 
    'x_sampleKurtosis__mutmut_16': x_sampleKurtosis__mutmut_16, 
    'x_sampleKurtosis__mutmut_17': x_sampleKurtosis__mutmut_17, 
    'x_sampleKurtosis__mutmut_18': x_sampleKurtosis__mutmut_18, 
    'x_sampleKurtosis__mutmut_19': x_sampleKurtosis__mutmut_19, 
    'x_sampleKurtosis__mutmut_20': x_sampleKurtosis__mutmut_20, 
    'x_sampleKurtosis__mutmut_21': x_sampleKurtosis__mutmut_21, 
    'x_sampleKurtosis__mutmut_22': x_sampleKurtosis__mutmut_22, 
    'x_sampleKurtosis__mutmut_23': x_sampleKurtosis__mutmut_23, 
    'x_sampleKurtosis__mutmut_24': x_sampleKurtosis__mutmut_24, 
    'x_sampleKurtosis__mutmut_25': x_sampleKurtosis__mutmut_25, 
    'x_sampleKurtosis__mutmut_26': x_sampleKurtosis__mutmut_26, 
    'x_sampleKurtosis__mutmut_27': x_sampleKurtosis__mutmut_27, 
    'x_sampleKurtosis__mutmut_28': x_sampleKurtosis__mutmut_28, 
    'x_sampleKurtosis__mutmut_29': x_sampleKurtosis__mutmut_29, 
    'x_sampleKurtosis__mutmut_30': x_sampleKurtosis__mutmut_30, 
    'x_sampleKurtosis__mutmut_31': x_sampleKurtosis__mutmut_31, 
    'x_sampleKurtosis__mutmut_32': x_sampleKurtosis__mutmut_32
}

def sampleKurtosis(*args, **kwargs):
    result = _mutmut_trampoline(x_sampleKurtosis__mutmut_orig, x_sampleKurtosis__mutmut_mutants, args, kwargs)
    return result 

sampleKurtosis.__signature__ = _mutmut_signature(x_sampleKurtosis__mutmut_orig)
x_sampleKurtosis__mutmut_orig.__name__ = 'x_sampleKurtosis'
