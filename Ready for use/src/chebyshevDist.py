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
def x_chebyshevDist__mutmut_orig(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_1(p1, p2):
    if len(p1) == len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_2(p1, p2):
    if len(p1) != len(p2):
        print(None)
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_3(p1, p2):
    if len(p1) != len(p2):
        print('XXError!XX')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_4(p1, p2):
    if len(p1) != len(p2):
        print('error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_5(p1, p2):
    if len(p1) != len(p2):
        print('ERROR!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_6(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return +1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_7(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -2

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_8(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = None
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_9(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(None)
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_10(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] + p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_11(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[1] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_12(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[1])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_13(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(None, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_14(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, None):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_15(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_16(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, ):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_17(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(1, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_18(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = None

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_19(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(None)

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_20(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] + p2[i])

        if maxDiff < diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_21(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff <= diff:
            maxDiff = diff

    return maxDiff
def x_chebyshevDist__mutmut_22(p1, p2):
    if len(p1) != len(p2):
        print('Error!')
        return -1

    maxDiff = abs(p1[0] - p2[0])
    for i in range(0, len(p1)):
        diff = abs(p1[i] - p2[i])

        if maxDiff < diff:
            maxDiff = None

    return maxDiff

x_chebyshevDist__mutmut_mutants : ClassVar[MutantDict] = {
'x_chebyshevDist__mutmut_1': x_chebyshevDist__mutmut_1, 
    'x_chebyshevDist__mutmut_2': x_chebyshevDist__mutmut_2, 
    'x_chebyshevDist__mutmut_3': x_chebyshevDist__mutmut_3, 
    'x_chebyshevDist__mutmut_4': x_chebyshevDist__mutmut_4, 
    'x_chebyshevDist__mutmut_5': x_chebyshevDist__mutmut_5, 
    'x_chebyshevDist__mutmut_6': x_chebyshevDist__mutmut_6, 
    'x_chebyshevDist__mutmut_7': x_chebyshevDist__mutmut_7, 
    'x_chebyshevDist__mutmut_8': x_chebyshevDist__mutmut_8, 
    'x_chebyshevDist__mutmut_9': x_chebyshevDist__mutmut_9, 
    'x_chebyshevDist__mutmut_10': x_chebyshevDist__mutmut_10, 
    'x_chebyshevDist__mutmut_11': x_chebyshevDist__mutmut_11, 
    'x_chebyshevDist__mutmut_12': x_chebyshevDist__mutmut_12, 
    'x_chebyshevDist__mutmut_13': x_chebyshevDist__mutmut_13, 
    'x_chebyshevDist__mutmut_14': x_chebyshevDist__mutmut_14, 
    'x_chebyshevDist__mutmut_15': x_chebyshevDist__mutmut_15, 
    'x_chebyshevDist__mutmut_16': x_chebyshevDist__mutmut_16, 
    'x_chebyshevDist__mutmut_17': x_chebyshevDist__mutmut_17, 
    'x_chebyshevDist__mutmut_18': x_chebyshevDist__mutmut_18, 
    'x_chebyshevDist__mutmut_19': x_chebyshevDist__mutmut_19, 
    'x_chebyshevDist__mutmut_20': x_chebyshevDist__mutmut_20, 
    'x_chebyshevDist__mutmut_21': x_chebyshevDist__mutmut_21, 
    'x_chebyshevDist__mutmut_22': x_chebyshevDist__mutmut_22
}

def chebyshevDist(*args, **kwargs):
    result = _mutmut_trampoline(x_chebyshevDist__mutmut_orig, x_chebyshevDist__mutmut_mutants, args, kwargs)
    return result 

chebyshevDist.__signature__ = _mutmut_signature(x_chebyshevDist__mutmut_orig)
x_chebyshevDist__mutmut_orig.__name__ = 'x_chebyshevDist'
