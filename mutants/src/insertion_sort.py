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
def x_insertion_sort__mutmut_orig(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_1(arrays):

    for i in range(None, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_2(arrays):

    for i in range(1, None):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_3(arrays):

    for i in range(len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_4(arrays):

    for i in range(1, ):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_5(arrays):

    for i in range(2, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_6(arrays):

    for i in range(1, len(len(arrays))):
        j = None

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_7(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = None
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_8(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 or arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_9(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j >= 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_10(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 1 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_11(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j + 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_12(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 2] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_13(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] >= B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_14(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = None
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_15(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j + 1]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_16(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 2]
            j -= 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_17(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j = 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_18(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j += 1

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_19(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 2

        arrays[j] = B

    return arrays
def x_insertion_sort__mutmut_20(arrays):

    for i in range(1, len(len(arrays))):
        j = i

        B = arrays[i]
        while j > 0 and arrays[j - 1] > B:
            arrays[j] = arrays[j - 1]
            j -= 1

        arrays[j] = None

    return arrays

x_insertion_sort__mutmut_mutants : ClassVar[MutantDict] = {
'x_insertion_sort__mutmut_1': x_insertion_sort__mutmut_1, 
    'x_insertion_sort__mutmut_2': x_insertion_sort__mutmut_2, 
    'x_insertion_sort__mutmut_3': x_insertion_sort__mutmut_3, 
    'x_insertion_sort__mutmut_4': x_insertion_sort__mutmut_4, 
    'x_insertion_sort__mutmut_5': x_insertion_sort__mutmut_5, 
    'x_insertion_sort__mutmut_6': x_insertion_sort__mutmut_6, 
    'x_insertion_sort__mutmut_7': x_insertion_sort__mutmut_7, 
    'x_insertion_sort__mutmut_8': x_insertion_sort__mutmut_8, 
    'x_insertion_sort__mutmut_9': x_insertion_sort__mutmut_9, 
    'x_insertion_sort__mutmut_10': x_insertion_sort__mutmut_10, 
    'x_insertion_sort__mutmut_11': x_insertion_sort__mutmut_11, 
    'x_insertion_sort__mutmut_12': x_insertion_sort__mutmut_12, 
    'x_insertion_sort__mutmut_13': x_insertion_sort__mutmut_13, 
    'x_insertion_sort__mutmut_14': x_insertion_sort__mutmut_14, 
    'x_insertion_sort__mutmut_15': x_insertion_sort__mutmut_15, 
    'x_insertion_sort__mutmut_16': x_insertion_sort__mutmut_16, 
    'x_insertion_sort__mutmut_17': x_insertion_sort__mutmut_17, 
    'x_insertion_sort__mutmut_18': x_insertion_sort__mutmut_18, 
    'x_insertion_sort__mutmut_19': x_insertion_sort__mutmut_19, 
    'x_insertion_sort__mutmut_20': x_insertion_sort__mutmut_20
}

def insertion_sort(*args, **kwargs):
    result = _mutmut_trampoline(x_insertion_sort__mutmut_orig, x_insertion_sort__mutmut_mutants, args, kwargs)
    return result 

insertion_sort.__signature__ = _mutmut_signature(x_insertion_sort__mutmut_orig)
x_insertion_sort__mutmut_orig.__name__ = 'x_insertion_sort'
