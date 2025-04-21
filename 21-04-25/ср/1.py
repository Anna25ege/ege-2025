from itertools import product,permutations

graf='BH HF FD DC CG GE EC GF EA AB AH '.split()
matrix = '247 148 578 126 38 47 136 235'.split()

print(*range(1,9))
for i in permutations('ABHFDCGE'):
    res = []
    for x,y in graf:
        res.append(str(i.index(x)+1)in matrix[i.index(y)])
    if all(res):
        print(*i)