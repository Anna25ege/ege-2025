ans = []
for n in range(1,10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r= '1' + r + str(r.count('1')%2)
    else:
        r = r+ '0' + str(r.count('1')%2)
    r = int(r,2)
    if r > 100:
        ans.append([r,n])

print(min(ans))