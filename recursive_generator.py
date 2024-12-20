def genTuple(k, n, result=[]):
    result.append(0)
    for i in range(n + 1):
        result[-1] = i
        if len(result) == k:
            print(result)
        else:
            genTuple(k, n, result)
    result.pop()


def genTupleNoRep(k, n, result=[]):
    result.append(-1)
    for i in range(n + 1):
        if i not in result:
            result[-1] = i
            if len(result) == k:
                print(result)
            else:
                genTupleNoRep(k, n, result)
    result.pop()


def genGrowingSequence(k, n, result=[-1]):
    result.append(-1)
    for i in range(result[-2] + 1, n - k + len(result)):
        result[-1] = i
        if len(result) == k + 1:
            print(result[1:])
        else:
            genGrowingSequence(k, n, result)
    result.pop()


def genNonDecreasingSequence(k, n, result=[0]):
    result.append(-1)
    for i in range(result[-2], n + 1):
        result[-1] = i
        if len(result) == k + 1:
            print(result[1:])
        else:
            genNonDecreasingSequence(k, n, result)
    result.pop()


def genSequenceFromSet(k, items, result=[]):
    result.append(-1)
    for element in items:
        if len(result) == k:
            print(result)
        else:
            genSequenceFromSet(k, items, result)
    result.pop()


def genSequenceFromSetLimitedRep(k, dic, result=[]):
    result.append(-1)
    for key in dic:
        if dic[key] >= 1:
            result[-1] = key
            if len(result) == k:
                print(result)
            else:
                dic[key] -= 1
                genSequenceFromSetLimitedRep(k, dic, result)
                dic[key] += 1
    result.pop()
