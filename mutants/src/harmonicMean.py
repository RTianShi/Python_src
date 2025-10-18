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
def x_harmonicMean__mutmut_orig(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_1(data):
    sumOfInversions = None
    for i in range(0, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_2(data):
    sumOfInversions = 1
    for i in range(0, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_3(data):
    sumOfInversions = 0
    for i in range(None, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_4(data):
    sumOfInversions = 0
    for i in range(0, None):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_5(data):
    sumOfInversions = 0
    for i in range(len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_6(data):
    sumOfInversions = 0
    for i in range(0, ):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_7(data):
    sumOfInversions = 0
    for i in range(1, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_8(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions = 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_9(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions -= 1 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_10(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions += 1 * data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_11(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions += 2 / data[i]

    return len(data) / sumOfInversions
def x_harmonicMean__mutmut_12(data):
    sumOfInversions = 0
    for i in range(0, len(data)):
        sumOfInversions += 1 / data[i]

    return len(data) * sumOfInversions

x_harmonicMean__mutmut_mutants : ClassVar[MutantDict] = {
'x_harmonicMean__mutmut_1': x_harmonicMean__mutmut_1, 
    'x_harmonicMean__mutmut_2': x_harmonicMean__mutmut_2, 
    'x_harmonicMean__mutmut_3': x_harmonicMean__mutmut_3, 
    'x_harmonicMean__mutmut_4': x_harmonicMean__mutmut_4, 
    'x_harmonicMean__mutmut_5': x_harmonicMean__mutmut_5, 
    'x_harmonicMean__mutmut_6': x_harmonicMean__mutmut_6, 
    'x_harmonicMean__mutmut_7': x_harmonicMean__mutmut_7, 
    'x_harmonicMean__mutmut_8': x_harmonicMean__mutmut_8, 
    'x_harmonicMean__mutmut_9': x_harmonicMean__mutmut_9, 
    'x_harmonicMean__mutmut_10': x_harmonicMean__mutmut_10, 
    'x_harmonicMean__mutmut_11': x_harmonicMean__mutmut_11, 
    'x_harmonicMean__mutmut_12': x_harmonicMean__mutmut_12
}

def harmonicMean(*args, **kwargs):
    result = _mutmut_trampoline(x_harmonicMean__mutmut_orig, x_harmonicMean__mutmut_mutants, args, kwargs)
    return result 

harmonicMean.__signature__ = _mutmut_signature(x_harmonicMean__mutmut_orig)
x_harmonicMean__mutmut_orig.__name__ = 'x_harmonicMean'


