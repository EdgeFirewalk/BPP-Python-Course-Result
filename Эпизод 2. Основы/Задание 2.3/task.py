# todo: replace this with an actual task
def task_1(str):
    result_list = []
    for i in str.split(' '):
        if i != '':
            result_list.append(i)
    ans = len(result_list[-1])
    return ans


def task_2(str):
    result_list = []
    for i in str.split(' '):
        if i != '':
            result_list.append(i)
    for i in range(0, len(result_list) - 1, 2):
        result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
    ans = ' '.join(result_list)
    return ans


def task_3(str):
    tmp_list = []
    count = 0
    for i in str.split(' '):
        if i != ' ':
            tmp_list.append(i)
    for i in range(0, len(tmp_list) - 1):
        if tmp_list[i][-1] == tmp_list[i + 1][0]:
            count += 1

    return count
