# 1. Найти самую длинную последовательность из одинаковых чисел в списке, вывести длину и само число.
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
# '9' - 4
lst = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
d = {}
d1 = {}


def func(lst):
    c = 0
    for x in range(len(lst)-1):
        if lst[x] == lst[x+1]:
            c += 1
            z = {lst[x]: c}
            d.update(z)
        elif lst[x] != lst[x+1]:
            c = 1
            z1 = {lst[x]: c}
            d1.update(z1)
            d1.update(d)
    max_value = max(d1.values())
    max_keys = [k for k, v in d1.items() if v == max_value]
    print(d1)
    return max_keys, max_value

print(func(lst))


'''
def func(lst):
    c = 1
    li = []
    d = {}
    for x in range(len(lst)-1):
        if lst[x] == lst[x+1]:
            c += 1
            li.append(c)
            d = {c: i for i in lst}
        else:
            c = 1
    m = max(li)
    return d, d.get(m), m


print(func(lst))

'''
