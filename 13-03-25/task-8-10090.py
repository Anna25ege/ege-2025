from itertools import *
cnt = 0
c1 = '0246'
c2 = '1357'
for p in permutations('0234567', 5):
    s = ''.join(p)
    for i in range(len(s)-1):
        if s[i] in c1 and s[i+1] in c1 or s[i] in c2 and s[i+1] in c2:
            break
    else:
        if s[0] != '0':
            cnt += 1
print(cnt)
