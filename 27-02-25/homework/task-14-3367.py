def convert (num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res [::-1]


ans = []
for x in range(4036):
    num = 3*16**2018 - 2*8**1028 - 3*4**1100 - 4**x - 2022
    num4 = convert(num,4)
    if num >0:
        ans.append(sum(map(int,num4)))

print(len(set(ans)))

