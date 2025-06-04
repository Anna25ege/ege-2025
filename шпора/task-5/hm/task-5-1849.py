ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    r = int(r, 2)
    if r > 52:
        ans.append(r)
print(min(ans))
