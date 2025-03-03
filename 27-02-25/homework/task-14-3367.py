
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase #36 символов

for x in alph[:4]:
    num1 = 3*16**2018
    num2 = 2*8**1028
    num3 = 3*4**1100
    num4 = int(4**x)
    num5 = 2022
    num= num1 - num2 - num3 - num4 -num5
