def decomposeTheNumber(n, result=[]):
    result.append(-1)
    for i in range(1, n + 1):
        result[-1] = i
        if sum(result) == n:
            print(result)
        elif sum(result) < n:
            decomposeTheNumber(n, result)
        else:
            break

    result.pop()


def decomposeTheNumber2(fraction, result=[]):
    result.append(-1)
    for i in range(1, fraction + 1):
        result[-1] = i
        if i == fraction:
            print(result)
        else:
            decomposeTheNumber2(fraction - i, result)
    result.pop()


def decomposeTheNumberByK(fraction, k, result=[]):
    result.append(-1)
    for i in range(1, fraction + 1):
        result[-1] = i
        if (fraction == i) and (k == 1):
            print(result)
        else:
            if k > 0:
                decomposeTheNumberByK(fraction - i, k - 1, result)
    result.pop()


def decomposeTheNumberNonDecreasing(fraction, result=[1]):
    result.append(-1)
    for i in range(result[-2], fraction + 1):
        result[-1] = i
        if fraction == i:
            print(result[1:])
        else:
            decomposeTheNumberNonDecreasing(fraction - i, result)
    result.pop()
