from itertools import permutations

graf = 'CE EG GF FA AC CD DH HE AB BF'.split()
matrix = '68 47 45 237 368 15 248 157'.split()

print(*range(1, 9))

for i in permutations('CEGFABDH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
