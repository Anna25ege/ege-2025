from itertools import permutations

graf = 'АГ ГЖ ЖЗ ЗД ДВ ВА АБ БВ БГ ГД ДЕ ЕЖ ЕЗ'.split()
matrix= '256 1458 478 237 126 158 348 2367'.split()

print(*range(1,9))
for i in permutations('АБВГДЕЖЗ'):
    res = []
    for x,y in graf:
        res.append(str(i.index(x)+1) in matrix[i.index(y)])
    if all(res):
        print(*i)
