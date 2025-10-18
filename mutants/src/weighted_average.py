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
def x_weighted_average__mutmut_orig(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_1(a, b):
    sum1 = None
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_2(a, b):
    sum1 = 1
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_3(a, b):
    sum1 = 0
    sum2 = None

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_4(a, b):
    sum1 = 0
    sum2 = 1

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_5(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(None, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_6(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, None):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_7(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_8(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, ):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_9(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(1, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_10(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 = a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_11(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 -= a[i] * b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_12(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] / b[i]
        sum2 += b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_13(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 = b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_14(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 -= b[i]

    return sum1 / sum2
def x_weighted_average__mutmut_15(a, b):
    sum1 = 0
    sum2 = 0

    for i in range(0, len(a)):
        sum1 += a[i] * b[i]
        sum2 += b[i]

    return sum1 * sum2

x_weighted_average__mutmut_mutants : ClassVar[MutantDict] = {
'x_weighted_average__mutmut_1': x_weighted_average__mutmut_1, 
    'x_weighted_average__mutmut_2': x_weighted_average__mutmut_2, 
    'x_weighted_average__mutmut_3': x_weighted_average__mutmut_3, 
    'x_weighted_average__mutmut_4': x_weighted_average__mutmut_4, 
    'x_weighted_average__mutmut_5': x_weighted_average__mutmut_5, 
    'x_weighted_average__mutmut_6': x_weighted_average__mutmut_6, 
    'x_weighted_average__mutmut_7': x_weighted_average__mutmut_7, 
    'x_weighted_average__mutmut_8': x_weighted_average__mutmut_8, 
    'x_weighted_average__mutmut_9': x_weighted_average__mutmut_9, 
    'x_weighted_average__mutmut_10': x_weighted_average__mutmut_10, 
    'x_weighted_average__mutmut_11': x_weighted_average__mutmut_11, 
    'x_weighted_average__mutmut_12': x_weighted_average__mutmut_12, 
    'x_weighted_average__mutmut_13': x_weighted_average__mutmut_13, 
    'x_weighted_average__mutmut_14': x_weighted_average__mutmut_14, 
    'x_weighted_average__mutmut_15': x_weighted_average__mutmut_15
}

def weighted_average(*args, **kwargs):
    result = _mutmut_trampoline(x_weighted_average__mutmut_orig, x_weighted_average__mutmut_mutants, args, kwargs)
    return result 

weighted_average.__signature__ = _mutmut_signature(x_weighted_average__mutmut_orig)
x_weighted_average__mutmut_orig.__name__ = 'x_weighted_average'
