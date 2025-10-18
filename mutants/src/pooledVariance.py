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
def x_pooledVariance__mutmut_orig(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_1(data1, data2):

    sum1 = None
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_2(data1, data2):

    sum1 = 1
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_3(data1, data2):

    sum1 = 0
    sumSq1 = None

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_4(data1, data2):

    sum1 = 0
    sumSq1 = 1

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_5(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(None, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_6(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, None):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_7(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_8(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, ):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_9(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(1, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_10(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 = data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_11(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 -= data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_12(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 = data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_13(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 -= data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_14(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] / data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_15(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = None
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_16(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 * len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_17(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = None

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_18(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) * len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_19(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 + mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_20(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 / sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_21(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = None
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_22(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 1
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_23(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = None

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_24(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 1

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_25(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(None, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_26(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, None):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_27(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_28(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, ):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_29(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(1, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_30(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 = data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_31(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 -= data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_32(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 = data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_33(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 -= data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_34(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] / data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_35(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = None
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_36(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 * len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_37(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = None

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_38(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) * len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_39(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 + mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_40(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 / sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_41(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) * (len(data1) + len(data2))
def x_pooledVariance__mutmut_42(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 - len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_43(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) / var1 + len(data2) * var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_44(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) / var2) / (len(data1) + len(data2))
def x_pooledVariance__mutmut_45(data1, data2):

    sum1 = 0
    sumSq1 = 0

    for i in range(0, len(data1)):
        sum1 += data1[i]
        sumSq1 += data1[i] * data1[i]

    mean1 = sum1 / len(data1)
    var1 = (sumSq1 - mean1 * sum1) / len(data1)

    sum2 = 0
    sumSq2 = 0

    for i in range(0, len(data2)):
        sum2 += data2[i]
        sumSq2 += data2[i] * data2[i]

    mean2 = sum2 / len(data2)
    var2 = (sumSq2 - mean2 * sum2) / len(data2)

    return (len(data1) * var1 + len(data2) * var2) / (len(data1) - len(data2))

x_pooledVariance__mutmut_mutants : ClassVar[MutantDict] = {
'x_pooledVariance__mutmut_1': x_pooledVariance__mutmut_1, 
    'x_pooledVariance__mutmut_2': x_pooledVariance__mutmut_2, 
    'x_pooledVariance__mutmut_3': x_pooledVariance__mutmut_3, 
    'x_pooledVariance__mutmut_4': x_pooledVariance__mutmut_4, 
    'x_pooledVariance__mutmut_5': x_pooledVariance__mutmut_5, 
    'x_pooledVariance__mutmut_6': x_pooledVariance__mutmut_6, 
    'x_pooledVariance__mutmut_7': x_pooledVariance__mutmut_7, 
    'x_pooledVariance__mutmut_8': x_pooledVariance__mutmut_8, 
    'x_pooledVariance__mutmut_9': x_pooledVariance__mutmut_9, 
    'x_pooledVariance__mutmut_10': x_pooledVariance__mutmut_10, 
    'x_pooledVariance__mutmut_11': x_pooledVariance__mutmut_11, 
    'x_pooledVariance__mutmut_12': x_pooledVariance__mutmut_12, 
    'x_pooledVariance__mutmut_13': x_pooledVariance__mutmut_13, 
    'x_pooledVariance__mutmut_14': x_pooledVariance__mutmut_14, 
    'x_pooledVariance__mutmut_15': x_pooledVariance__mutmut_15, 
    'x_pooledVariance__mutmut_16': x_pooledVariance__mutmut_16, 
    'x_pooledVariance__mutmut_17': x_pooledVariance__mutmut_17, 
    'x_pooledVariance__mutmut_18': x_pooledVariance__mutmut_18, 
    'x_pooledVariance__mutmut_19': x_pooledVariance__mutmut_19, 
    'x_pooledVariance__mutmut_20': x_pooledVariance__mutmut_20, 
    'x_pooledVariance__mutmut_21': x_pooledVariance__mutmut_21, 
    'x_pooledVariance__mutmut_22': x_pooledVariance__mutmut_22, 
    'x_pooledVariance__mutmut_23': x_pooledVariance__mutmut_23, 
    'x_pooledVariance__mutmut_24': x_pooledVariance__mutmut_24, 
    'x_pooledVariance__mutmut_25': x_pooledVariance__mutmut_25, 
    'x_pooledVariance__mutmut_26': x_pooledVariance__mutmut_26, 
    'x_pooledVariance__mutmut_27': x_pooledVariance__mutmut_27, 
    'x_pooledVariance__mutmut_28': x_pooledVariance__mutmut_28, 
    'x_pooledVariance__mutmut_29': x_pooledVariance__mutmut_29, 
    'x_pooledVariance__mutmut_30': x_pooledVariance__mutmut_30, 
    'x_pooledVariance__mutmut_31': x_pooledVariance__mutmut_31, 
    'x_pooledVariance__mutmut_32': x_pooledVariance__mutmut_32, 
    'x_pooledVariance__mutmut_33': x_pooledVariance__mutmut_33, 
    'x_pooledVariance__mutmut_34': x_pooledVariance__mutmut_34, 
    'x_pooledVariance__mutmut_35': x_pooledVariance__mutmut_35, 
    'x_pooledVariance__mutmut_36': x_pooledVariance__mutmut_36, 
    'x_pooledVariance__mutmut_37': x_pooledVariance__mutmut_37, 
    'x_pooledVariance__mutmut_38': x_pooledVariance__mutmut_38, 
    'x_pooledVariance__mutmut_39': x_pooledVariance__mutmut_39, 
    'x_pooledVariance__mutmut_40': x_pooledVariance__mutmut_40, 
    'x_pooledVariance__mutmut_41': x_pooledVariance__mutmut_41, 
    'x_pooledVariance__mutmut_42': x_pooledVariance__mutmut_42, 
    'x_pooledVariance__mutmut_43': x_pooledVariance__mutmut_43, 
    'x_pooledVariance__mutmut_44': x_pooledVariance__mutmut_44, 
    'x_pooledVariance__mutmut_45': x_pooledVariance__mutmut_45
}

def pooledVariance(*args, **kwargs):
    result = _mutmut_trampoline(x_pooledVariance__mutmut_orig, x_pooledVariance__mutmut_mutants, args, kwargs)
    return result 

pooledVariance.__signature__ = _mutmut_signature(x_pooledVariance__mutmut_orig)
x_pooledVariance__mutmut_orig.__name__ = 'x_pooledVariance'
