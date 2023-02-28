import math

# Пример 1
def task_1(a, b):
    if a > b:
        ans = math.sqrt(a * b) - 3
    elif a == b:
        ans = math.log10(2)
    else:
        ans = third = math.log(a * a * a + 1) / b

    return ans


# Пример 2
def task_2(a, b):
    if a < b:
        ans = math.tan(a / b) + 1
    elif a == b:
        ans = math.tan(-1)
    else:
        ans = math.sqrt(a*b-5)/a

    return ans


# Пример 3
def task_3(a, b):
    if a > b:
        ans = math.log10(a*b)+21
    elif a == b:
        ans = math.tan(-5)
    else:
        ans = math.log(3*a/b)+1

    return ans


# Пример 4
def task_4(a, b):
    if a > b:
        ans = math.sqrt(a*b-1)
    if a == b:
        ans = math.log10(255)
    elif a < b:
        ans = math.tan(a-5)/b

    return ans


# Пример 5
def task_5(a, b):
    if a > b:
        ans = math.log(a / b) + 31
    if a == b:
        ans = math.tan(-25)
    elif a < b:
        ans = math.cos(a*5-1)/a

    return ans


# Пример 6
def task_6(a, b):
    if a < b:
        ans = math.sqrt(b/a+1)
    elif a == b:
        ans = math.sqrt(25)
    elif a > b:
        ans = math.log10(a*a*a-5)/b

    return ans
