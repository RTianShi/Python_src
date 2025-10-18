def dec(array1, array2):
    #Preconditions.checkArgument(len(array1) == len(array2), "array1.length != array2.length")
    for index in range(len(array1)):
        array1[index] -= array2[index]
            