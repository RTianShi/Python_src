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


def x_safeNorm__mutmut_orig(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_1(v):
    rdwarf = None
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_2(v):
    rdwarf = 1.0
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_3(v):
    rdwarf = 3.834e-20
    rgiant = None
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_4(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_5(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = None
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_6(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 1
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_7(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = None
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_8(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 1
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_9(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = None
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_10(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 1
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_11(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = None
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_12(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 1
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_13(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = None
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_14(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 1
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_15(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = None
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_16(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = None

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_17(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant * floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_18(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(None, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_19(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, None):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_20(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_21(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, ):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_22(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(1, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_23(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = None
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_24(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(None)
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_25(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf and xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_26(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs <= rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_27(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs >= agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_28(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs >= rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_29(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs >= x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_30(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = None
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_31(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max * xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_32(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = None
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_33(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 - s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_34(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 2 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_35(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r / r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_36(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 / r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_37(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = None

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_38(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = None
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_39(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs * x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_40(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 = r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_41(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 -= r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_42(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r / r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_43(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs >= x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_44(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = None
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_45(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max * xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_46(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = None
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_47(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 - s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_48(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 2 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_49(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r / r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_50(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 / r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_51(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = None
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_52(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs == 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_53(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 1:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_54(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = None
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_55(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs * x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_56(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 = r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_57(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 -= r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_58(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r / r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_59(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 = xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_60(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 -= xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_61(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs / xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_62(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 == 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_63(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 1:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_64(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = None
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_65(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max / math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_66(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(None)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_67(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 - s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_68(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max * x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_69(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 * x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_70(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 != 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_71(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 1:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_72(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = None

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_73(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max / math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_74(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(None)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_75(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 > x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_76(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = None
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_77(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(None)
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_78(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 / (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_79(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 - x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_80(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (2 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_81(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 / (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_82(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max * s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_83(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max / s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_84(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = None

    return norm


def x_safeNorm__mutmut_85(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(None)

    return norm


def x_safeNorm__mutmut_86(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max / (s2 / x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_87(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max - x3max * s3))

    return norm


def x_safeNorm__mutmut_88(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 * x3max + x3max * s3))

    return norm


def x_safeNorm__mutmut_89(v):
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = 0
    s2 = 0
    s3 = 0
    x1max = 0
    x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in range(0, len(v)):
        xabs = abs(v[i])
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs

                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    else:
        if s2 == 0:
            norm = x3max * math.sqrt(s3)

        else:
            if s2 >= x3max:
                norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
            else:
                norm = math.sqrt(x3max * (s2 / x3max + x3max / s3))

    return norm

x_safeNorm__mutmut_mutants : ClassVar[MutantDict] = {
'x_safeNorm__mutmut_1': x_safeNorm__mutmut_1, 
    'x_safeNorm__mutmut_2': x_safeNorm__mutmut_2, 
    'x_safeNorm__mutmut_3': x_safeNorm__mutmut_3, 
    'x_safeNorm__mutmut_4': x_safeNorm__mutmut_4, 
    'x_safeNorm__mutmut_5': x_safeNorm__mutmut_5, 
    'x_safeNorm__mutmut_6': x_safeNorm__mutmut_6, 
    'x_safeNorm__mutmut_7': x_safeNorm__mutmut_7, 
    'x_safeNorm__mutmut_8': x_safeNorm__mutmut_8, 
    'x_safeNorm__mutmut_9': x_safeNorm__mutmut_9, 
    'x_safeNorm__mutmut_10': x_safeNorm__mutmut_10, 
    'x_safeNorm__mutmut_11': x_safeNorm__mutmut_11, 
    'x_safeNorm__mutmut_12': x_safeNorm__mutmut_12, 
    'x_safeNorm__mutmut_13': x_safeNorm__mutmut_13, 
    'x_safeNorm__mutmut_14': x_safeNorm__mutmut_14, 
    'x_safeNorm__mutmut_15': x_safeNorm__mutmut_15, 
    'x_safeNorm__mutmut_16': x_safeNorm__mutmut_16, 
    'x_safeNorm__mutmut_17': x_safeNorm__mutmut_17, 
    'x_safeNorm__mutmut_18': x_safeNorm__mutmut_18, 
    'x_safeNorm__mutmut_19': x_safeNorm__mutmut_19, 
    'x_safeNorm__mutmut_20': x_safeNorm__mutmut_20, 
    'x_safeNorm__mutmut_21': x_safeNorm__mutmut_21, 
    'x_safeNorm__mutmut_22': x_safeNorm__mutmut_22, 
    'x_safeNorm__mutmut_23': x_safeNorm__mutmut_23, 
    'x_safeNorm__mutmut_24': x_safeNorm__mutmut_24, 
    'x_safeNorm__mutmut_25': x_safeNorm__mutmut_25, 
    'x_safeNorm__mutmut_26': x_safeNorm__mutmut_26, 
    'x_safeNorm__mutmut_27': x_safeNorm__mutmut_27, 
    'x_safeNorm__mutmut_28': x_safeNorm__mutmut_28, 
    'x_safeNorm__mutmut_29': x_safeNorm__mutmut_29, 
    'x_safeNorm__mutmut_30': x_safeNorm__mutmut_30, 
    'x_safeNorm__mutmut_31': x_safeNorm__mutmut_31, 
    'x_safeNorm__mutmut_32': x_safeNorm__mutmut_32, 
    'x_safeNorm__mutmut_33': x_safeNorm__mutmut_33, 
    'x_safeNorm__mutmut_34': x_safeNorm__mutmut_34, 
    'x_safeNorm__mutmut_35': x_safeNorm__mutmut_35, 
    'x_safeNorm__mutmut_36': x_safeNorm__mutmut_36, 
    'x_safeNorm__mutmut_37': x_safeNorm__mutmut_37, 
    'x_safeNorm__mutmut_38': x_safeNorm__mutmut_38, 
    'x_safeNorm__mutmut_39': x_safeNorm__mutmut_39, 
    'x_safeNorm__mutmut_40': x_safeNorm__mutmut_40, 
    'x_safeNorm__mutmut_41': x_safeNorm__mutmut_41, 
    'x_safeNorm__mutmut_42': x_safeNorm__mutmut_42, 
    'x_safeNorm__mutmut_43': x_safeNorm__mutmut_43, 
    'x_safeNorm__mutmut_44': x_safeNorm__mutmut_44, 
    'x_safeNorm__mutmut_45': x_safeNorm__mutmut_45, 
    'x_safeNorm__mutmut_46': x_safeNorm__mutmut_46, 
    'x_safeNorm__mutmut_47': x_safeNorm__mutmut_47, 
    'x_safeNorm__mutmut_48': x_safeNorm__mutmut_48, 
    'x_safeNorm__mutmut_49': x_safeNorm__mutmut_49, 
    'x_safeNorm__mutmut_50': x_safeNorm__mutmut_50, 
    'x_safeNorm__mutmut_51': x_safeNorm__mutmut_51, 
    'x_safeNorm__mutmut_52': x_safeNorm__mutmut_52, 
    'x_safeNorm__mutmut_53': x_safeNorm__mutmut_53, 
    'x_safeNorm__mutmut_54': x_safeNorm__mutmut_54, 
    'x_safeNorm__mutmut_55': x_safeNorm__mutmut_55, 
    'x_safeNorm__mutmut_56': x_safeNorm__mutmut_56, 
    'x_safeNorm__mutmut_57': x_safeNorm__mutmut_57, 
    'x_safeNorm__mutmut_58': x_safeNorm__mutmut_58, 
    'x_safeNorm__mutmut_59': x_safeNorm__mutmut_59, 
    'x_safeNorm__mutmut_60': x_safeNorm__mutmut_60, 
    'x_safeNorm__mutmut_61': x_safeNorm__mutmut_61, 
    'x_safeNorm__mutmut_62': x_safeNorm__mutmut_62, 
    'x_safeNorm__mutmut_63': x_safeNorm__mutmut_63, 
    'x_safeNorm__mutmut_64': x_safeNorm__mutmut_64, 
    'x_safeNorm__mutmut_65': x_safeNorm__mutmut_65, 
    'x_safeNorm__mutmut_66': x_safeNorm__mutmut_66, 
    'x_safeNorm__mutmut_67': x_safeNorm__mutmut_67, 
    'x_safeNorm__mutmut_68': x_safeNorm__mutmut_68, 
    'x_safeNorm__mutmut_69': x_safeNorm__mutmut_69, 
    'x_safeNorm__mutmut_70': x_safeNorm__mutmut_70, 
    'x_safeNorm__mutmut_71': x_safeNorm__mutmut_71, 
    'x_safeNorm__mutmut_72': x_safeNorm__mutmut_72, 
    'x_safeNorm__mutmut_73': x_safeNorm__mutmut_73, 
    'x_safeNorm__mutmut_74': x_safeNorm__mutmut_74, 
    'x_safeNorm__mutmut_75': x_safeNorm__mutmut_75, 
    'x_safeNorm__mutmut_76': x_safeNorm__mutmut_76, 
    'x_safeNorm__mutmut_77': x_safeNorm__mutmut_77, 
    'x_safeNorm__mutmut_78': x_safeNorm__mutmut_78, 
    'x_safeNorm__mutmut_79': x_safeNorm__mutmut_79, 
    'x_safeNorm__mutmut_80': x_safeNorm__mutmut_80, 
    'x_safeNorm__mutmut_81': x_safeNorm__mutmut_81, 
    'x_safeNorm__mutmut_82': x_safeNorm__mutmut_82, 
    'x_safeNorm__mutmut_83': x_safeNorm__mutmut_83, 
    'x_safeNorm__mutmut_84': x_safeNorm__mutmut_84, 
    'x_safeNorm__mutmut_85': x_safeNorm__mutmut_85, 
    'x_safeNorm__mutmut_86': x_safeNorm__mutmut_86, 
    'x_safeNorm__mutmut_87': x_safeNorm__mutmut_87, 
    'x_safeNorm__mutmut_88': x_safeNorm__mutmut_88, 
    'x_safeNorm__mutmut_89': x_safeNorm__mutmut_89
}

def safeNorm(*args, **kwargs):
    result = _mutmut_trampoline(x_safeNorm__mutmut_orig, x_safeNorm__mutmut_mutants, args, kwargs)
    return result 

safeNorm.__signature__ = _mutmut_signature(x_safeNorm__mutmut_orig)
x_safeNorm__mutmut_orig.__name__ = 'x_safeNorm'
