def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 4*625**9 - 25**15 + 2*5**11-7

num_5=convert(num,5)
print(num_5.count('4'))
