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
def x_partition__mutmut_orig(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_1(work, begin, end, pivot):

    value = None
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_2(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = None

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_3(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = None
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_4(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin - 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_5(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 2
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_6(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = None

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_7(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end + 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_8(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 2

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_9(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i <= j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_10(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j or work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_11(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i <= j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_12(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] >= value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_13(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j = 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_14(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j += 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_15(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 2
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_16(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j or work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_17(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i <= j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_18(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] <= value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_19(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i = 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_20(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i -= 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_21(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 2

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_22(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i <= j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_23(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = None
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_24(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = None
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_25(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i - 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_26(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 2] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_27(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = None

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_28(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j + 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_29(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 2] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_30(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end and work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_31(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i > end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_32(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] >= value:
        i -= 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_33(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i = 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_34(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i += 1

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_35(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 2

    work[begin] = work[i]
    work[i] = value

    return i
def x_partition__mutmut_36(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = None
    work[i] = value

    return i
def x_partition__mutmut_37(work, begin, end, pivot):

    value = work[pivot]
    work[pivot] = work[begin]

    i = begin + 1
    j = end - 1

    while i < j:
        while i < j and work[j] > value:
            j -= 1
        while i < j and work[i] < value:
            i += 1

        if i < j:
            tmp = work[i]
            work[i + 1] = work[j]
            work[j - 1] = tmp

    if i >= end or work[i] > value:
        i -= 1

    work[begin] = work[i]
    work[i] = None

    return i

x_partition__mutmut_mutants : ClassVar[MutantDict] = {
'x_partition__mutmut_1': x_partition__mutmut_1, 
    'x_partition__mutmut_2': x_partition__mutmut_2, 
    'x_partition__mutmut_3': x_partition__mutmut_3, 
    'x_partition__mutmut_4': x_partition__mutmut_4, 
    'x_partition__mutmut_5': x_partition__mutmut_5, 
    'x_partition__mutmut_6': x_partition__mutmut_6, 
    'x_partition__mutmut_7': x_partition__mutmut_7, 
    'x_partition__mutmut_8': x_partition__mutmut_8, 
    'x_partition__mutmut_9': x_partition__mutmut_9, 
    'x_partition__mutmut_10': x_partition__mutmut_10, 
    'x_partition__mutmut_11': x_partition__mutmut_11, 
    'x_partition__mutmut_12': x_partition__mutmut_12, 
    'x_partition__mutmut_13': x_partition__mutmut_13, 
    'x_partition__mutmut_14': x_partition__mutmut_14, 
    'x_partition__mutmut_15': x_partition__mutmut_15, 
    'x_partition__mutmut_16': x_partition__mutmut_16, 
    'x_partition__mutmut_17': x_partition__mutmut_17, 
    'x_partition__mutmut_18': x_partition__mutmut_18, 
    'x_partition__mutmut_19': x_partition__mutmut_19, 
    'x_partition__mutmut_20': x_partition__mutmut_20, 
    'x_partition__mutmut_21': x_partition__mutmut_21, 
    'x_partition__mutmut_22': x_partition__mutmut_22, 
    'x_partition__mutmut_23': x_partition__mutmut_23, 
    'x_partition__mutmut_24': x_partition__mutmut_24, 
    'x_partition__mutmut_25': x_partition__mutmut_25, 
    'x_partition__mutmut_26': x_partition__mutmut_26, 
    'x_partition__mutmut_27': x_partition__mutmut_27, 
    'x_partition__mutmut_28': x_partition__mutmut_28, 
    'x_partition__mutmut_29': x_partition__mutmut_29, 
    'x_partition__mutmut_30': x_partition__mutmut_30, 
    'x_partition__mutmut_31': x_partition__mutmut_31, 
    'x_partition__mutmut_32': x_partition__mutmut_32, 
    'x_partition__mutmut_33': x_partition__mutmut_33, 
    'x_partition__mutmut_34': x_partition__mutmut_34, 
    'x_partition__mutmut_35': x_partition__mutmut_35, 
    'x_partition__mutmut_36': x_partition__mutmut_36, 
    'x_partition__mutmut_37': x_partition__mutmut_37
}

def partition(*args, **kwargs):
    result = _mutmut_trampoline(x_partition__mutmut_orig, x_partition__mutmut_mutants, args, kwargs)
    return result 

partition.__signature__ = _mutmut_signature(x_partition__mutmut_orig)
x_partition__mutmut_orig.__name__ = 'x_partition'
