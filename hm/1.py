from itertools import permutations

graf = 'AB BF FG GE EA AC EC CD BD FD'.split()
matrix = '235 146 145 236 137 247 56'.split()

print(*range(1, 8))
for i in permutations('ABFECDG'):
    res = []
    for x, y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
