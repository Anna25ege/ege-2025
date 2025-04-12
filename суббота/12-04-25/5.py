ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + str(r.count('1') % 2)
    else:
        r = '1' + r + '101'
        r = int(r, 2)
        if r > 350:
            ans.append(n)
print(ans)
