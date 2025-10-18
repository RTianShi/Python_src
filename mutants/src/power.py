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


def x_power__mutmut_orig(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_1(data, k):

    for i in range(None, len(data)):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_2(data, k):

    for i in range(0, None):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_3(data, k):

    for i in range(len(data)):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_4(data, k):

    for i in range(0, ):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_5(data, k):

    for i in range(1, len(data)):
        data[i] = math.pow(data[i], k)

    return data


def x_power__mutmut_6(data, k):

    for i in range(0, len(data)):
        data[i] = None

    return data


def x_power__mutmut_7(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(None, k)

    return data


def x_power__mutmut_8(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(data[i], None)

    return data


def x_power__mutmut_9(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(k)

    return data


def x_power__mutmut_10(data, k):

    for i in range(0, len(data)):
        data[i] = math.pow(data[i], )

    return data

x_power__mutmut_mutants : ClassVar[MutantDict] = {
'x_power__mutmut_1': x_power__mutmut_1, 
    'x_power__mutmut_2': x_power__mutmut_2, 
    'x_power__mutmut_3': x_power__mutmut_3, 
    'x_power__mutmut_4': x_power__mutmut_4, 
    'x_power__mutmut_5': x_power__mutmut_5, 
    'x_power__mutmut_6': x_power__mutmut_6, 
    'x_power__mutmut_7': x_power__mutmut_7, 
    'x_power__mutmut_8': x_power__mutmut_8, 
    'x_power__mutmut_9': x_power__mutmut_9, 
    'x_power__mutmut_10': x_power__mutmut_10
}

def power(*args, **kwargs):
    result = _mutmut_trampoline(x_power__mutmut_orig, x_power__mutmut_mutants, args, kwargs)
    return result 

power.__signature__ = _mutmut_signature(x_power__mutmut_orig)
x_power__mutmut_orig.__name__ = 'x_power'