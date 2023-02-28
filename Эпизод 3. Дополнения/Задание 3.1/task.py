import math

def task_1(text):
    mas = text.rstrip('.').split('.')

    d = {sent.strip(): len(sent.strip().split(' ')) for sent in mas}

    return d

def task_2(x1, y1, x2, y2):
    ans = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return ans