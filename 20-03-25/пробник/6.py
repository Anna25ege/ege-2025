from turtle import *
tracer(0)
screensize(1000,1000)
pensize(3)
m = 10
lt(90)
color('blue')
for i in range(9):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
bk(10*m)
rt(90)
down()
color('green')
for i in range(8):
    fd(15*m)
    lt(90)
    fd(25*m)
    lt(90)
up()
fd(6*m)
lt(90)
down()
color('orange')
for i in range(7):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        dot(3,'red')
        goto(x*m,y*m)


















update()
done()