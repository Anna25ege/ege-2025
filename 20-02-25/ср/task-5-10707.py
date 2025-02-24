def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1,10000):
    r = convert(N, 6)
    if N % 3 == 0:
        r += r[:2]
    else:
        r += convert(N % 3 * 10, 6)
    r = int(r, 6)
    if r > 680:
        ans.append(r)

print(min(ans))
