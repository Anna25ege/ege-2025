from itertools import permutations

graf = 'AD DE EG GC CF FA AB BE BF'.split()
matrix = '37  367 128 56 34 247 126'.split()

print(*range(1, 8))

for i in permutations('ADEGCFB'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
