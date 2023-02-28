import math

def task_1(a, value):
    a.sort()

    id = ''
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        id = "No value"
    else:
        id = str(mid)

    return id

def task_2(n):
    flag = True
    if n < 2:
        flag = False
    if n == 2:
        flag = True
    limit = math.sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            flag = False
        i += 1

    return flag