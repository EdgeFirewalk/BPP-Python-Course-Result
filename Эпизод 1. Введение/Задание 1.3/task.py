# Пример 1
def task_1(n):
    x = 0
    i = 1
    while i != 10:
        x += 1/i
    return x


# Пример 2
def task_2(x, n):
    n = 0
    x = 0
    b = 1
    while n != 18:
        x += b/i
        n += 2
        
    return x


# Пример 3
def task_3(n):
    x = 10
    p = 1
    i = 1
    while i <= x:
       p = p * i
       i = i + 1
    return p


# Пример 4
def task_4(x, n):
    y = 1
    i = 2
    while i <= n:
        x *= (y + i) / i
    return x

# Пример 5
def task_5(x, n):
    y = 1
    i = 1
    while i <= n:
        x += (y * i) / (2 * i)
    return x


# Пример 6
def task_6(n):
    i = 2
    y = 1
    while(i <= n):
        y *= i
        i += 2
    return y