from itertools import permutations

graf = 'DF FE EC CA AB BD FG CG DG'.split()
matrix = '457 46 567 12 136 235 13'.split()

print(*range(1, 8))
for i in permutations('DFECABG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
