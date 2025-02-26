ans = []
for n in range(1,10000):
    r = bin(n)[2:]
    if n% 2 ==0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = (n, 2)
    if n<12:
        ans=ans.append(r,n)
print(max(ans))

