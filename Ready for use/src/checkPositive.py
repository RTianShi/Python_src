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
def x_checkPositive__mutmut_orig(n):

    for i in range(0, len(n)):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_1(n):

    for i in range(None, len(n)):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_2(n):

    for i in range(0, None):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_3(n):

    for i in range(len(n)):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_4(n):

    for i in range(0, ):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_5(n):

    for i in range(1, len(n)):
        if n[i] <= 0:
            return False
    return True
def x_checkPositive__mutmut_6(n):

    for i in range(0, len(n)):
        if n[i] < 0:
            return False
    return True
def x_checkPositive__mutmut_7(n):

    for i in range(0, len(n)):
        if n[i] <= 1:
            return False
    return True
def x_checkPositive__mutmut_8(n):

    for i in range(0, len(n)):
        if n[i] <= 0:
            return True
    return True
def x_checkPositive__mutmut_9(n):

    for i in range(0, len(n)):
        if n[i] <= 0:
            return False
    return False

x_checkPositive__mutmut_mutants : ClassVar[MutantDict] = {
'x_checkPositive__mutmut_1': x_checkPositive__mutmut_1, 
    'x_checkPositive__mutmut_2': x_checkPositive__mutmut_2, 
    'x_checkPositive__mutmut_3': x_checkPositive__mutmut_3, 
    'x_checkPositive__mutmut_4': x_checkPositive__mutmut_4, 
    'x_checkPositive__mutmut_5': x_checkPositive__mutmut_5, 
    'x_checkPositive__mutmut_6': x_checkPositive__mutmut_6, 
    'x_checkPositive__mutmut_7': x_checkPositive__mutmut_7, 
    'x_checkPositive__mutmut_8': x_checkPositive__mutmut_8, 
    'x_checkPositive__mutmut_9': x_checkPositive__mutmut_9
}

def checkPositive(*args, **kwargs):
    result = _mutmut_trampoline(x_checkPositive__mutmut_orig, x_checkPositive__mutmut_mutants, args, kwargs)
    return result 

checkPositive.__signature__ = _mutmut_signature(x_checkPositive__mutmut_orig)
x_checkPositive__mutmut_orig.__name__ = 'x_checkPositive'
