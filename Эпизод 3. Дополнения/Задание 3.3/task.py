def task_1(lis):
    max = lis[0]
    max_count = lis.count(max)
    for n in lis:
        if lis.count(n) > max_count:
            max = n
        max_count = lis.count(n)

    return max

def task_2(x, y):
    correct = True
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

        if correct:
            flag = 'NO'
        else:
            flag = 'YES'

    return flag

def task_3(x, y, xc, yc, r):
    return (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r

def task_4(lis):
    counter = 0
    for i in range(1, len(lis) - 1):
        if lis[i - 1] < lis[i] > lis[i + 1]:
            counter += 1
    return counter

def task_5(key):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    itog = ''
    b = []
    with open('file.txt', 'r') as f:
        for line in f:
            line = line.lower().strip()
            for i in line:
                mesto = alpha.find(i)

                new_m = mesto + key

                itog += alpha[new_m]
            b.append(itog)
            itog = ''

    return b