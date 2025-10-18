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
def x_manhattanDist2__mutmut_orig(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_1(p1, p2):

    result = None

    for i in range(0, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_2(p1, p2):

    result = 1

    for i in range(0, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_3(p1, p2):

    result = 0

    for i in range(None, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_4(p1, p2):

    result = 0

    for i in range(0, None):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_5(p1, p2):

    result = 0

    for i in range(len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_6(p1, p2):

    result = 0

    for i in range(0, ):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_7(p1, p2):

    result = 0

    for i in range(1, len(p1)):
        result += abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_8(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result = abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_9(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result -= abs(p2[i] - p1[i])

    return result
def x_manhattanDist2__mutmut_10(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result += abs(None)

    return result
def x_manhattanDist2__mutmut_11(p1, p2):

    result = 0

    for i in range(0, len(p1)):
        result += abs(p2[i] + p1[i])

    return result

x_manhattanDist2__mutmut_mutants : ClassVar[MutantDict] = {
'x_manhattanDist2__mutmut_1': x_manhattanDist2__mutmut_1, 
    'x_manhattanDist2__mutmut_2': x_manhattanDist2__mutmut_2, 
    'x_manhattanDist2__mutmut_3': x_manhattanDist2__mutmut_3, 
    'x_manhattanDist2__mutmut_4': x_manhattanDist2__mutmut_4, 
    'x_manhattanDist2__mutmut_5': x_manhattanDist2__mutmut_5, 
    'x_manhattanDist2__mutmut_6': x_manhattanDist2__mutmut_6, 
    'x_manhattanDist2__mutmut_7': x_manhattanDist2__mutmut_7, 
    'x_manhattanDist2__mutmut_8': x_manhattanDist2__mutmut_8, 
    'x_manhattanDist2__mutmut_9': x_manhattanDist2__mutmut_9, 
    'x_manhattanDist2__mutmut_10': x_manhattanDist2__mutmut_10, 
    'x_manhattanDist2__mutmut_11': x_manhattanDist2__mutmut_11
}

def manhattanDist2(*args, **kwargs):
    result = _mutmut_trampoline(x_manhattanDist2__mutmut_orig, x_manhattanDist2__mutmut_mutants, args, kwargs)
    return result 

manhattanDist2.__signature__ = _mutmut_signature(x_manhattanDist2__mutmut_orig)
x_manhattanDist2__mutmut_orig.__name__ = 'x_manhattanDist2'
