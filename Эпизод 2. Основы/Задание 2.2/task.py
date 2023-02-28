import math

# Пример 1
def task_1(A):
    sum = 0
    for i in range(0, len(A)):
        if A[i] > 0:
            sum += A[i]

    return sum


# Пример 2
def task_2(A):
    avg = sum(A) / len(A)
    return avg


# Пример 3
def task_3(A):
    dispersion = 0
    avg = sum(A) / len(A)
    for i in A:
        dispersion += (i - avg) ** 2
    dispersion = math.sqrt(dispersion / len(A))

    return dispersion
