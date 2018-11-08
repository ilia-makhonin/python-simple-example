def fac_recurs(num):
    if num == 1:
        return num
    return num * fac_recurs(num - 1)