import numpy as np
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


def x_cosineDistance__mutmut_orig(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_1(p1, p2):
    dotProduct = None
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_2(p1, p2):
    dotProduct = 1
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_3(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = None
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_4(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 1
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_5(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = None

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_6(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 1

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_7(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(None, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_8(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, None):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_9(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_10(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, ):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_11(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(1, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_12(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 = p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_13(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 -= p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_14(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] / p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_15(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 = p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_16(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 -= p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_17(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] / p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_18(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct = p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_19(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct -= p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_20(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] / p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_21(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = None

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_22(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) / np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_23(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(None) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_24(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(None)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_25(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator <= dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_26(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = None

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_27(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 or dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_28(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator != 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_29(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 1 and dotProduct == 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_30(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct != 0:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_31(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 1:
        return 0

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_32(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 1

    return 1 - dotProduct / denominator


def x_cosineDistance__mutmut_33(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 + dotProduct / denominator


def x_cosineDistance__mutmut_34(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 2 - dotProduct / denominator


def x_cosineDistance__mutmut_35(p1, p2):
    dotProduct = 0
    lengthSquaredp1 = 0
    lengthSquaredp2 = 0

    for i in range(0, len(p1)):
        lengthSquaredp1 += p1[i] * p1[i]
        lengthSquaredp2 += p2[i] * p2[i]
        dotProduct += p1[i] * p2[i]

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator < dotProduct:
        denominator = dotProduct

    if denominator == 0 and dotProduct == 0:
        return 0

    return 1 - dotProduct * denominator

x_cosineDistance__mutmut_mutants : ClassVar[MutantDict] = {
'x_cosineDistance__mutmut_1': x_cosineDistance__mutmut_1, 
    'x_cosineDistance__mutmut_2': x_cosineDistance__mutmut_2, 
    'x_cosineDistance__mutmut_3': x_cosineDistance__mutmut_3, 
    'x_cosineDistance__mutmut_4': x_cosineDistance__mutmut_4, 
    'x_cosineDistance__mutmut_5': x_cosineDistance__mutmut_5, 
    'x_cosineDistance__mutmut_6': x_cosineDistance__mutmut_6, 
    'x_cosineDistance__mutmut_7': x_cosineDistance__mutmut_7, 
    'x_cosineDistance__mutmut_8': x_cosineDistance__mutmut_8, 
    'x_cosineDistance__mutmut_9': x_cosineDistance__mutmut_9, 
    'x_cosineDistance__mutmut_10': x_cosineDistance__mutmut_10, 
    'x_cosineDistance__mutmut_11': x_cosineDistance__mutmut_11, 
    'x_cosineDistance__mutmut_12': x_cosineDistance__mutmut_12, 
    'x_cosineDistance__mutmut_13': x_cosineDistance__mutmut_13, 
    'x_cosineDistance__mutmut_14': x_cosineDistance__mutmut_14, 
    'x_cosineDistance__mutmut_15': x_cosineDistance__mutmut_15, 
    'x_cosineDistance__mutmut_16': x_cosineDistance__mutmut_16, 
    'x_cosineDistance__mutmut_17': x_cosineDistance__mutmut_17, 
    'x_cosineDistance__mutmut_18': x_cosineDistance__mutmut_18, 
    'x_cosineDistance__mutmut_19': x_cosineDistance__mutmut_19, 
    'x_cosineDistance__mutmut_20': x_cosineDistance__mutmut_20, 
    'x_cosineDistance__mutmut_21': x_cosineDistance__mutmut_21, 
    'x_cosineDistance__mutmut_22': x_cosineDistance__mutmut_22, 
    'x_cosineDistance__mutmut_23': x_cosineDistance__mutmut_23, 
    'x_cosineDistance__mutmut_24': x_cosineDistance__mutmut_24, 
    'x_cosineDistance__mutmut_25': x_cosineDistance__mutmut_25, 
    'x_cosineDistance__mutmut_26': x_cosineDistance__mutmut_26, 
    'x_cosineDistance__mutmut_27': x_cosineDistance__mutmut_27, 
    'x_cosineDistance__mutmut_28': x_cosineDistance__mutmut_28, 
    'x_cosineDistance__mutmut_29': x_cosineDistance__mutmut_29, 
    'x_cosineDistance__mutmut_30': x_cosineDistance__mutmut_30, 
    'x_cosineDistance__mutmut_31': x_cosineDistance__mutmut_31, 
    'x_cosineDistance__mutmut_32': x_cosineDistance__mutmut_32, 
    'x_cosineDistance__mutmut_33': x_cosineDistance__mutmut_33, 
    'x_cosineDistance__mutmut_34': x_cosineDistance__mutmut_34, 
    'x_cosineDistance__mutmut_35': x_cosineDistance__mutmut_35
}

def cosineDistance(*args, **kwargs):
    result = _mutmut_trampoline(x_cosineDistance__mutmut_orig, x_cosineDistance__mutmut_mutants, args, kwargs)
    return result 

cosineDistance.__signature__ = _mutmut_signature(x_cosineDistance__mutmut_orig)
x_cosineDistance__mutmut_orig.__name__ = 'x_cosineDistance'
