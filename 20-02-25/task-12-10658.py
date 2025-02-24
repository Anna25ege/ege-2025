def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(11, 10000):
    r = convert(N, 3)
    if r.count('0') + r.count('2') > r.count('1'):
        r = '22' + r
    else:
        r = '11' + r
    r = int(r, 3)
    if r > 100:
        ans.append(r)

print(min(ans))
