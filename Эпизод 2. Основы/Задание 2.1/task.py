def task_1(N):
    factorial = 1
    if N < 0:
        print("Для отрицательных чисел факториал не определен")
    elif N == 0:
        print("Факториал 0 равен 1")
    else:
        for i in range(1, N + 1):
            factorial = factorial * i
    return factorial


def task_2(N):
    a = 0
    b = 1
    N = 7
    for i in range(3, N + 1):
        c = a + b
        a = b
        b = c

    return b


def task_3(N):
    lst = [1, N]
    for i in range(2, 1 + int(N ** 0.5)):
        if N % i == 0:
            lst.extend({N // i, i})
    return sorted(lst)
