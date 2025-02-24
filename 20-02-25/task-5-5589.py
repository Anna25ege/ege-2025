
ans = []
for N in range(1, 10_000):
    R = bin(N)[2:]
    if len(R) % 2 == 0: # кол-во символов в строке
        R = R[:len(R)//2] + '111' + R[len(R)//2:] # срез первой половины и второй чтобы в центр дописать число
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R > 4000:
        ans.append(N)

print(min(ans))
