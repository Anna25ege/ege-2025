ans = []
for n in range(1,10000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r +='00'
    else:
        r +='10'
    r = int(r,2)
    if r>64:
        print(n)
        break