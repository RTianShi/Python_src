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
def x_chiSquare__mutmut_orig(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_1(expected, observed):
    sumExpected = None
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_2(expected, observed):
    sumExpected = 1
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_3(expected, observed):
    sumExpected = 0
    sumObserved = None

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_4(expected, observed):
    sumExpected = 0
    sumObserved = 1

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_5(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(None, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_6(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, None):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_7(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_8(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, ):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_9(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(1, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_10(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected = expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_11(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected -= expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_12(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved = observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_13(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved -= observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_14(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = None
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_15(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 2
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_16(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = None

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_17(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = True

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_18(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(None) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_19(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected + sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_20(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) >= 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_21(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 1.00001:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_22(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = None
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_23(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved * sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_24(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = None

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_25(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = False

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_26(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = None

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_27(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 1

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_28(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(None, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_29(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, None):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_30(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_31(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, ):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_32(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(1, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_33(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = None
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_34(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] + (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_35(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio / expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_36(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq = (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_37(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq -= (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_38(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) * (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_39(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev / dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_40(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio / expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_41(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = None
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_42(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] + expected[i]
            sumSq += dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_43(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq = dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_44(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq -= dev * dev / expected[i]

    return sumSq
def x_chiSquare__mutmut_45(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev * dev * expected[i]

    return sumSq
def x_chiSquare__mutmut_46(expected, observed):
    sumExpected = 0
    sumObserved = 0

    for i in range(0, len(observed)):
        sumExpected += expected[i]
        sumObserved += observed[i]

    ratio = 1
    rescale = False

    if abs(sumExpected - sumObserved) > 10E-6:
        ratio = sumObserved / sumExpected
        rescale = True

    sumSq = 0

    for i in range(0, len(observed)):
        if rescale:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev * dev) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += dev / dev / expected[i]

    return sumSq

x_chiSquare__mutmut_mutants : ClassVar[MutantDict] = {
'x_chiSquare__mutmut_1': x_chiSquare__mutmut_1, 
    'x_chiSquare__mutmut_2': x_chiSquare__mutmut_2, 
    'x_chiSquare__mutmut_3': x_chiSquare__mutmut_3, 
    'x_chiSquare__mutmut_4': x_chiSquare__mutmut_4, 
    'x_chiSquare__mutmut_5': x_chiSquare__mutmut_5, 
    'x_chiSquare__mutmut_6': x_chiSquare__mutmut_6, 
    'x_chiSquare__mutmut_7': x_chiSquare__mutmut_7, 
    'x_chiSquare__mutmut_8': x_chiSquare__mutmut_8, 
    'x_chiSquare__mutmut_9': x_chiSquare__mutmut_9, 
    'x_chiSquare__mutmut_10': x_chiSquare__mutmut_10, 
    'x_chiSquare__mutmut_11': x_chiSquare__mutmut_11, 
    'x_chiSquare__mutmut_12': x_chiSquare__mutmut_12, 
    'x_chiSquare__mutmut_13': x_chiSquare__mutmut_13, 
    'x_chiSquare__mutmut_14': x_chiSquare__mutmut_14, 
    'x_chiSquare__mutmut_15': x_chiSquare__mutmut_15, 
    'x_chiSquare__mutmut_16': x_chiSquare__mutmut_16, 
    'x_chiSquare__mutmut_17': x_chiSquare__mutmut_17, 
    'x_chiSquare__mutmut_18': x_chiSquare__mutmut_18, 
    'x_chiSquare__mutmut_19': x_chiSquare__mutmut_19, 
    'x_chiSquare__mutmut_20': x_chiSquare__mutmut_20, 
    'x_chiSquare__mutmut_21': x_chiSquare__mutmut_21, 
    'x_chiSquare__mutmut_22': x_chiSquare__mutmut_22, 
    'x_chiSquare__mutmut_23': x_chiSquare__mutmut_23, 
    'x_chiSquare__mutmut_24': x_chiSquare__mutmut_24, 
    'x_chiSquare__mutmut_25': x_chiSquare__mutmut_25, 
    'x_chiSquare__mutmut_26': x_chiSquare__mutmut_26, 
    'x_chiSquare__mutmut_27': x_chiSquare__mutmut_27, 
    'x_chiSquare__mutmut_28': x_chiSquare__mutmut_28, 
    'x_chiSquare__mutmut_29': x_chiSquare__mutmut_29, 
    'x_chiSquare__mutmut_30': x_chiSquare__mutmut_30, 
    'x_chiSquare__mutmut_31': x_chiSquare__mutmut_31, 
    'x_chiSquare__mutmut_32': x_chiSquare__mutmut_32, 
    'x_chiSquare__mutmut_33': x_chiSquare__mutmut_33, 
    'x_chiSquare__mutmut_34': x_chiSquare__mutmut_34, 
    'x_chiSquare__mutmut_35': x_chiSquare__mutmut_35, 
    'x_chiSquare__mutmut_36': x_chiSquare__mutmut_36, 
    'x_chiSquare__mutmut_37': x_chiSquare__mutmut_37, 
    'x_chiSquare__mutmut_38': x_chiSquare__mutmut_38, 
    'x_chiSquare__mutmut_39': x_chiSquare__mutmut_39, 
    'x_chiSquare__mutmut_40': x_chiSquare__mutmut_40, 
    'x_chiSquare__mutmut_41': x_chiSquare__mutmut_41, 
    'x_chiSquare__mutmut_42': x_chiSquare__mutmut_42, 
    'x_chiSquare__mutmut_43': x_chiSquare__mutmut_43, 
    'x_chiSquare__mutmut_44': x_chiSquare__mutmut_44, 
    'x_chiSquare__mutmut_45': x_chiSquare__mutmut_45, 
    'x_chiSquare__mutmut_46': x_chiSquare__mutmut_46
}

def chiSquare(*args, **kwargs):
    result = _mutmut_trampoline(x_chiSquare__mutmut_orig, x_chiSquare__mutmut_mutants, args, kwargs)
    return result 

chiSquare.__signature__ = _mutmut_signature(x_chiSquare__mutmut_orig)
x_chiSquare__mutmut_orig.__name__ = 'x_chiSquare'
