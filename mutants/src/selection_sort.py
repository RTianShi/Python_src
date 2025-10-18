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
def x_selection_sort__mutmut_orig(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_1(list1):

    for i in range(None, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_2(list1):

    for i in range(0, None):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_3(list1):

    for i in range(len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_4(list1):

    for i in range(0, ):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_5(list1):

    for i in range(1, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_6(list1):

    for i in range(0, len(list1)):
        min1 = None
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_7(list1):

    for i in range(0, len(list1)):
        min1 = 2
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_8(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(None, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_9(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, None):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_10(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_11(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, ):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_12(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i - 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_13(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 2, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_14(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] <= list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_15(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = None

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_16(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = None
        list1[i] = list1[min1]
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_17(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = None
        list1[min1] = tmp

    return list1
def x_selection_sort__mutmut_18(list1):

    for i in range(0, len(list1)):
        min1 = 1
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min1]:
                min1 = j

        tmp = list1[i]
        list1[i] = list1[min1]
        list1[min1] = None

    return list1

x_selection_sort__mutmut_mutants : ClassVar[MutantDict] = {
'x_selection_sort__mutmut_1': x_selection_sort__mutmut_1, 
    'x_selection_sort__mutmut_2': x_selection_sort__mutmut_2, 
    'x_selection_sort__mutmut_3': x_selection_sort__mutmut_3, 
    'x_selection_sort__mutmut_4': x_selection_sort__mutmut_4, 
    'x_selection_sort__mutmut_5': x_selection_sort__mutmut_5, 
    'x_selection_sort__mutmut_6': x_selection_sort__mutmut_6, 
    'x_selection_sort__mutmut_7': x_selection_sort__mutmut_7, 
    'x_selection_sort__mutmut_8': x_selection_sort__mutmut_8, 
    'x_selection_sort__mutmut_9': x_selection_sort__mutmut_9, 
    'x_selection_sort__mutmut_10': x_selection_sort__mutmut_10, 
    'x_selection_sort__mutmut_11': x_selection_sort__mutmut_11, 
    'x_selection_sort__mutmut_12': x_selection_sort__mutmut_12, 
    'x_selection_sort__mutmut_13': x_selection_sort__mutmut_13, 
    'x_selection_sort__mutmut_14': x_selection_sort__mutmut_14, 
    'x_selection_sort__mutmut_15': x_selection_sort__mutmut_15, 
    'x_selection_sort__mutmut_16': x_selection_sort__mutmut_16, 
    'x_selection_sort__mutmut_17': x_selection_sort__mutmut_17, 
    'x_selection_sort__mutmut_18': x_selection_sort__mutmut_18
}

def selection_sort(*args, **kwargs):
    result = _mutmut_trampoline(x_selection_sort__mutmut_orig, x_selection_sort__mutmut_mutants, args, kwargs)
    return result 

selection_sort.__signature__ = _mutmut_signature(x_selection_sort__mutmut_orig)
x_selection_sort__mutmut_orig.__name__ = 'x_selection_sort'
