ans = []
for n in range(1,10000):
    R = bin(n)[2::]
    if n%2 == 0:
        R = '1' + R + '0'
    else:
        R = '11' + R + '11'
    R = int(R,2)
    if R > 52:
        ans.append(R) # добавить элеиетн в конец списка

print(min(ans))
