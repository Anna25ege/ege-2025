for a in range(55):
    num1 = int('z', 36)* 55**3 + a *55**2 +int('y',36)*55 + int('x',36)
    num2 = 2*55**3 + int('x',36) * 55**2 + a*55 + int('y',36)
    num = num1 - num2
    if num % 29 == 0:
        print(num)

print(5546859-5460729)