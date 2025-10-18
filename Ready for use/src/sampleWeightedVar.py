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
def x_sampleWeightedVar__mutmut_orig(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_1(data, weights):

    sumOfWeights = None
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_2(data, weights):

    sumOfWeights = 1
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_3(data, weights):

    sumOfWeights = 0
    sumOfProducts = None
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_4(data, weights):

    sumOfWeights = 0
    sumOfProducts = 1
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_5(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = None

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_6(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 1

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_7(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(None, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_8(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, None):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_9(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_10(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, ):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_11(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(1, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_12(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights = weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_13(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights -= weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_14(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts = data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_15(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts -= data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_16(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] / weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_17(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts = data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_18(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts -= data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_19(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] / weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_20(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] / data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_21(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) * (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_22(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts + sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_23(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts * sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_24(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts / sumOfProducts / sumOfWeights) / (sumOfWeights - 1)
def x_sampleWeightedVar__mutmut_25(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights + 1)
def x_sampleWeightedVar__mutmut_26(data, weights):

    sumOfWeights = 0
    sumOfProducts = 0
    sumOfSquaredProducts = 0

    for i in range(0, len(data)):
        sumOfWeights += weights[i]
        sumOfProducts += data[i] * weights[i]
        sumOfSquaredProducts += data[i] * data[i] * weights[i]

    return (sumOfSquaredProducts - sumOfProducts * sumOfProducts / sumOfWeights) / (sumOfWeights - 2)

x_sampleWeightedVar__mutmut_mutants : ClassVar[MutantDict] = {
'x_sampleWeightedVar__mutmut_1': x_sampleWeightedVar__mutmut_1, 
    'x_sampleWeightedVar__mutmut_2': x_sampleWeightedVar__mutmut_2, 
    'x_sampleWeightedVar__mutmut_3': x_sampleWeightedVar__mutmut_3, 
    'x_sampleWeightedVar__mutmut_4': x_sampleWeightedVar__mutmut_4, 
    'x_sampleWeightedVar__mutmut_5': x_sampleWeightedVar__mutmut_5, 
    'x_sampleWeightedVar__mutmut_6': x_sampleWeightedVar__mutmut_6, 
    'x_sampleWeightedVar__mutmut_7': x_sampleWeightedVar__mutmut_7, 
    'x_sampleWeightedVar__mutmut_8': x_sampleWeightedVar__mutmut_8, 
    'x_sampleWeightedVar__mutmut_9': x_sampleWeightedVar__mutmut_9, 
    'x_sampleWeightedVar__mutmut_10': x_sampleWeightedVar__mutmut_10, 
    'x_sampleWeightedVar__mutmut_11': x_sampleWeightedVar__mutmut_11, 
    'x_sampleWeightedVar__mutmut_12': x_sampleWeightedVar__mutmut_12, 
    'x_sampleWeightedVar__mutmut_13': x_sampleWeightedVar__mutmut_13, 
    'x_sampleWeightedVar__mutmut_14': x_sampleWeightedVar__mutmut_14, 
    'x_sampleWeightedVar__mutmut_15': x_sampleWeightedVar__mutmut_15, 
    'x_sampleWeightedVar__mutmut_16': x_sampleWeightedVar__mutmut_16, 
    'x_sampleWeightedVar__mutmut_17': x_sampleWeightedVar__mutmut_17, 
    'x_sampleWeightedVar__mutmut_18': x_sampleWeightedVar__mutmut_18, 
    'x_sampleWeightedVar__mutmut_19': x_sampleWeightedVar__mutmut_19, 
    'x_sampleWeightedVar__mutmut_20': x_sampleWeightedVar__mutmut_20, 
    'x_sampleWeightedVar__mutmut_21': x_sampleWeightedVar__mutmut_21, 
    'x_sampleWeightedVar__mutmut_22': x_sampleWeightedVar__mutmut_22, 
    'x_sampleWeightedVar__mutmut_23': x_sampleWeightedVar__mutmut_23, 
    'x_sampleWeightedVar__mutmut_24': x_sampleWeightedVar__mutmut_24, 
    'x_sampleWeightedVar__mutmut_25': x_sampleWeightedVar__mutmut_25, 
    'x_sampleWeightedVar__mutmut_26': x_sampleWeightedVar__mutmut_26
}

def sampleWeightedVar(*args, **kwargs):
    result = _mutmut_trampoline(x_sampleWeightedVar__mutmut_orig, x_sampleWeightedVar__mutmut_mutants, args, kwargs)
    return result 

sampleWeightedVar.__signature__ = _mutmut_signature(x_sampleWeightedVar__mutmut_orig)
x_sampleWeightedVar__mutmut_orig.__name__ = 'x_sampleWeightedVar'
