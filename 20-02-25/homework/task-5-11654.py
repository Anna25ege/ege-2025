ans = []
def convert (num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return  res [::-1]


for n in range(1,10000):
    r = convert(n,7)
    if  r.count('2')%2 == 0:
        r +='555'
    else:
        r = '1' + r
    r = int(r,7)
    if r < 3799:
        ans.append(n)
print(max(ans))