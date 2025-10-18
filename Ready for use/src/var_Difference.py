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
def x_var_Difference__mutmut_orig(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_1(sample1, sample2):
    sum1 = None
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_2(sample1, sample2):
    sum1 = 1
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_3(sample1, sample2):
    sum1 = 0
    sum2 = None
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_4(sample1, sample2):
    sum1 = 0
    sum2 = 1
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_5(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = None
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_6(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 1
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_7(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = None
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_8(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = None

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_9(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 1

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_10(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(None, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_11(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, None):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_12(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_13(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, ):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_14(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(1, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_15(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference = sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_16(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference -= sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_17(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] + sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_18(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = None

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_19(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference * n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_20(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(None, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_21(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, None):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_22(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_23(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, ):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_24(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(1, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_25(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = None
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_26(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] + sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_27(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 = (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_28(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 -= (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_29(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) / (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_30(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff + meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_31(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff + meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_32(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 = diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_33(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 -= diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_34(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff + meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_35(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) * (n - 1)
def x_var_Difference__mutmut_36(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 + sum2 * sum2 / n) / (n - 1)
def x_var_Difference__mutmut_37(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 * n) / (n - 1)
def x_var_Difference__mutmut_38(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 / sum2 / n) / (n - 1)
def x_var_Difference__mutmut_39(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n + 1)
def x_var_Difference__mutmut_40(sample1, sample2):
    sum1 = 0
    sum2 = 0
    diff = 0
    n = len(sample1)
    sumDifference = 0

    for i in range(0, n):
        sumDifference += sample1[i] - sample2[i]

    meanDifference = sumDifference / n

    for i in range(0, n):
        diff = sample1[i] - sample2[i]
        sum1 += (diff - meanDifference) * (diff - meanDifference)
        sum2 += diff - meanDifference

    return (sum1 - sum2 * sum2 / n) / (n - 2)

x_var_Difference__mutmut_mutants : ClassVar[MutantDict] = {
'x_var_Difference__mutmut_1': x_var_Difference__mutmut_1, 
    'x_var_Difference__mutmut_2': x_var_Difference__mutmut_2, 
    'x_var_Difference__mutmut_3': x_var_Difference__mutmut_3, 
    'x_var_Difference__mutmut_4': x_var_Difference__mutmut_4, 
    'x_var_Difference__mutmut_5': x_var_Difference__mutmut_5, 
    'x_var_Difference__mutmut_6': x_var_Difference__mutmut_6, 
    'x_var_Difference__mutmut_7': x_var_Difference__mutmut_7, 
    'x_var_Difference__mutmut_8': x_var_Difference__mutmut_8, 
    'x_var_Difference__mutmut_9': x_var_Difference__mutmut_9, 
    'x_var_Difference__mutmut_10': x_var_Difference__mutmut_10, 
    'x_var_Difference__mutmut_11': x_var_Difference__mutmut_11, 
    'x_var_Difference__mutmut_12': x_var_Difference__mutmut_12, 
    'x_var_Difference__mutmut_13': x_var_Difference__mutmut_13, 
    'x_var_Difference__mutmut_14': x_var_Difference__mutmut_14, 
    'x_var_Difference__mutmut_15': x_var_Difference__mutmut_15, 
    'x_var_Difference__mutmut_16': x_var_Difference__mutmut_16, 
    'x_var_Difference__mutmut_17': x_var_Difference__mutmut_17, 
    'x_var_Difference__mutmut_18': x_var_Difference__mutmut_18, 
    'x_var_Difference__mutmut_19': x_var_Difference__mutmut_19, 
    'x_var_Difference__mutmut_20': x_var_Difference__mutmut_20, 
    'x_var_Difference__mutmut_21': x_var_Difference__mutmut_21, 
    'x_var_Difference__mutmut_22': x_var_Difference__mutmut_22, 
    'x_var_Difference__mutmut_23': x_var_Difference__mutmut_23, 
    'x_var_Difference__mutmut_24': x_var_Difference__mutmut_24, 
    'x_var_Difference__mutmut_25': x_var_Difference__mutmut_25, 
    'x_var_Difference__mutmut_26': x_var_Difference__mutmut_26, 
    'x_var_Difference__mutmut_27': x_var_Difference__mutmut_27, 
    'x_var_Difference__mutmut_28': x_var_Difference__mutmut_28, 
    'x_var_Difference__mutmut_29': x_var_Difference__mutmut_29, 
    'x_var_Difference__mutmut_30': x_var_Difference__mutmut_30, 
    'x_var_Difference__mutmut_31': x_var_Difference__mutmut_31, 
    'x_var_Difference__mutmut_32': x_var_Difference__mutmut_32, 
    'x_var_Difference__mutmut_33': x_var_Difference__mutmut_33, 
    'x_var_Difference__mutmut_34': x_var_Difference__mutmut_34, 
    'x_var_Difference__mutmut_35': x_var_Difference__mutmut_35, 
    'x_var_Difference__mutmut_36': x_var_Difference__mutmut_36, 
    'x_var_Difference__mutmut_37': x_var_Difference__mutmut_37, 
    'x_var_Difference__mutmut_38': x_var_Difference__mutmut_38, 
    'x_var_Difference__mutmut_39': x_var_Difference__mutmut_39, 
    'x_var_Difference__mutmut_40': x_var_Difference__mutmut_40
}

def var_Difference(*args, **kwargs):
    result = _mutmut_trampoline(x_var_Difference__mutmut_orig, x_var_Difference__mutmut_mutants, args, kwargs)
    return result 

var_Difference.__signature__ = _mutmut_signature(x_var_Difference__mutmut_orig)
x_var_Difference__mutmut_orig.__name__ = 'x_var_Difference'
