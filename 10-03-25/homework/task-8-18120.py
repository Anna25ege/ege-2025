from itertools import product
def valid(s):
    alph1 = 'ПРСТЛ'
    alph2 = 'ОЕ'
    return s[-1] in alph2 and sum(ch in alph1 for ch in s) < 4

cnt = 0
for i, p in enumerate(product('ПРЕСТОЛ', repeat=5)):
    cnt += int(i % 2 == 0 and valid(''.join(p)))
print(cnt)