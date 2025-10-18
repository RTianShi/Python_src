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
def x_quantile__mutmut_orig(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_1(sortedElements, phi):

    n = None
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_2(sortedElements, phi):

    n = len(sortedElements)
    index = None
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_3(sortedElements, phi):

    n = len(sortedElements)
    index = phi / (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_4(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n + 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_5(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 2)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_6(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = None

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_7(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(None)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_8(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = None

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_9(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index + lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_10(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n != 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_11(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 1:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_12(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 1

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_13(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs != n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_14(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n + 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_15(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 2:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_16(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = None

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_17(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = None

    return result
def x_quantile__mutmut_18(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] - delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_19(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) / sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_20(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 + delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_21(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (2 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_22(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta / sortedElements[lhs + 1]

    return result
def x_quantile__mutmut_23(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs - 1]

    return result
def x_quantile__mutmut_24(sortedElements, phi):

    n = len(sortedElements)
    index = phi * (n - 1)
    lhs = int(index)

    delta = index - lhs

    if n == 0:
        return 0

    if lhs == n - 1:
        result = sortedElements[lhs]

    else:
        result = (1 - delta) * sortedElements[lhs] + delta * sortedElements[lhs + 2]

    return result

x_quantile__mutmut_mutants : ClassVar[MutantDict] = {
'x_quantile__mutmut_1': x_quantile__mutmut_1, 
    'x_quantile__mutmut_2': x_quantile__mutmut_2, 
    'x_quantile__mutmut_3': x_quantile__mutmut_3, 
    'x_quantile__mutmut_4': x_quantile__mutmut_4, 
    'x_quantile__mutmut_5': x_quantile__mutmut_5, 
    'x_quantile__mutmut_6': x_quantile__mutmut_6, 
    'x_quantile__mutmut_7': x_quantile__mutmut_7, 
    'x_quantile__mutmut_8': x_quantile__mutmut_8, 
    'x_quantile__mutmut_9': x_quantile__mutmut_9, 
    'x_quantile__mutmut_10': x_quantile__mutmut_10, 
    'x_quantile__mutmut_11': x_quantile__mutmut_11, 
    'x_quantile__mutmut_12': x_quantile__mutmut_12, 
    'x_quantile__mutmut_13': x_quantile__mutmut_13, 
    'x_quantile__mutmut_14': x_quantile__mutmut_14, 
    'x_quantile__mutmut_15': x_quantile__mutmut_15, 
    'x_quantile__mutmut_16': x_quantile__mutmut_16, 
    'x_quantile__mutmut_17': x_quantile__mutmut_17, 
    'x_quantile__mutmut_18': x_quantile__mutmut_18, 
    'x_quantile__mutmut_19': x_quantile__mutmut_19, 
    'x_quantile__mutmut_20': x_quantile__mutmut_20, 
    'x_quantile__mutmut_21': x_quantile__mutmut_21, 
    'x_quantile__mutmut_22': x_quantile__mutmut_22, 
    'x_quantile__mutmut_23': x_quantile__mutmut_23, 
    'x_quantile__mutmut_24': x_quantile__mutmut_24
}

def quantile(*args, **kwargs):
    result = _mutmut_trampoline(x_quantile__mutmut_orig, x_quantile__mutmut_mutants, args, kwargs)
    return result 

quantile.__signature__ = _mutmut_signature(x_quantile__mutmut_orig)
x_quantile__mutmut_orig.__name__ = 'x_quantile'
