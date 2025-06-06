from itertools import permutations

graf = 'AC CD DF FE EB BG GA AB FC'.split()
matrix = '246 16 57 15 347 127 356'.split()

print(*range(1, 8))
for i in permutations('ACFEBGD'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
