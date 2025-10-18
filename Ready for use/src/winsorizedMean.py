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
def x_winsorizedMean__mutmut_orig(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_1(sortedElements, left, rigth):

    N = None
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_2(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = None

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_3(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 1

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_4(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(None, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_5(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, None):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_6(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_7(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, ):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_8(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(1, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_9(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma = sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_10(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma -= sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_11(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = None
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_12(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma * len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_13(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = None

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_14(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(None, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_15(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, None):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_16(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_17(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, ):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_18(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(1, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_19(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean = (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_20(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean -= (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_21(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) * N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_22(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes + sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_23(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = None
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_24(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 + rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_25(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N + 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_26(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 2 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_27(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(None, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_28(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, None):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_29(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_30(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, ):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_31(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(1, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_32(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean = (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_33(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean -= (rigthElement - sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_34(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 - i]) * N

    return mean
def x_winsorizedMean__mutmut_35(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement + sortedElements[N - 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_36(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 1 + i]) / N

    return mean
def x_winsorizedMean__mutmut_37(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N + 1 - i]) / N

    return mean
def x_winsorizedMean__mutmut_38(sortedElements, left, rigth):

    N = len(sortedElements)
    suma = 0

    for i in range(0, len(sortedElements)):
        suma += sortedElements[i]

    mean = suma / len(sortedElements)
    leftElementes = sortedElements[left]

    for i in range(0, left):
        mean += (leftElementes - sortedElements[i]) / N

    rigthElement = sortedElements[N - 1 - rigth]
    for i in range(0, rigth):
        mean += (rigthElement - sortedElements[N - 2 - i]) / N

    return mean

x_winsorizedMean__mutmut_mutants : ClassVar[MutantDict] = {
'x_winsorizedMean__mutmut_1': x_winsorizedMean__mutmut_1, 
    'x_winsorizedMean__mutmut_2': x_winsorizedMean__mutmut_2, 
    'x_winsorizedMean__mutmut_3': x_winsorizedMean__mutmut_3, 
    'x_winsorizedMean__mutmut_4': x_winsorizedMean__mutmut_4, 
    'x_winsorizedMean__mutmut_5': x_winsorizedMean__mutmut_5, 
    'x_winsorizedMean__mutmut_6': x_winsorizedMean__mutmut_6, 
    'x_winsorizedMean__mutmut_7': x_winsorizedMean__mutmut_7, 
    'x_winsorizedMean__mutmut_8': x_winsorizedMean__mutmut_8, 
    'x_winsorizedMean__mutmut_9': x_winsorizedMean__mutmut_9, 
    'x_winsorizedMean__mutmut_10': x_winsorizedMean__mutmut_10, 
    'x_winsorizedMean__mutmut_11': x_winsorizedMean__mutmut_11, 
    'x_winsorizedMean__mutmut_12': x_winsorizedMean__mutmut_12, 
    'x_winsorizedMean__mutmut_13': x_winsorizedMean__mutmut_13, 
    'x_winsorizedMean__mutmut_14': x_winsorizedMean__mutmut_14, 
    'x_winsorizedMean__mutmut_15': x_winsorizedMean__mutmut_15, 
    'x_winsorizedMean__mutmut_16': x_winsorizedMean__mutmut_16, 
    'x_winsorizedMean__mutmut_17': x_winsorizedMean__mutmut_17, 
    'x_winsorizedMean__mutmut_18': x_winsorizedMean__mutmut_18, 
    'x_winsorizedMean__mutmut_19': x_winsorizedMean__mutmut_19, 
    'x_winsorizedMean__mutmut_20': x_winsorizedMean__mutmut_20, 
    'x_winsorizedMean__mutmut_21': x_winsorizedMean__mutmut_21, 
    'x_winsorizedMean__mutmut_22': x_winsorizedMean__mutmut_22, 
    'x_winsorizedMean__mutmut_23': x_winsorizedMean__mutmut_23, 
    'x_winsorizedMean__mutmut_24': x_winsorizedMean__mutmut_24, 
    'x_winsorizedMean__mutmut_25': x_winsorizedMean__mutmut_25, 
    'x_winsorizedMean__mutmut_26': x_winsorizedMean__mutmut_26, 
    'x_winsorizedMean__mutmut_27': x_winsorizedMean__mutmut_27, 
    'x_winsorizedMean__mutmut_28': x_winsorizedMean__mutmut_28, 
    'x_winsorizedMean__mutmut_29': x_winsorizedMean__mutmut_29, 
    'x_winsorizedMean__mutmut_30': x_winsorizedMean__mutmut_30, 
    'x_winsorizedMean__mutmut_31': x_winsorizedMean__mutmut_31, 
    'x_winsorizedMean__mutmut_32': x_winsorizedMean__mutmut_32, 
    'x_winsorizedMean__mutmut_33': x_winsorizedMean__mutmut_33, 
    'x_winsorizedMean__mutmut_34': x_winsorizedMean__mutmut_34, 
    'x_winsorizedMean__mutmut_35': x_winsorizedMean__mutmut_35, 
    'x_winsorizedMean__mutmut_36': x_winsorizedMean__mutmut_36, 
    'x_winsorizedMean__mutmut_37': x_winsorizedMean__mutmut_37, 
    'x_winsorizedMean__mutmut_38': x_winsorizedMean__mutmut_38
}

def winsorizedMean(*args, **kwargs):
    result = _mutmut_trampoline(x_winsorizedMean__mutmut_orig, x_winsorizedMean__mutmut_mutants, args, kwargs)
    return result 

winsorizedMean.__signature__ = _mutmut_signature(x_winsorizedMean__mutmut_orig)
x_winsorizedMean__mutmut_orig.__name__ = 'x_winsorizedMean'
