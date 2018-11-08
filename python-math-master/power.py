def power(num, pow):
    result = num
    for i in range(1, pow):
        result *= num
    return result