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
def x_max__mutmut_orig(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_1(elements):
    size = None
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_2(elements):
    size = len(elements)
    mixi = None

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_3(elements):
    size = len(elements)
    mixi = elements[size + 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_4(elements):
    size = len(elements)
    mixi = elements[size - 2]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_5(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(None, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_6(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, None, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_7(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, None):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_8(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(-1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_9(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_10(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, ):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_11(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size + 1, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_12(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 2, -1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_13(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, +1, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_14(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -2, -1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_15(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, +1):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_16(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -2):
        if elements[i] > mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_17(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] >= mixi:
            mixi = elements[i]

    return mixi
def x_max__mutmut_18(elements):
    size = len(elements)
    mixi = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] > mixi:
            mixi = None

    return mixi

x_max__mutmut_mutants : ClassVar[MutantDict] = {
'x_max__mutmut_1': x_max__mutmut_1, 
    'x_max__mutmut_2': x_max__mutmut_2, 
    'x_max__mutmut_3': x_max__mutmut_3, 
    'x_max__mutmut_4': x_max__mutmut_4, 
    'x_max__mutmut_5': x_max__mutmut_5, 
    'x_max__mutmut_6': x_max__mutmut_6, 
    'x_max__mutmut_7': x_max__mutmut_7, 
    'x_max__mutmut_8': x_max__mutmut_8, 
    'x_max__mutmut_9': x_max__mutmut_9, 
    'x_max__mutmut_10': x_max__mutmut_10, 
    'x_max__mutmut_11': x_max__mutmut_11, 
    'x_max__mutmut_12': x_max__mutmut_12, 
    'x_max__mutmut_13': x_max__mutmut_13, 
    'x_max__mutmut_14': x_max__mutmut_14, 
    'x_max__mutmut_15': x_max__mutmut_15, 
    'x_max__mutmut_16': x_max__mutmut_16, 
    'x_max__mutmut_17': x_max__mutmut_17, 
    'x_max__mutmut_18': x_max__mutmut_18
}

def max(*args, **kwargs):
    result = _mutmut_trampoline(x_max__mutmut_orig, x_max__mutmut_mutants, args, kwargs)
    return result 

max.__signature__ = _mutmut_signature(x_max__mutmut_orig)
x_max__mutmut_orig.__name__ = 'x_max'
