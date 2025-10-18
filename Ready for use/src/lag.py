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
def x_lag__mutmut_orig(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_1(elements, mean):
    v = None
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_2(elements, mean):
    v = (elements[0] - mean) / (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_3(elements, mean):
    v = (elements[0] + mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_4(elements, mean):
    v = (elements[1] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_5(elements, mean):
    v = (elements[0] - mean) * (elements[0] + mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_6(elements, mean):
    v = (elements[0] - mean) * (elements[1] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_7(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = None
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_8(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 1
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_9(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(None, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_10(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, None):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_11(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_12(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, ):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_13(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(1, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_14(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = None
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_15(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] + mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_16(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i + 1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_17(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -2] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_18(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = None

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_19(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] + mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_20(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q = (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_21(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q -= (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_22(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) * (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_23(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 + q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_24(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 / delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_25(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i - 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_26(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 2)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_27(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v = (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_28(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v -= (delta1 * delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_29(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) * (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_30(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 + v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_31(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 / delta1 - v) / (i + 1)

    r1 = q / v

    return r1
def x_lag__mutmut_32(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i - 1)

    r1 = q / v

    return r1
def x_lag__mutmut_33(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 2)

    r1 = q / v

    return r1
def x_lag__mutmut_34(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = None

    return r1
def x_lag__mutmut_35(elements, mean):
    v = (elements[0] - mean) * (elements[0] - mean)
    q = 0
    for i in range(0, len(elements)):
        delta0 = elements[i -1] - mean
        delta1 = elements[i] - mean

        q += (delta0 * delta1 - q) / (i + 1)
        v += (delta1 * delta1 - v) / (i + 1)

    r1 = q * v

    return r1

x_lag__mutmut_mutants : ClassVar[MutantDict] = {
'x_lag__mutmut_1': x_lag__mutmut_1, 
    'x_lag__mutmut_2': x_lag__mutmut_2, 
    'x_lag__mutmut_3': x_lag__mutmut_3, 
    'x_lag__mutmut_4': x_lag__mutmut_4, 
    'x_lag__mutmut_5': x_lag__mutmut_5, 
    'x_lag__mutmut_6': x_lag__mutmut_6, 
    'x_lag__mutmut_7': x_lag__mutmut_7, 
    'x_lag__mutmut_8': x_lag__mutmut_8, 
    'x_lag__mutmut_9': x_lag__mutmut_9, 
    'x_lag__mutmut_10': x_lag__mutmut_10, 
    'x_lag__mutmut_11': x_lag__mutmut_11, 
    'x_lag__mutmut_12': x_lag__mutmut_12, 
    'x_lag__mutmut_13': x_lag__mutmut_13, 
    'x_lag__mutmut_14': x_lag__mutmut_14, 
    'x_lag__mutmut_15': x_lag__mutmut_15, 
    'x_lag__mutmut_16': x_lag__mutmut_16, 
    'x_lag__mutmut_17': x_lag__mutmut_17, 
    'x_lag__mutmut_18': x_lag__mutmut_18, 
    'x_lag__mutmut_19': x_lag__mutmut_19, 
    'x_lag__mutmut_20': x_lag__mutmut_20, 
    'x_lag__mutmut_21': x_lag__mutmut_21, 
    'x_lag__mutmut_22': x_lag__mutmut_22, 
    'x_lag__mutmut_23': x_lag__mutmut_23, 
    'x_lag__mutmut_24': x_lag__mutmut_24, 
    'x_lag__mutmut_25': x_lag__mutmut_25, 
    'x_lag__mutmut_26': x_lag__mutmut_26, 
    'x_lag__mutmut_27': x_lag__mutmut_27, 
    'x_lag__mutmut_28': x_lag__mutmut_28, 
    'x_lag__mutmut_29': x_lag__mutmut_29, 
    'x_lag__mutmut_30': x_lag__mutmut_30, 
    'x_lag__mutmut_31': x_lag__mutmut_31, 
    'x_lag__mutmut_32': x_lag__mutmut_32, 
    'x_lag__mutmut_33': x_lag__mutmut_33, 
    'x_lag__mutmut_34': x_lag__mutmut_34, 
    'x_lag__mutmut_35': x_lag__mutmut_35
}

def lag(*args, **kwargs):
    result = _mutmut_trampoline(x_lag__mutmut_orig, x_lag__mutmut_mutants, args, kwargs)
    return result 

lag.__signature__ = _mutmut_signature(x_lag__mutmut_orig)
x_lag__mutmut_orig.__name__ = 'x_lag'

