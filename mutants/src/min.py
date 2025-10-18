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
def x_min__mutmut_orig(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_1(data):
    size = None

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_2(data):
    size = len(data)

    if(size != 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_3(data):
    size = len(data)

    if(size == 1):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_4(data):
    size = len(data)

    if(size == 0):
        raise NameError(None)

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_5(data):
    size = len(data)

    if(size == 0):
        raise NameError('XXIligalArgumentExceptionXX')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_6(data):
    size = len(data)

    if(size == 0):
        raise NameError('iligalargumentexception')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_7(data):
    size = len(data)

    if(size == 0):
        raise NameError('ILIGALARGUMENTEXCEPTION')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_8(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = None
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_9(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = None

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_10(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size + 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_11(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 2]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_12(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(None, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_13(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, None, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_14(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, None):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_15(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(-1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_16(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_17(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, ):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_18(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size + 1, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_19(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 2, -1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_20(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, +1, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_21(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -2, -1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_22(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, +1):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_23(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -2):
        if elements[i] < min:
            min = elements[i]

    return min
def x_min__mutmut_24(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] <= min:
            min = elements[i]

    return min
def x_min__mutmut_25(data):
    size = len(data)

    if(size == 0):
        raise NameError('IligalArgumentException')

    elements = data.copy()
    minimoun = elements[size - 1]

    for i in range(size - 1, -1, -1):
        if elements[i] < min:
            min = None

    return min

x_min__mutmut_mutants : ClassVar[MutantDict] = {
'x_min__mutmut_1': x_min__mutmut_1, 
    'x_min__mutmut_2': x_min__mutmut_2, 
    'x_min__mutmut_3': x_min__mutmut_3, 
    'x_min__mutmut_4': x_min__mutmut_4, 
    'x_min__mutmut_5': x_min__mutmut_5, 
    'x_min__mutmut_6': x_min__mutmut_6, 
    'x_min__mutmut_7': x_min__mutmut_7, 
    'x_min__mutmut_8': x_min__mutmut_8, 
    'x_min__mutmut_9': x_min__mutmut_9, 
    'x_min__mutmut_10': x_min__mutmut_10, 
    'x_min__mutmut_11': x_min__mutmut_11, 
    'x_min__mutmut_12': x_min__mutmut_12, 
    'x_min__mutmut_13': x_min__mutmut_13, 
    'x_min__mutmut_14': x_min__mutmut_14, 
    'x_min__mutmut_15': x_min__mutmut_15, 
    'x_min__mutmut_16': x_min__mutmut_16, 
    'x_min__mutmut_17': x_min__mutmut_17, 
    'x_min__mutmut_18': x_min__mutmut_18, 
    'x_min__mutmut_19': x_min__mutmut_19, 
    'x_min__mutmut_20': x_min__mutmut_20, 
    'x_min__mutmut_21': x_min__mutmut_21, 
    'x_min__mutmut_22': x_min__mutmut_22, 
    'x_min__mutmut_23': x_min__mutmut_23, 
    'x_min__mutmut_24': x_min__mutmut_24, 
    'x_min__mutmut_25': x_min__mutmut_25
}

def min(*args, **kwargs):
    result = _mutmut_trampoline(x_min__mutmut_orig, x_min__mutmut_mutants, args, kwargs)
    return result 

min.__signature__ = _mutmut_signature(x_min__mutmut_orig)
x_min__mutmut_orig.__name__ = 'x_min'