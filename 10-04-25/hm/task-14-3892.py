def convert(num,sys):
    res = []
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]

n = 7*5**1984 - 6*25**777 + 5*125**333-4

