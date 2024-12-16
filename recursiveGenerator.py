def gen_k_tice(k, n, result=[]):
    result.append(0)
    for i in range(n):
        result[-1] = i
        if len(result) == k:
            print(result)
        else:
            gen_k_tice(k, n, result)
    result.pop()


#gen_k_tice(2, 3)


def gen_k_tice_no_rep(k, n, result=[]):
    result.append(-1)
    for i in range(n + 1):
        if (i not in result):
            result[-1] = i
            if len(result) == k:
                print(result)
            else:
                gen_k_tice_no_rep(k, n, result)
    result.pop()


#gen_k_tice_no_rep(3, 3)


def gen_growing_sequence(k, n, result=[-1]):
    result.append(-1)
    for i in range(result[-2] + 1, n - k + len(result)):
        result[-1] = i
        if len(result) == k + 1:
            print(result[1:])
        else:
            gen_growing_sequence(k, n, result)
    result.pop()


#gen_growing_sequence(3, 5)

def gen_non_decreasing_sequence(k, n, result = [0]):
    result.append(-1)
    for i in range(result[-2], n + 1):
        result[-1] = i
        if len(result) == k + 1:
            print(result[1:])
        else:
            gen_non_decreasing_sequence(k, n, result)
    result.pop()

gen_non_decreasing_sequence(3,5)

def gen_sequence_from_set(k, items, result = []):
    result.append(-1)
    for element in items:
        if len(result) == k:
            print(result)
        else:
            gen_sequence_from_set(k, items, result)
    result.pop()

#gen_sequence_from_set(3, [3, -2, 5, "x"])

def gen_sequence_from_set_limited_rep_dic(k, dic, result=[]):
    result.append(-1)
    for key in dic:
        if dic[key] >= 1:
            result[-1] = key
            if len(result) == k:
                print(result)
            else:
                dic[key] -= 1
                gen_sequence_from_set_limited_rep_dic(k, dic, result)
                dic[key] += 1
    result.pop()

#k = 3

#d = {1: 2, "x": 5, 0: 1}

#gen_sequence_from_set_limited_rep_dic(k, d)

def decompose_the_number(n, result=[]):
    result.append(-1)
    for i in range(1, n+1):
        result[-1] = i
        if sum(result) == n:
            print(result)
        elif sum(result) < n:
            decompose_the_number(n, result)
        else:
            break
    
    result.pop()

#decompose_the_number(4)

def decompose_the_number2(fraction, result=[]):
    result.append(-1)
    for i in range(1, fraction + 1):
        result[-1] = i
        if i == fraction:
            print(result)
        else:
            decompose_the_number2(fraction - i, result)
    result.pop()

#decompose_the_number2(4)

def decompose_the_number_by_k(fraction, k, result = []):
    result.append(-1)
    for i in range(1, fraction + 1):
        result[-1] = i
        if (fraction == i) and (k==1):
            print(result)
        else:
            if k > 0:
               decompose_the_number_by_k(fraction - i, k - 1, result)
    result.pop()

#decompose_the_number_by_k(6, 3)

def decompose_the_number_non_decreasing(fraction, result = [1]):
    result.append(-1)
    for i in range(result[-2], fraction+1):
        result[-1] = i
        if fraction == i:
            print(result[1:])
        else:
            decompose_the_number_non_decreasing(fraction - i, result)
    result.pop()

#decompose_the_number_non_decreasing(5)



