def convert (num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//= sys
    return res [::-1]

num = 6*343**1156 - 5 * 49**1147 + 4* 7**1153 - 875
ans = convert(num,7)
num = str(num)
ans = sum(map(int,num))
print(ans)

