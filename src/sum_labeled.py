def sum_labeled(a, i, j):

    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        return -1000
    else:
        return a[i] + a[j] / 2