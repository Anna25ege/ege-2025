from itertools import permutations

graf = 'AE EH HG GC CF FA DF DB BH BG '.split()
matrix = '367 568 18 58 247 127 156 234'.split()

print(*range(1, 9))

for i in permutations('EHGCFADB'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graf):
        print(*i)
