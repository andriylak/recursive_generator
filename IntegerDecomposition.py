def decomposeTheNumber(fraction, result = [1]):
    result.append(0)
    for i in range(result[-2], fraction + 1):
        result[-1] = i
        if i == fraction:
            printDecomposition(result[1:])
        else:
            decomposeTheNumber(fraction - i, result)
    result.pop()


def printDecomposition(array):
    print('+'.join(map(str, array)))


number = int(input())
decomposeTheNumber(number)