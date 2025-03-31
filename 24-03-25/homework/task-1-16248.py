from itertools import permutations

graf = 'BC CD DF FG EG EF ED EC BA CA AD'.split()
matrix = '347 3456 1245 1237 236 25 14'.split()

print(*range(1,8))
for i in permutations('BCDFGAE'):
    res = []
    for x,y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
