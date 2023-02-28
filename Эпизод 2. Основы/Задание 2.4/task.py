def task_1(str):
    d = {}
    for i in str:
        if i.isalpha():
            if i.lower() in d:
                d[i.lower()] += 1
            else:
                d[i.lower()] = 1
    return d


def task_2(list):
    b = sum(set(list))
    return b


def task_3(cities):
    str = ''
    for i in cities:
        str += i + ',' + ' '
    str = str[0:-2] + '.'
    return str


def task_4(a, b):
    c = list(set(a) & set(b))
    return c
