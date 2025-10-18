def clip(a, loweLim, upperLim):
    r = [0] * len(a)  # 预分配与 a 相同长度
    for i in range(0, len(a)):
        if a[i] < loweLim:
            r[i] = loweLim
        else:
            if a[i] > upperLim:
                r[i] = upperLim
            else:
                r[i] = a[i]

    return r
