def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1, 2031):
    num = 7 ** 91 + 7 ** 160 - x
    num_7 = convert(num, 7)
    if num_7.count('0') == 70:
        print(x)
   