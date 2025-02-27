ans = []
for n in range(1,10000):
    r = oct(n)[2:]
    if n % 7 ==0:
        r = r + r[-2:]
    else:
        r = r + oct(n %7 * 7)[2:]
    r = int(r,8)
    if r < 3000:
        ans.append(r)
print(len(ans))