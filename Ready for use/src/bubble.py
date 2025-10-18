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
def x_bubble__mutmut_orig(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_1(elements):
    for n in range(None, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_2(elements):
    for n in range(len(elements)-1, None, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_3(elements):
    for n in range(len(elements)-1, 0, None):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_4(elements):
    for n in range(0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_5(elements):
    for n in range(len(elements)-1, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_6(elements):
    for n in range(len(elements)-1, 0, ):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_7(elements):
    for n in range(len(elements) + 1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_8(elements):
    for n in range(len(elements)-2, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_9(elements):
    for n in range(len(elements)-1, 1, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_10(elements):
    for n in range(len(elements)-1, 0, +1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_11(elements):
    for n in range(len(elements)-1, 0, -2):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_12(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(None):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_13(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] >= elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_14(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i - 1]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_15(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 2]:

                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_16(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = None

    return elements
def x_bubble__mutmut_17(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i - 1] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_18(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 2] = elements[i + 1], elements[i]

    return elements
def x_bubble__mutmut_19(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i - 1], elements[i]

    return elements
def x_bubble__mutmut_20(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):

            if elements[i] > elements[i + 1]:

                elements[i], elements[i + 1] = elements[i + 2], elements[i]

    return elements

x_bubble__mutmut_mutants : ClassVar[MutantDict] = {
'x_bubble__mutmut_1': x_bubble__mutmut_1, 
    'x_bubble__mutmut_2': x_bubble__mutmut_2, 
    'x_bubble__mutmut_3': x_bubble__mutmut_3, 
    'x_bubble__mutmut_4': x_bubble__mutmut_4, 
    'x_bubble__mutmut_5': x_bubble__mutmut_5, 
    'x_bubble__mutmut_6': x_bubble__mutmut_6, 
    'x_bubble__mutmut_7': x_bubble__mutmut_7, 
    'x_bubble__mutmut_8': x_bubble__mutmut_8, 
    'x_bubble__mutmut_9': x_bubble__mutmut_9, 
    'x_bubble__mutmut_10': x_bubble__mutmut_10, 
    'x_bubble__mutmut_11': x_bubble__mutmut_11, 
    'x_bubble__mutmut_12': x_bubble__mutmut_12, 
    'x_bubble__mutmut_13': x_bubble__mutmut_13, 
    'x_bubble__mutmut_14': x_bubble__mutmut_14, 
    'x_bubble__mutmut_15': x_bubble__mutmut_15, 
    'x_bubble__mutmut_16': x_bubble__mutmut_16, 
    'x_bubble__mutmut_17': x_bubble__mutmut_17, 
    'x_bubble__mutmut_18': x_bubble__mutmut_18, 
    'x_bubble__mutmut_19': x_bubble__mutmut_19, 
    'x_bubble__mutmut_20': x_bubble__mutmut_20
}

def bubble(*args, **kwargs):
    result = _mutmut_trampoline(x_bubble__mutmut_orig, x_bubble__mutmut_mutants, args, kwargs)
    return result 

bubble.__signature__ = _mutmut_signature(x_bubble__mutmut_orig)
x_bubble__mutmut_orig.__name__ = 'x_bubble'