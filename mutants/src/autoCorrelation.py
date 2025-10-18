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
def x_autoCorrelation__mutmut_orig(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_1(data, lag, mean, variance):
    N = None
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_2(data, lag, mean, variance):
    N = len(data)
    run = None
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_3(data, lag, mean, variance):
    N = len(data)
    run = 1
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_4(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(None, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_5(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, None):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_6(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_7(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, ):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_8(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run = (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_9(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run -= (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_10(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) / (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_11(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] + mean) * (data[i - lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_12(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] + mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_13(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i + lag] - mean)
    return run / (N-lag)/variance
def x_autoCorrelation__mutmut_14(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N-lag) * variance
def x_autoCorrelation__mutmut_15(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run * (N-lag)/variance
def x_autoCorrelation__mutmut_16(data, lag, mean, variance):
    N = len(data)
    run = 0
    for i in range(lag, N):
        run += (data[i] - mean) * (data[i - lag] - mean)
    return run / (N + lag)/variance

x_autoCorrelation__mutmut_mutants : ClassVar[MutantDict] = {
'x_autoCorrelation__mutmut_1': x_autoCorrelation__mutmut_1, 
    'x_autoCorrelation__mutmut_2': x_autoCorrelation__mutmut_2, 
    'x_autoCorrelation__mutmut_3': x_autoCorrelation__mutmut_3, 
    'x_autoCorrelation__mutmut_4': x_autoCorrelation__mutmut_4, 
    'x_autoCorrelation__mutmut_5': x_autoCorrelation__mutmut_5, 
    'x_autoCorrelation__mutmut_6': x_autoCorrelation__mutmut_6, 
    'x_autoCorrelation__mutmut_7': x_autoCorrelation__mutmut_7, 
    'x_autoCorrelation__mutmut_8': x_autoCorrelation__mutmut_8, 
    'x_autoCorrelation__mutmut_9': x_autoCorrelation__mutmut_9, 
    'x_autoCorrelation__mutmut_10': x_autoCorrelation__mutmut_10, 
    'x_autoCorrelation__mutmut_11': x_autoCorrelation__mutmut_11, 
    'x_autoCorrelation__mutmut_12': x_autoCorrelation__mutmut_12, 
    'x_autoCorrelation__mutmut_13': x_autoCorrelation__mutmut_13, 
    'x_autoCorrelation__mutmut_14': x_autoCorrelation__mutmut_14, 
    'x_autoCorrelation__mutmut_15': x_autoCorrelation__mutmut_15, 
    'x_autoCorrelation__mutmut_16': x_autoCorrelation__mutmut_16
}

def autoCorrelation(*args, **kwargs):
    result = _mutmut_trampoline(x_autoCorrelation__mutmut_orig, x_autoCorrelation__mutmut_mutants, args, kwargs)
    return result 

autoCorrelation.__signature__ = _mutmut_signature(x_autoCorrelation__mutmut_orig)
x_autoCorrelation__mutmut_orig.__name__ = 'x_autoCorrelation'

