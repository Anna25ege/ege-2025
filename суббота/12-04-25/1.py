from itertools import permutations

graf ='FA AB BE ED DF DC CB CG GF'.split()
matrix='567 3457 26 256 124 134 12'.split()

print(*range(1,8))
for i in permutations('ABEDFGC'):
    res = []
    for x,y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)