#1
num = int(input('ведите число'))
cnt = 0
while num > 0:
    num = num//10
    cnt += 1
    print('колличество разрядов:', cnt)

#2
num = int(input('ведите число'))
while num > 0:
    num = num % 10
    num2 = num + num
    num = num // 10
print("произведение цифр:", num2)

#3
#4
num = int(input('ведите число'))
if (num>1) and (num/1) and(num/num):
    print('true')
#5