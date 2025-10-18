def mean_abs_error(a, b):
    suma = 0
    for i in range(0, len(a)):
        suma += abs(a[i] - b[i])

    return suma / len(a)
