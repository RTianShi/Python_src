def euc_Dist(array1, array2):
    Sum = 0.0
    for i in range(len(array1)):
        Sum += (array1[i] - array2[i]) ** 2.0
    return Sum ** 0.5