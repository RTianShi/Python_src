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
def x_shell_sort__mutmut_orig(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_1(arr):

    n = None
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_2(arr):

    n = len(arr)
    gap = None

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_3(arr):

    n = len(arr)
    gap = n * 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_4(arr):

    n = len(arr)
    gap = n / 3

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_5(arr):

    n = len(arr)
    gap = n / 2

    while gap >= 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_6(arr):

    n = len(arr)
    gap = n / 2

    while gap > 1:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_7(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(None, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_8(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, None):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_9(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_10(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, ):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_11(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = None
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_12(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = None
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_13(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap or arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_14(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j > gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_15(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j + gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_16(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] >= temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_17(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = None
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_18(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j + gap]
                j -= gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_19(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_20(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j += gap
            arr[j] = temp
        gap /= 2

    return arr
def x_shell_sort__mutmut_21(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = None
        gap /= 2

    return arr
def x_shell_sort__mutmut_22(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = 2

    return arr
def x_shell_sort__mutmut_23(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap *= 2

    return arr
def x_shell_sort__mutmut_24(arr):

    n = len(arr)
    gap = n / 2

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap /= 3

    return arr

x_shell_sort__mutmut_mutants : ClassVar[MutantDict] = {
'x_shell_sort__mutmut_1': x_shell_sort__mutmut_1, 
    'x_shell_sort__mutmut_2': x_shell_sort__mutmut_2, 
    'x_shell_sort__mutmut_3': x_shell_sort__mutmut_3, 
    'x_shell_sort__mutmut_4': x_shell_sort__mutmut_4, 
    'x_shell_sort__mutmut_5': x_shell_sort__mutmut_5, 
    'x_shell_sort__mutmut_6': x_shell_sort__mutmut_6, 
    'x_shell_sort__mutmut_7': x_shell_sort__mutmut_7, 
    'x_shell_sort__mutmut_8': x_shell_sort__mutmut_8, 
    'x_shell_sort__mutmut_9': x_shell_sort__mutmut_9, 
    'x_shell_sort__mutmut_10': x_shell_sort__mutmut_10, 
    'x_shell_sort__mutmut_11': x_shell_sort__mutmut_11, 
    'x_shell_sort__mutmut_12': x_shell_sort__mutmut_12, 
    'x_shell_sort__mutmut_13': x_shell_sort__mutmut_13, 
    'x_shell_sort__mutmut_14': x_shell_sort__mutmut_14, 
    'x_shell_sort__mutmut_15': x_shell_sort__mutmut_15, 
    'x_shell_sort__mutmut_16': x_shell_sort__mutmut_16, 
    'x_shell_sort__mutmut_17': x_shell_sort__mutmut_17, 
    'x_shell_sort__mutmut_18': x_shell_sort__mutmut_18, 
    'x_shell_sort__mutmut_19': x_shell_sort__mutmut_19, 
    'x_shell_sort__mutmut_20': x_shell_sort__mutmut_20, 
    'x_shell_sort__mutmut_21': x_shell_sort__mutmut_21, 
    'x_shell_sort__mutmut_22': x_shell_sort__mutmut_22, 
    'x_shell_sort__mutmut_23': x_shell_sort__mutmut_23, 
    'x_shell_sort__mutmut_24': x_shell_sort__mutmut_24
}

def shell_sort(*args, **kwargs):
    result = _mutmut_trampoline(x_shell_sort__mutmut_orig, x_shell_sort__mutmut_mutants, args, kwargs)
    return result 

shell_sort.__signature__ = _mutmut_signature(x_shell_sort__mutmut_orig)
x_shell_sort__mutmut_orig.__name__ = 'x_shell_sort'
