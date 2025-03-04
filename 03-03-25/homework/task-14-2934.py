from string import digits, ascii_uppercase
def convert (num,sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 6*512**180 + 7*64**181 + 3*8**184 + 5*8**125 - 65
num = convert(num,64)
num = num.count('0')
print(num)