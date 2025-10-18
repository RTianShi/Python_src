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


def x_eval_Internal__mutmut_orig(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_1(x, y, z):

    nearest = None
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_2(x, y, z):

    nearest = 1
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_3(x, y, z):

    nearest = 0
    n = None
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_4(x, y, z):

    nearest = 0
    n = len(x)
    c = None
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_5(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = None

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_6(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = None

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_7(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(None, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_8(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, None):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_9(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_10(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, ):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_11(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(1, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_12(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = None
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_13(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = None

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_14(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = None

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_15(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(None)

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_16(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z + x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_17(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist <= min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_18(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = None
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_19(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = None

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_20(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = None
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_21(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(None, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_22(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, None):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_23(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_24(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, ):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_25(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(1, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_26(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(None, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_27(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, None):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_28(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_29(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, ):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_30(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(1, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_31(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n + i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_32(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = None
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_33(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] + z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_34(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = None
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_35(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] + z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_36(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i - j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_37(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = None
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_38(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] + x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_39(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i - j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_40(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = None

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_41(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) * divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_42(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] + d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_43(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j - 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_44(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 2] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_45(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = None
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_46(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc / w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_47(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = None

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_48(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td / w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_49(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest <= 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_50(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 / (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_51(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 1.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_52(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i - 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_53(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n + i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_54(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 2):
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_55(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value = c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_56(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value -= c[nearest]
        else:
            nearest -= 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_57(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest = 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_58(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest += 1
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_59(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 2
            value += d[nearest]

    return value


def x_eval_Internal__mutmut_60(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value = d[nearest]

    return value


def x_eval_Internal__mutmut_61(x, y, z):

    nearest = 0
    n = len(x)
    c = []
    d = []

    min_dist = math.inf

    for i in range(0, n):
        c[i] = y[i]
        d[i] = y[i]

        dist = abs(z -x[i])

        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(0, n):
        for j in range(0, n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i +j]
            w = (c[j + 1] - d[j]) / divider

            c[j] = tc * w
            d[j] = td * w

        if nearest < 0.5 * (n - i + 1):
            value += c[nearest]
        else:
            nearest -= 1
            value -= d[nearest]

    return value

x_eval_Internal__mutmut_mutants : ClassVar[MutantDict] = {
'x_eval_Internal__mutmut_1': x_eval_Internal__mutmut_1, 
    'x_eval_Internal__mutmut_2': x_eval_Internal__mutmut_2, 
    'x_eval_Internal__mutmut_3': x_eval_Internal__mutmut_3, 
    'x_eval_Internal__mutmut_4': x_eval_Internal__mutmut_4, 
    'x_eval_Internal__mutmut_5': x_eval_Internal__mutmut_5, 
    'x_eval_Internal__mutmut_6': x_eval_Internal__mutmut_6, 
    'x_eval_Internal__mutmut_7': x_eval_Internal__mutmut_7, 
    'x_eval_Internal__mutmut_8': x_eval_Internal__mutmut_8, 
    'x_eval_Internal__mutmut_9': x_eval_Internal__mutmut_9, 
    'x_eval_Internal__mutmut_10': x_eval_Internal__mutmut_10, 
    'x_eval_Internal__mutmut_11': x_eval_Internal__mutmut_11, 
    'x_eval_Internal__mutmut_12': x_eval_Internal__mutmut_12, 
    'x_eval_Internal__mutmut_13': x_eval_Internal__mutmut_13, 
    'x_eval_Internal__mutmut_14': x_eval_Internal__mutmut_14, 
    'x_eval_Internal__mutmut_15': x_eval_Internal__mutmut_15, 
    'x_eval_Internal__mutmut_16': x_eval_Internal__mutmut_16, 
    'x_eval_Internal__mutmut_17': x_eval_Internal__mutmut_17, 
    'x_eval_Internal__mutmut_18': x_eval_Internal__mutmut_18, 
    'x_eval_Internal__mutmut_19': x_eval_Internal__mutmut_19, 
    'x_eval_Internal__mutmut_20': x_eval_Internal__mutmut_20, 
    'x_eval_Internal__mutmut_21': x_eval_Internal__mutmut_21, 
    'x_eval_Internal__mutmut_22': x_eval_Internal__mutmut_22, 
    'x_eval_Internal__mutmut_23': x_eval_Internal__mutmut_23, 
    'x_eval_Internal__mutmut_24': x_eval_Internal__mutmut_24, 
    'x_eval_Internal__mutmut_25': x_eval_Internal__mutmut_25, 
    'x_eval_Internal__mutmut_26': x_eval_Internal__mutmut_26, 
    'x_eval_Internal__mutmut_27': x_eval_Internal__mutmut_27, 
    'x_eval_Internal__mutmut_28': x_eval_Internal__mutmut_28, 
    'x_eval_Internal__mutmut_29': x_eval_Internal__mutmut_29, 
    'x_eval_Internal__mutmut_30': x_eval_Internal__mutmut_30, 
    'x_eval_Internal__mutmut_31': x_eval_Internal__mutmut_31, 
    'x_eval_Internal__mutmut_32': x_eval_Internal__mutmut_32, 
    'x_eval_Internal__mutmut_33': x_eval_Internal__mutmut_33, 
    'x_eval_Internal__mutmut_34': x_eval_Internal__mutmut_34, 
    'x_eval_Internal__mutmut_35': x_eval_Internal__mutmut_35, 
    'x_eval_Internal__mutmut_36': x_eval_Internal__mutmut_36, 
    'x_eval_Internal__mutmut_37': x_eval_Internal__mutmut_37, 
    'x_eval_Internal__mutmut_38': x_eval_Internal__mutmut_38, 
    'x_eval_Internal__mutmut_39': x_eval_Internal__mutmut_39, 
    'x_eval_Internal__mutmut_40': x_eval_Internal__mutmut_40, 
    'x_eval_Internal__mutmut_41': x_eval_Internal__mutmut_41, 
    'x_eval_Internal__mutmut_42': x_eval_Internal__mutmut_42, 
    'x_eval_Internal__mutmut_43': x_eval_Internal__mutmut_43, 
    'x_eval_Internal__mutmut_44': x_eval_Internal__mutmut_44, 
    'x_eval_Internal__mutmut_45': x_eval_Internal__mutmut_45, 
    'x_eval_Internal__mutmut_46': x_eval_Internal__mutmut_46, 
    'x_eval_Internal__mutmut_47': x_eval_Internal__mutmut_47, 
    'x_eval_Internal__mutmut_48': x_eval_Internal__mutmut_48, 
    'x_eval_Internal__mutmut_49': x_eval_Internal__mutmut_49, 
    'x_eval_Internal__mutmut_50': x_eval_Internal__mutmut_50, 
    'x_eval_Internal__mutmut_51': x_eval_Internal__mutmut_51, 
    'x_eval_Internal__mutmut_52': x_eval_Internal__mutmut_52, 
    'x_eval_Internal__mutmut_53': x_eval_Internal__mutmut_53, 
    'x_eval_Internal__mutmut_54': x_eval_Internal__mutmut_54, 
    'x_eval_Internal__mutmut_55': x_eval_Internal__mutmut_55, 
    'x_eval_Internal__mutmut_56': x_eval_Internal__mutmut_56, 
    'x_eval_Internal__mutmut_57': x_eval_Internal__mutmut_57, 
    'x_eval_Internal__mutmut_58': x_eval_Internal__mutmut_58, 
    'x_eval_Internal__mutmut_59': x_eval_Internal__mutmut_59, 
    'x_eval_Internal__mutmut_60': x_eval_Internal__mutmut_60, 
    'x_eval_Internal__mutmut_61': x_eval_Internal__mutmut_61
}

def eval_Internal(*args, **kwargs):
    result = _mutmut_trampoline(x_eval_Internal__mutmut_orig, x_eval_Internal__mutmut_mutants, args, kwargs)
    return result 

eval_Internal.__signature__ = _mutmut_signature(x_eval_Internal__mutmut_orig)
x_eval_Internal__mutmut_orig.__name__ = 'x_eval_Internal'
