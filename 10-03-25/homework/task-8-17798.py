from itertools import product

alph = sorted('МИНУС')

cnt=0

for i in product(alph,repeat=4):
    i = ''.join(i)
    cnt+=1
    num1='М', 'Н', 'С'
    num2 = 'И' , 'У'
    if  i in alph:
        num1 <= num2
        print(cnt,i)


