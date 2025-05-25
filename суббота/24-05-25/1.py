from itertools import permutations

graf = 'AC CD DE EF FB BD DG GA AD'.split()
matrix = '37 57 147 37 26 57 12346'.split()

print(*range(1, 8))
for i in permutations('ACDEFBG'):
    res = []
    for x, y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
