ans = []
for n in range(1,10000):
    def convert(num, sys):
        res = ''
        while num:
            res += str(num % sys)
            num //= sys
        return res[::-1]
    if res.count('1')% 3 == 0:
