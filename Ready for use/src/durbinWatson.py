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
def x_durbinWatson__mutmut_orig(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_1(elements):
    run = None

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_2(elements):
    run = 1

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_3(elements):
    run = 0

    for i in range(None, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_4(elements):
    run = 0

    for i in range(1, None):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_5(elements):
    run = 0

    for i in range(len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_6(elements):
    run = 0

    for i in range(1, ):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_7(elements):
    run = 0

    for i in range(2, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_8(elements):
    run = 0

    for i in range(1, len(elements)):
        x = None

        run += x * x

    return run
def x_durbinWatson__mutmut_9(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] + elements[i - 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_10(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i + 1]

        run += x * x

    return run
def x_durbinWatson__mutmut_11(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 2]

        run += x * x

    return run
def x_durbinWatson__mutmut_12(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run = x * x

    return run
def x_durbinWatson__mutmut_13(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run -= x * x

    return run
def x_durbinWatson__mutmut_14(elements):
    run = 0

    for i in range(1, len(elements)):
        x = elements[i] - elements[i - 1]

        run += x / x

    return run

x_durbinWatson__mutmut_mutants : ClassVar[MutantDict] = {
'x_durbinWatson__mutmut_1': x_durbinWatson__mutmut_1, 
    'x_durbinWatson__mutmut_2': x_durbinWatson__mutmut_2, 
    'x_durbinWatson__mutmut_3': x_durbinWatson__mutmut_3, 
    'x_durbinWatson__mutmut_4': x_durbinWatson__mutmut_4, 
    'x_durbinWatson__mutmut_5': x_durbinWatson__mutmut_5, 
    'x_durbinWatson__mutmut_6': x_durbinWatson__mutmut_6, 
    'x_durbinWatson__mutmut_7': x_durbinWatson__mutmut_7, 
    'x_durbinWatson__mutmut_8': x_durbinWatson__mutmut_8, 
    'x_durbinWatson__mutmut_9': x_durbinWatson__mutmut_9, 
    'x_durbinWatson__mutmut_10': x_durbinWatson__mutmut_10, 
    'x_durbinWatson__mutmut_11': x_durbinWatson__mutmut_11, 
    'x_durbinWatson__mutmut_12': x_durbinWatson__mutmut_12, 
    'x_durbinWatson__mutmut_13': x_durbinWatson__mutmut_13, 
    'x_durbinWatson__mutmut_14': x_durbinWatson__mutmut_14
}

def durbinWatson(*args, **kwargs):
    result = _mutmut_trampoline(x_durbinWatson__mutmut_orig, x_durbinWatson__mutmut_mutants, args, kwargs)
    return result 

durbinWatson.__signature__ = _mutmut_signature(x_durbinWatson__mutmut_orig)
x_durbinWatson__mutmut_orig.__name__ = 'x_durbinWatson'
