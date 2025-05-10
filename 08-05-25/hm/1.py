from itertools import permutations

graf = 'EH HG GC CF FA AE ED DB DF BG BH '.split()
matrix = '367 568 18 58 247 127 156 234'.split()

print(*range(1, 9))
for i in permutations('EHGCFADB'):
    res = []
    for x, y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
