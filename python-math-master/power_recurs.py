def power_recurs(num, pow):
    if pow == 1:
        return num
    result = num * power_recurs(num, pow - 1)
    return result