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
def x_errorRate__mutmut_orig(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_1(labels, predictions):
    nberrors = None
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_2(labels, predictions):
    nberrors = 1
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_3(labels, predictions):
    nberrors = 0
    datasize = None

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_4(labels, predictions):
    nberrors = 0
    datasize = 1

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_5(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(None, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_6(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, None):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_7(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_8(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, ):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_9(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(1, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_10(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] != -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_11(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == +1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_12(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -2:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_13(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            break

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_14(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] == labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_15(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors = 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_16(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors -= 1

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_17(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 2

        datasize += 1

    return nberrors / datasize
def x_errorRate__mutmut_18(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize = 1

    return nberrors / datasize
def x_errorRate__mutmut_19(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize -= 1

    return nberrors / datasize
def x_errorRate__mutmut_20(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 2

    return nberrors / datasize
def x_errorRate__mutmut_21(labels, predictions):
    nberrors = 0
    datasize = 0

    for i in range(0, len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    return nberrors * datasize

x_errorRate__mutmut_mutants : ClassVar[MutantDict] = {
'x_errorRate__mutmut_1': x_errorRate__mutmut_1, 
    'x_errorRate__mutmut_2': x_errorRate__mutmut_2, 
    'x_errorRate__mutmut_3': x_errorRate__mutmut_3, 
    'x_errorRate__mutmut_4': x_errorRate__mutmut_4, 
    'x_errorRate__mutmut_5': x_errorRate__mutmut_5, 
    'x_errorRate__mutmut_6': x_errorRate__mutmut_6, 
    'x_errorRate__mutmut_7': x_errorRate__mutmut_7, 
    'x_errorRate__mutmut_8': x_errorRate__mutmut_8, 
    'x_errorRate__mutmut_9': x_errorRate__mutmut_9, 
    'x_errorRate__mutmut_10': x_errorRate__mutmut_10, 
    'x_errorRate__mutmut_11': x_errorRate__mutmut_11, 
    'x_errorRate__mutmut_12': x_errorRate__mutmut_12, 
    'x_errorRate__mutmut_13': x_errorRate__mutmut_13, 
    'x_errorRate__mutmut_14': x_errorRate__mutmut_14, 
    'x_errorRate__mutmut_15': x_errorRate__mutmut_15, 
    'x_errorRate__mutmut_16': x_errorRate__mutmut_16, 
    'x_errorRate__mutmut_17': x_errorRate__mutmut_17, 
    'x_errorRate__mutmut_18': x_errorRate__mutmut_18, 
    'x_errorRate__mutmut_19': x_errorRate__mutmut_19, 
    'x_errorRate__mutmut_20': x_errorRate__mutmut_20, 
    'x_errorRate__mutmut_21': x_errorRate__mutmut_21
}

def errorRate(*args, **kwargs):
    result = _mutmut_trampoline(x_errorRate__mutmut_orig, x_errorRate__mutmut_mutants, args, kwargs)
    return result 

errorRate.__signature__ = _mutmut_signature(x_errorRate__mutmut_orig)
x_errorRate__mutmut_orig.__name__ = 'x_errorRate'
