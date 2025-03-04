from string import digits, ascii_uppercase
def convert (num,sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num%sys]
        num//= sys
    return res [::-1]

num = 3*3125**8 + 2*625**7 - 4*625**6 +3*125**5 - 2*25**4 - 2024
num = convert(num,25)
num = num.count('0')
print(num)
