def fib_rec(sequence, limit):
    result = sequence
    count = result[-1] + result[-2]
    if count >= limit:
        return result
    result.append(count)
    fib_rec(result, limit)
    return result