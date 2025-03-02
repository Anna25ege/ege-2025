def convert (num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//= sys
    return res [::-1]

num = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
ans = convert(num,5)
ans= ans.count('4')
print(ans)