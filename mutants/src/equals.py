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
def x_equals__mutmut_orig(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_1(x, y):

    if len(x) == len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_2(x, y):

    if len(x) != len(y):
        return True

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_3(x, y):

    if len(x) != len(y):
        return False

    for i in range(None, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_4(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, None):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_5(x, y):

    if len(x) != len(y):
        return False

    for i in range(len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_6(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, ):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_7(x, y):

    if len(x) != len(y):
        return False

    for i in range(1, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_8(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(None) > 0.0001:
            return False

    return True
def x_equals__mutmut_9(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] + x[i]) > 0.0001:
            return False

    return True
def x_equals__mutmut_10(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) >= 0.0001:
            return False

    return True
def x_equals__mutmut_11(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 1.0001:
            return False

    return True
def x_equals__mutmut_12(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return True

    return True
def x_equals__mutmut_13(x, y):

    if len(x) != len(y):
        return False

    for i in range(0, len(x)):
        if abs(y[i] - x[i]) > 0.0001:
            return False

    return False

x_equals__mutmut_mutants : ClassVar[MutantDict] = {
'x_equals__mutmut_1': x_equals__mutmut_1, 
    'x_equals__mutmut_2': x_equals__mutmut_2, 
    'x_equals__mutmut_3': x_equals__mutmut_3, 
    'x_equals__mutmut_4': x_equals__mutmut_4, 
    'x_equals__mutmut_5': x_equals__mutmut_5, 
    'x_equals__mutmut_6': x_equals__mutmut_6, 
    'x_equals__mutmut_7': x_equals__mutmut_7, 
    'x_equals__mutmut_8': x_equals__mutmut_8, 
    'x_equals__mutmut_9': x_equals__mutmut_9, 
    'x_equals__mutmut_10': x_equals__mutmut_10, 
    'x_equals__mutmut_11': x_equals__mutmut_11, 
    'x_equals__mutmut_12': x_equals__mutmut_12, 
    'x_equals__mutmut_13': x_equals__mutmut_13
}

def equals(*args, **kwargs):
    result = _mutmut_trampoline(x_equals__mutmut_orig, x_equals__mutmut_mutants, args, kwargs)
    return result 

equals.__signature__ = _mutmut_signature(x_equals__mutmut_orig)
x_equals__mutmut_orig.__name__ = 'x_equals'
