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
def x_euc_Dist__mutmut_orig(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_1(array1, array2):
    Sum = None
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_2(array1, array2):
    Sum = 1.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_3(array1, array2):
    Sum = 0.0
    for i in range(None):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_4(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum = (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_5(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum -= (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_6(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) * 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_7(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] + array2[i]) ** 2.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_8(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 3.0
    return Sum ** 0.5
def x_euc_Dist__mutmut_9(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum * 0.5
def x_euc_Dist__mutmut_10(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 1.5

x_euc_Dist__mutmut_mutants : ClassVar[MutantDict] = {
'x_euc_Dist__mutmut_1': x_euc_Dist__mutmut_1, 
    'x_euc_Dist__mutmut_2': x_euc_Dist__mutmut_2, 
    'x_euc_Dist__mutmut_3': x_euc_Dist__mutmut_3, 
    'x_euc_Dist__mutmut_4': x_euc_Dist__mutmut_4, 
    'x_euc_Dist__mutmut_5': x_euc_Dist__mutmut_5, 
    'x_euc_Dist__mutmut_6': x_euc_Dist__mutmut_6, 
    'x_euc_Dist__mutmut_7': x_euc_Dist__mutmut_7, 
    'x_euc_Dist__mutmut_8': x_euc_Dist__mutmut_8, 
    'x_euc_Dist__mutmut_9': x_euc_Dist__mutmut_9, 
    'x_euc_Dist__mutmut_10': x_euc_Dist__mutmut_10
}

def euc_Dist(*args, **kwargs):
    result = _mutmut_trampoline(x_euc_Dist__mutmut_orig, x_euc_Dist__mutmut_mutants, args, kwargs)
    return result 

euc_Dist.__signature__ = _mutmut_signature(x_euc_Dist__mutmut_orig)
x_euc_Dist__mutmut_orig.__name__ = 'x_euc_Dist'