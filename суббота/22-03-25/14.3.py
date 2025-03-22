from string import digits,ascii_uppercase
def convert (num,sys):
    alph = digits+ ascii_uppercase
    res =''
    while num:
        res += alph[num % sys]
        num//=sys
    return res [::-1]

n = 3*2187**2020 + 3*729**2021- 2*81**2022 + 27**2023 - 4*3**2024 -2029
cnt = 0
while n:
    if n % 27 > 9 :
        cnt+=1
    n//=27
print(cnt)