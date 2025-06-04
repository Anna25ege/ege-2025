from itertools import permutations

graf = 'DE EA AH HC CF FG GB BD EB HG'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1, 9))
for i in permutations('DEAHCFGB'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
