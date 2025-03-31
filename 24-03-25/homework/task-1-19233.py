from itertools import permutations

graf = 'BD DG GA AF FH HC CB BE DE GF EH'.split()
matrix = '234 157 147 138 268 58 23 456'.split()

print(*range(1,9))
for i in permutations('BDGAFHCE'):
    res = []
    for x,y in graf:
        res.append(str(i.index(x) + 1) in matrix[i.index(y)])
    if all(res):
        print(*i)