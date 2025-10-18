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
def x_find_median__mutmut_orig(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_1(a):
    k = None
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_2(a):
    k = len(a) / 2 - 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_3(a):
    k = len(a) * 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_4(a):
    k = len(a) / 3 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_5(a):
    k = len(a) / 2 + 2
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_6(a):
    k = len(a) / 2 + 1
    minIndex = None
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_7(a):
    k = len(a) / 2 + 1
    minIndex = 1
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_8(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = None
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_9(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[1]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_10(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(None, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_11(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, None):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_12(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_13(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, ):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_14(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(1, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_15(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = None
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_16(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = None

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_17(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(None, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_18(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, None):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_19(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_20(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, ):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_21(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i - 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_22(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 2, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_23(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] <= minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_24(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = None
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_25(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = None

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_26(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = None
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_27(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = None
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_28(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = None
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_29(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) / 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_30(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 3 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_31(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 != 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_32(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 1:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_33(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) * 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_34(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] - a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_35(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 + 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_36(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) * 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_37(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 3 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_38(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 2)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_39(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) * 2]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_40(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 3]) / 2
    else:
        return a[len(a)/2]
def x_find_median__mutmut_41(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 3
    else:
        return a[len(a)/2]
def x_find_median__mutmut_42(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a) * 2]
def x_find_median__mutmut_43(a):
    k = len(a) / 2 + 1
    minIndex = 0
    minValue = a[0]
    for i in range(0, k):
        minIndex = i
        minValue = a[i]

        for j in range(i + 1, len(a)):
            if a[j] < minValue:
                minIndex = j
                minValue = a[j]

        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp
    if len(a) % 2 == 0:
        return (a[(len(a) / 2 - 1)] + a[len(a) / 2]) / 2
    else:
        return a[len(a)/3]

x_find_median__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_median__mutmut_1': x_find_median__mutmut_1, 
    'x_find_median__mutmut_2': x_find_median__mutmut_2, 
    'x_find_median__mutmut_3': x_find_median__mutmut_3, 
    'x_find_median__mutmut_4': x_find_median__mutmut_4, 
    'x_find_median__mutmut_5': x_find_median__mutmut_5, 
    'x_find_median__mutmut_6': x_find_median__mutmut_6, 
    'x_find_median__mutmut_7': x_find_median__mutmut_7, 
    'x_find_median__mutmut_8': x_find_median__mutmut_8, 
    'x_find_median__mutmut_9': x_find_median__mutmut_9, 
    'x_find_median__mutmut_10': x_find_median__mutmut_10, 
    'x_find_median__mutmut_11': x_find_median__mutmut_11, 
    'x_find_median__mutmut_12': x_find_median__mutmut_12, 
    'x_find_median__mutmut_13': x_find_median__mutmut_13, 
    'x_find_median__mutmut_14': x_find_median__mutmut_14, 
    'x_find_median__mutmut_15': x_find_median__mutmut_15, 
    'x_find_median__mutmut_16': x_find_median__mutmut_16, 
    'x_find_median__mutmut_17': x_find_median__mutmut_17, 
    'x_find_median__mutmut_18': x_find_median__mutmut_18, 
    'x_find_median__mutmut_19': x_find_median__mutmut_19, 
    'x_find_median__mutmut_20': x_find_median__mutmut_20, 
    'x_find_median__mutmut_21': x_find_median__mutmut_21, 
    'x_find_median__mutmut_22': x_find_median__mutmut_22, 
    'x_find_median__mutmut_23': x_find_median__mutmut_23, 
    'x_find_median__mutmut_24': x_find_median__mutmut_24, 
    'x_find_median__mutmut_25': x_find_median__mutmut_25, 
    'x_find_median__mutmut_26': x_find_median__mutmut_26, 
    'x_find_median__mutmut_27': x_find_median__mutmut_27, 
    'x_find_median__mutmut_28': x_find_median__mutmut_28, 
    'x_find_median__mutmut_29': x_find_median__mutmut_29, 
    'x_find_median__mutmut_30': x_find_median__mutmut_30, 
    'x_find_median__mutmut_31': x_find_median__mutmut_31, 
    'x_find_median__mutmut_32': x_find_median__mutmut_32, 
    'x_find_median__mutmut_33': x_find_median__mutmut_33, 
    'x_find_median__mutmut_34': x_find_median__mutmut_34, 
    'x_find_median__mutmut_35': x_find_median__mutmut_35, 
    'x_find_median__mutmut_36': x_find_median__mutmut_36, 
    'x_find_median__mutmut_37': x_find_median__mutmut_37, 
    'x_find_median__mutmut_38': x_find_median__mutmut_38, 
    'x_find_median__mutmut_39': x_find_median__mutmut_39, 
    'x_find_median__mutmut_40': x_find_median__mutmut_40, 
    'x_find_median__mutmut_41': x_find_median__mutmut_41, 
    'x_find_median__mutmut_42': x_find_median__mutmut_42, 
    'x_find_median__mutmut_43': x_find_median__mutmut_43
}

def find_median(*args, **kwargs):
    result = _mutmut_trampoline(x_find_median__mutmut_orig, x_find_median__mutmut_mutants, args, kwargs)
    return result 

find_median.__signature__ = _mutmut_signature(x_find_median__mutmut_orig)
x_find_median__mutmut_orig.__name__ = 'x_find_median'
