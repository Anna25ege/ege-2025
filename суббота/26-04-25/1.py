from itertools import permutations

graf = 'AE EH HG GC CF FA ED DB BH BG DF'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1, 9))
for i in permutations('AEHGCFDB'):
    res = []
    for x, y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)
