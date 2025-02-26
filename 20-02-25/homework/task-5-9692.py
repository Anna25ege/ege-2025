ans = []
for n in range(12,13):
    r = bin(n)[2:]
    if n % 2 ==0:
        r +=  str(r.count('1')) + r + str(r.count('1')%2)
    else:
        r += r + '0' + str(r.count('1'))
        r = int(r, 2)
        if r < 256 and r == max:
            ans.append(n)

print(min(ans))


