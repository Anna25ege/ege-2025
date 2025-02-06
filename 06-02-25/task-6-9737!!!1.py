from turtle import *
tracer(0)# отключить анимацию
screensize(2000,2000)
lt(90)
m = 10 #мащтаб

for i in range (2):
    fd(10* m)
    rt(90)
    fd(18* m)
    rt(90)
up()
fd(5* m)
rt(90)
fd(7* m)
lt(90)
down()
for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(3,'red')




update()# с tracer
done()