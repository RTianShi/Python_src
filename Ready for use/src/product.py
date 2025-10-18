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
def x_product__mutmut_orig(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_1(elements):

    size = None
    product1 = 1

    for i in range(size, -1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_2(elements):

    size = len(elements)
    product1 = None

    for i in range(size, -1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_3(elements):

    size = len(elements)
    product1 = 2

    for i in range(size, -1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_4(elements):

    size = len(elements)
    product1 = 1

    for i in range(None, -1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_5(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, None, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_6(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, None):
        product1 *= elements[i]

    return product1
def x_product__mutmut_7(elements):

    size = len(elements)
    product1 = 1

    for i in range(-1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_8(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_9(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, ):
        product1 *= elements[i]

    return product1
def x_product__mutmut_10(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, +1, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_11(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -2, -1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_12(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, +1):
        product1 *= elements[i]

    return product1
def x_product__mutmut_13(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, -2):
        product1 *= elements[i]

    return product1
def x_product__mutmut_14(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, -1):
        product1 = elements[i]

    return product1
def x_product__mutmut_15(elements):

    size = len(elements)
    product1 = 1

    for i in range(size, -1, -1):
        product1 /= elements[i]

    return product1

x_product__mutmut_mutants : ClassVar[MutantDict] = {
'x_product__mutmut_1': x_product__mutmut_1, 
    'x_product__mutmut_2': x_product__mutmut_2, 
    'x_product__mutmut_3': x_product__mutmut_3, 
    'x_product__mutmut_4': x_product__mutmut_4, 
    'x_product__mutmut_5': x_product__mutmut_5, 
    'x_product__mutmut_6': x_product__mutmut_6, 
    'x_product__mutmut_7': x_product__mutmut_7, 
    'x_product__mutmut_8': x_product__mutmut_8, 
    'x_product__mutmut_9': x_product__mutmut_9, 
    'x_product__mutmut_10': x_product__mutmut_10, 
    'x_product__mutmut_11': x_product__mutmut_11, 
    'x_product__mutmut_12': x_product__mutmut_12, 
    'x_product__mutmut_13': x_product__mutmut_13, 
    'x_product__mutmut_14': x_product__mutmut_14, 
    'x_product__mutmut_15': x_product__mutmut_15
}

def product(*args, **kwargs):
    result = _mutmut_trampoline(x_product__mutmut_orig, x_product__mutmut_mutants, args, kwargs)
    return result 

product.__signature__ = _mutmut_signature(x_product__mutmut_orig)
x_product__mutmut_orig.__name__ = 'x_product'
