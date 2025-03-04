def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//= sys
    return res [::-1]

for x in range(10000,0,-1):
    num = 6**900 + 6**10 - x
    r = convert(num,6)
    if r.count('3') == r.count('5'):
        print(x)
        break
