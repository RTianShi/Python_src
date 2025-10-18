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
def x_evaluateHoners__mutmut_orig(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_1(coefficients, argument):
    n = None
    result = []

    for i in range( n-2, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_2(coefficients, argument):
    n = len(coefficients)
    result = None

    for i in range( n-2, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_3(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( None, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_4(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, None, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_5(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, None):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_6(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_7(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_8(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, ):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_9(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n + 2, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_10(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-3, -1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_11(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, +1, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_12(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -2, -1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_13(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, +1):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_14(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -2):
        result = argument * result + coefficients[i]

    return result
def x_evaluateHoners__mutmut_15(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -1):
        result = None

    return result
def x_evaluateHoners__mutmut_16(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -1):
        result = argument * result - coefficients[i]

    return result
def x_evaluateHoners__mutmut_17(coefficients, argument):
    n = len(coefficients)
    result = []

    for i in range( n-2, -1, -1):
        result = argument / result + coefficients[i]

    return result

x_evaluateHoners__mutmut_mutants : ClassVar[MutantDict] = {
'x_evaluateHoners__mutmut_1': x_evaluateHoners__mutmut_1, 
    'x_evaluateHoners__mutmut_2': x_evaluateHoners__mutmut_2, 
    'x_evaluateHoners__mutmut_3': x_evaluateHoners__mutmut_3, 
    'x_evaluateHoners__mutmut_4': x_evaluateHoners__mutmut_4, 
    'x_evaluateHoners__mutmut_5': x_evaluateHoners__mutmut_5, 
    'x_evaluateHoners__mutmut_6': x_evaluateHoners__mutmut_6, 
    'x_evaluateHoners__mutmut_7': x_evaluateHoners__mutmut_7, 
    'x_evaluateHoners__mutmut_8': x_evaluateHoners__mutmut_8, 
    'x_evaluateHoners__mutmut_9': x_evaluateHoners__mutmut_9, 
    'x_evaluateHoners__mutmut_10': x_evaluateHoners__mutmut_10, 
    'x_evaluateHoners__mutmut_11': x_evaluateHoners__mutmut_11, 
    'x_evaluateHoners__mutmut_12': x_evaluateHoners__mutmut_12, 
    'x_evaluateHoners__mutmut_13': x_evaluateHoners__mutmut_13, 
    'x_evaluateHoners__mutmut_14': x_evaluateHoners__mutmut_14, 
    'x_evaluateHoners__mutmut_15': x_evaluateHoners__mutmut_15, 
    'x_evaluateHoners__mutmut_16': x_evaluateHoners__mutmut_16, 
    'x_evaluateHoners__mutmut_17': x_evaluateHoners__mutmut_17
}

def evaluateHoners(*args, **kwargs):
    result = _mutmut_trampoline(x_evaluateHoners__mutmut_orig, x_evaluateHoners__mutmut_mutants, args, kwargs)
    return result 

evaluateHoners.__signature__ = _mutmut_signature(x_evaluateHoners__mutmut_orig)
x_evaluateHoners__mutmut_orig.__name__ = 'x_evaluateHoners'
