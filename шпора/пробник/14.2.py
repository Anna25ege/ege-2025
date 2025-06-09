def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(1,2031):
    num = 7**170 + 7**100 - x
    num_7=convert(num,7)
    if num_7.count('0')==71:
        print(x)