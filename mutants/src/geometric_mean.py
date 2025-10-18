import math
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


def x_geometric_mean__mutmut_orig(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(product, 1/len(a))


def x_geometric_mean__mutmut_1(a):
    product = None

    for i in a:
        product *= i

    return math.pow(product, 1/len(a))


def x_geometric_mean__mutmut_2(a):
    product = 2

    for i in a:
        product *= i

    return math.pow(product, 1/len(a))


def x_geometric_mean__mutmut_3(a):
    product = 1

    for i in a:
        product = i

    return math.pow(product, 1/len(a))


def x_geometric_mean__mutmut_4(a):
    product = 1

    for i in a:
        product /= i

    return math.pow(product, 1/len(a))


def x_geometric_mean__mutmut_5(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(None, 1/len(a))


def x_geometric_mean__mutmut_6(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(product, None)


def x_geometric_mean__mutmut_7(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(1/len(a))


def x_geometric_mean__mutmut_8(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(product, )


def x_geometric_mean__mutmut_9(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(product, 1 * len(a))


def x_geometric_mean__mutmut_10(a):
    product = 1

    for i in a:
        product *= i

    return math.pow(product, 2/len(a))

x_geometric_mean__mutmut_mutants : ClassVar[MutantDict] = {
'x_geometric_mean__mutmut_1': x_geometric_mean__mutmut_1, 
    'x_geometric_mean__mutmut_2': x_geometric_mean__mutmut_2, 
    'x_geometric_mean__mutmut_3': x_geometric_mean__mutmut_3, 
    'x_geometric_mean__mutmut_4': x_geometric_mean__mutmut_4, 
    'x_geometric_mean__mutmut_5': x_geometric_mean__mutmut_5, 
    'x_geometric_mean__mutmut_6': x_geometric_mean__mutmut_6, 
    'x_geometric_mean__mutmut_7': x_geometric_mean__mutmut_7, 
    'x_geometric_mean__mutmut_8': x_geometric_mean__mutmut_8, 
    'x_geometric_mean__mutmut_9': x_geometric_mean__mutmut_9, 
    'x_geometric_mean__mutmut_10': x_geometric_mean__mutmut_10
}

def geometric_mean(*args, **kwargs):
    result = _mutmut_trampoline(x_geometric_mean__mutmut_orig, x_geometric_mean__mutmut_mutants, args, kwargs)
    return result 

geometric_mean.__signature__ = _mutmut_signature(x_geometric_mean__mutmut_orig)
x_geometric_mean__mutmut_orig.__name__ = 'x_geometric_mean'
