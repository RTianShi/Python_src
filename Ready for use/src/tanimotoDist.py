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
def x_tanimotoDist__mutmut_orig(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_1(p1, p2):

    ab = None
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_2(p1, p2):

    ab = 1
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_3(p1, p2):

    ab = 0
    aSq = None
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_4(p1, p2):

    ab = 0
    aSq = 1
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_5(p1, p2):

    ab = 0
    aSq = 0
    bSq = None

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_6(p1, p2):

    ab = 0
    aSq = 0
    bSq = 1

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_7(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(None, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_8(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, None):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_9(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_10(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, ):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_11(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(1, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_12(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab = p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_13(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab -= p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_14(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] / p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_15(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq = p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_16(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq -= p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_17(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] / p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_18(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq = p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_19(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq -= p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_20(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] / p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_21(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = None
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_22(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq + ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_23(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq - bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_24(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator <= ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_25(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = None
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_26(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator >= 0:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_27(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 1:
        return 1 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_28(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 + ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_29(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 2 - ab / denominator
    else:
        return 0
def x_tanimotoDist__mutmut_30(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab * denominator
    else:
        return 0
def x_tanimotoDist__mutmut_31(p1, p2):

    ab = 0
    aSq = 0
    bSq = 0

    for i in range(0, len(p1)):
        ab += p1[i] * p2[i]
        aSq += p1[i] * p1[i]
        bSq += p2[i] * p2[i]

    denominator = aSq + bSq - ab
    if denominator < ab:
        denominator = ab
    if denominator > 0:
        return 1 - ab / denominator
    else:
        return 1

x_tanimotoDist__mutmut_mutants : ClassVar[MutantDict] = {
'x_tanimotoDist__mutmut_1': x_tanimotoDist__mutmut_1, 
    'x_tanimotoDist__mutmut_2': x_tanimotoDist__mutmut_2, 
    'x_tanimotoDist__mutmut_3': x_tanimotoDist__mutmut_3, 
    'x_tanimotoDist__mutmut_4': x_tanimotoDist__mutmut_4, 
    'x_tanimotoDist__mutmut_5': x_tanimotoDist__mutmut_5, 
    'x_tanimotoDist__mutmut_6': x_tanimotoDist__mutmut_6, 
    'x_tanimotoDist__mutmut_7': x_tanimotoDist__mutmut_7, 
    'x_tanimotoDist__mutmut_8': x_tanimotoDist__mutmut_8, 
    'x_tanimotoDist__mutmut_9': x_tanimotoDist__mutmut_9, 
    'x_tanimotoDist__mutmut_10': x_tanimotoDist__mutmut_10, 
    'x_tanimotoDist__mutmut_11': x_tanimotoDist__mutmut_11, 
    'x_tanimotoDist__mutmut_12': x_tanimotoDist__mutmut_12, 
    'x_tanimotoDist__mutmut_13': x_tanimotoDist__mutmut_13, 
    'x_tanimotoDist__mutmut_14': x_tanimotoDist__mutmut_14, 
    'x_tanimotoDist__mutmut_15': x_tanimotoDist__mutmut_15, 
    'x_tanimotoDist__mutmut_16': x_tanimotoDist__mutmut_16, 
    'x_tanimotoDist__mutmut_17': x_tanimotoDist__mutmut_17, 
    'x_tanimotoDist__mutmut_18': x_tanimotoDist__mutmut_18, 
    'x_tanimotoDist__mutmut_19': x_tanimotoDist__mutmut_19, 
    'x_tanimotoDist__mutmut_20': x_tanimotoDist__mutmut_20, 
    'x_tanimotoDist__mutmut_21': x_tanimotoDist__mutmut_21, 
    'x_tanimotoDist__mutmut_22': x_tanimotoDist__mutmut_22, 
    'x_tanimotoDist__mutmut_23': x_tanimotoDist__mutmut_23, 
    'x_tanimotoDist__mutmut_24': x_tanimotoDist__mutmut_24, 
    'x_tanimotoDist__mutmut_25': x_tanimotoDist__mutmut_25, 
    'x_tanimotoDist__mutmut_26': x_tanimotoDist__mutmut_26, 
    'x_tanimotoDist__mutmut_27': x_tanimotoDist__mutmut_27, 
    'x_tanimotoDist__mutmut_28': x_tanimotoDist__mutmut_28, 
    'x_tanimotoDist__mutmut_29': x_tanimotoDist__mutmut_29, 
    'x_tanimotoDist__mutmut_30': x_tanimotoDist__mutmut_30, 
    'x_tanimotoDist__mutmut_31': x_tanimotoDist__mutmut_31
}

def tanimotoDist(*args, **kwargs):
    result = _mutmut_trampoline(x_tanimotoDist__mutmut_orig, x_tanimotoDist__mutmut_mutants, args, kwargs)
    return result 

tanimotoDist.__signature__ = _mutmut_signature(x_tanimotoDist__mutmut_orig)
x_tanimotoDist__mutmut_orig.__name__ = 'x_tanimotoDist'
