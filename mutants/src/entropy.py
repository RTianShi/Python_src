import numpy as np
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


def x_entropy__mutmut_orig(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_1(k):
    h = None
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_2(k):
    h = 1
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_3(k):
    h = 0
    sum_k = None
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_4(k):
    h = 0
    sum_k = 1
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_5(k):
    h = 0
    sum_k = 0
    for i in range(None, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_6(k):
    h = 0
    sum_k = 0
    for i in range(0, None):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_7(k):
    h = 0
    sum_k = 0
    for i in range(len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_8(k):
    h = 0
    sum_k = 0
    for i in range(0, ):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_9(k):
    h = 0
    sum_k = 0
    for i in range(1, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_10(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k = k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_11(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k -= k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_12(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i == 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_13(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 1:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_14(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = None
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_15(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i * sum_k
            h += p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_16(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h = p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_17(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h -= p_i * np.log(p_i)

    return -h


def x_entropy__mutmut_18(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i / np.log(p_i)

    return -h


def x_entropy__mutmut_19(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(None)

    return -h


def x_entropy__mutmut_20(k):
    h = 0
    sum_k = 0
    for i in range(0, len(k)):
        sum_k += k[i]

    for i in k:
        if i != 0:
            p_i = i / sum_k
            h += p_i * np.log(p_i)

    return +h

x_entropy__mutmut_mutants : ClassVar[MutantDict] = {
'x_entropy__mutmut_1': x_entropy__mutmut_1, 
    'x_entropy__mutmut_2': x_entropy__mutmut_2, 
    'x_entropy__mutmut_3': x_entropy__mutmut_3, 
    'x_entropy__mutmut_4': x_entropy__mutmut_4, 
    'x_entropy__mutmut_5': x_entropy__mutmut_5, 
    'x_entropy__mutmut_6': x_entropy__mutmut_6, 
    'x_entropy__mutmut_7': x_entropy__mutmut_7, 
    'x_entropy__mutmut_8': x_entropy__mutmut_8, 
    'x_entropy__mutmut_9': x_entropy__mutmut_9, 
    'x_entropy__mutmut_10': x_entropy__mutmut_10, 
    'x_entropy__mutmut_11': x_entropy__mutmut_11, 
    'x_entropy__mutmut_12': x_entropy__mutmut_12, 
    'x_entropy__mutmut_13': x_entropy__mutmut_13, 
    'x_entropy__mutmut_14': x_entropy__mutmut_14, 
    'x_entropy__mutmut_15': x_entropy__mutmut_15, 
    'x_entropy__mutmut_16': x_entropy__mutmut_16, 
    'x_entropy__mutmut_17': x_entropy__mutmut_17, 
    'x_entropy__mutmut_18': x_entropy__mutmut_18, 
    'x_entropy__mutmut_19': x_entropy__mutmut_19, 
    'x_entropy__mutmut_20': x_entropy__mutmut_20
}

def entropy(*args, **kwargs):
    result = _mutmut_trampoline(x_entropy__mutmut_orig, x_entropy__mutmut_mutants, args, kwargs)
    return result 

entropy.__signature__ = _mutmut_signature(x_entropy__mutmut_orig)
x_entropy__mutmut_orig.__name__ = 'x_entropy'
