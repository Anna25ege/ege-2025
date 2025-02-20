ans = []
for n in range(1,10000): # 6 = (6,7)
    r = bin(n)[2:]
    if r.count('1')% 2 == 0:#2 система 100110 = 3
        r ='10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r,2)
    if r >=16:
       ans.append(n)
print(min(ans))

