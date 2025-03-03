ans = []
for n in range(1,10000):
    r = bin(n)[2:]
    if r.count('1')% 2==0:
        r = r + '1'
    else:
        r = r + '0'
    if int(r,2) %2 ==0:
        r = r+'10'
    else:
        r = r +'01'
    r = int(r, 2)
    if r < 1000:
        ans.append([r,n])
print(max(ans))


