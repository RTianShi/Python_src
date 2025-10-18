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
def x_variance__mutmut_orig(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_1(x):
    suma = None
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_2(x):
    suma = 1
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_3(x):
    suma = 0
    sum1 = None
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_4(x):
    suma = 0
    sum1 = 1
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_5(x):
    suma = 0
    sum1 = 0
    var = None
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_6(x):
    suma = 0
    sum1 = 0
    var = 1
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_7(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = None

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_8(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 1

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_9(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(None, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_10(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, None):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_11(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_12(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, ):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_13(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(1, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_14(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = None

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_15(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma - x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_16(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = None

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_17(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma * len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_18(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(None, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_19(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, None):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_20(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_21(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, ):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_22(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(1, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_23(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = None

    var = sum1 / len(x)

    return var
def x_variance__mutmut_24(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 - (x[i] - avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_25(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) / (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_26(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] + avrg) * (x[i] - avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_27(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] + avrg)

    var = sum1 / len(x)

    return var
def x_variance__mutmut_28(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = None

    return var
def x_variance__mutmut_29(x):
    suma = 0
    sum1 = 0
    var = 0
    avrg = 0

    for i in range(0, len(x)):
        suma = suma + x[i]

    avrg = suma / len(x)

    for i in range(0, len(x)):
        sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)

    var = sum1 * len(x)

    return var

x_variance__mutmut_mutants : ClassVar[MutantDict] = {
'x_variance__mutmut_1': x_variance__mutmut_1, 
    'x_variance__mutmut_2': x_variance__mutmut_2, 
    'x_variance__mutmut_3': x_variance__mutmut_3, 
    'x_variance__mutmut_4': x_variance__mutmut_4, 
    'x_variance__mutmut_5': x_variance__mutmut_5, 
    'x_variance__mutmut_6': x_variance__mutmut_6, 
    'x_variance__mutmut_7': x_variance__mutmut_7, 
    'x_variance__mutmut_8': x_variance__mutmut_8, 
    'x_variance__mutmut_9': x_variance__mutmut_9, 
    'x_variance__mutmut_10': x_variance__mutmut_10, 
    'x_variance__mutmut_11': x_variance__mutmut_11, 
    'x_variance__mutmut_12': x_variance__mutmut_12, 
    'x_variance__mutmut_13': x_variance__mutmut_13, 
    'x_variance__mutmut_14': x_variance__mutmut_14, 
    'x_variance__mutmut_15': x_variance__mutmut_15, 
    'x_variance__mutmut_16': x_variance__mutmut_16, 
    'x_variance__mutmut_17': x_variance__mutmut_17, 
    'x_variance__mutmut_18': x_variance__mutmut_18, 
    'x_variance__mutmut_19': x_variance__mutmut_19, 
    'x_variance__mutmut_20': x_variance__mutmut_20, 
    'x_variance__mutmut_21': x_variance__mutmut_21, 
    'x_variance__mutmut_22': x_variance__mutmut_22, 
    'x_variance__mutmut_23': x_variance__mutmut_23, 
    'x_variance__mutmut_24': x_variance__mutmut_24, 
    'x_variance__mutmut_25': x_variance__mutmut_25, 
    'x_variance__mutmut_26': x_variance__mutmut_26, 
    'x_variance__mutmut_27': x_variance__mutmut_27, 
    'x_variance__mutmut_28': x_variance__mutmut_28, 
    'x_variance__mutmut_29': x_variance__mutmut_29
}

def variance(*args, **kwargs):
    result = _mutmut_trampoline(x_variance__mutmut_orig, x_variance__mutmut_mutants, args, kwargs)
    return result 

variance.__signature__ = _mutmut_signature(x_variance__mutmut_orig)
x_variance__mutmut_orig.__name__ = 'x_variance'
