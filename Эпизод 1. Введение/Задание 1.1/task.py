import math

# Пример 1
def task_1(a, d, c):
    ans = (c - d / 5 + math.sqrt(321)) / (1 + a * 3)
    return ans


# Пример 2
def task_2(a, d, c):
    ans = (math.log10(c/3)-d+25)/(a*5-1)
    return ans


# Пример 3
def task_3(a, d, c):
    ans = (c/2+math.log(d)-35)/(a*5+1)
    return ans


# Пример 4
def task_4(a, d, c):
    ans = (math.tan(c)+d/32)/(a/3+1)
    return ans


# Пример 5
def task_5(a, d, c):
    ans = (c/5-d+1)/(c+math.tan(2*a))
    return ans


# Пример 6
def task_6(a, d, c):
    ans = (math.sqrt(25*c)+d-3)/(d-a*a+1)
    return ans


# Пример 7
def task_7(a, d, c):
    ans = (5*math.log10(c)+3*d-32)/(a*a+1)
    return ans


# Пример 8
def task_8(a, d, c):
    ans = (c*d-math.log(4*3*a))/(c+a-1)
    return ans
