with open('9_14250 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file]


def f1(pip):
    return len(pip) == len(set(pip))


def f2(pip):
    return (max(pip) - min(pip)) ** 3 >= (sum(pip) - max(pip) - min(pip)) ** 2


summ = 0
cnt = 0
for i in data:
    cnt += 1
    if f1(i) and f2(i):
        summ += cnt
print(summ)
