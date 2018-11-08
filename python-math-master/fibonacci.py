def fib(limit):
    result = [0, 1]
    count = None
    while True:
        count = result[-1] + result[-2]
        result.append(count)
        if result[-1] >= limit:
            break
    return result