def sim_num(limit):
    result = []
    for i in range(2, limit + 1):
        if isSimple(i):
            result.append(i)
    return result

def isSimple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True