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


def x_distInf__mutmut_orig(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_1(p1, p2):
    max = None
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_2(p1, p2):
    max = 1
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_3(p1, p2):
    max = 0
    for i in range(None, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_4(p1, p2):
    max = 0
    for i in range(0, None):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_5(p1, p2):
    max = 0
    for i in range(len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_6(p1, p2):
    max = 0
    for i in range(0, ):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_7(p1, p2):
    max = 0
    for i in range(1, len(p1)):
        max = np.maximum(max, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_8(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = None

    return max


def x_distInf__mutmut_9(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(None, abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_10(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, None)

    return max


def x_distInf__mutmut_11(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(abs(p1[i] - p2[i]))

    return max


def x_distInf__mutmut_12(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, )

    return max


def x_distInf__mutmut_13(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(None))

    return max


def x_distInf__mutmut_14(p1, p2):
    max = 0
    for i in range(0, len(p1)):
        max = np.maximum(max, abs(p1[i] + p2[i]))

    return max

x_distInf__mutmut_mutants : ClassVar[MutantDict] = {
'x_distInf__mutmut_1': x_distInf__mutmut_1, 
    'x_distInf__mutmut_2': x_distInf__mutmut_2, 
    'x_distInf__mutmut_3': x_distInf__mutmut_3, 
    'x_distInf__mutmut_4': x_distInf__mutmut_4, 
    'x_distInf__mutmut_5': x_distInf__mutmut_5, 
    'x_distInf__mutmut_6': x_distInf__mutmut_6, 
    'x_distInf__mutmut_7': x_distInf__mutmut_7, 
    'x_distInf__mutmut_8': x_distInf__mutmut_8, 
    'x_distInf__mutmut_9': x_distInf__mutmut_9, 
    'x_distInf__mutmut_10': x_distInf__mutmut_10, 
    'x_distInf__mutmut_11': x_distInf__mutmut_11, 
    'x_distInf__mutmut_12': x_distInf__mutmut_12, 
    'x_distInf__mutmut_13': x_distInf__mutmut_13, 
    'x_distInf__mutmut_14': x_distInf__mutmut_14
}

def distInf(*args, **kwargs):
    result = _mutmut_trampoline(x_distInf__mutmut_orig, x_distInf__mutmut_mutants, args, kwargs)
    return result 

distInf.__signature__ = _mutmut_signature(x_distInf__mutmut_orig)
x_distInf__mutmut_orig.__name__ = 'x_distInf'
