def cal_AbsoluteDiff(z):
    if z == None:
        return None

    if len(z) == 0:
        return None

    zAbs = []
    for i in z:
        zAbs.append(abs(i))
    return zAbs
