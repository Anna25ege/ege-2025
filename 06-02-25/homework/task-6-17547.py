from turtle import *
tracer(0)
pensize(2)
screensize(2000,2000)
m = 10
lt(90)
#1
color('green')
for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)

up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
#2
color('orange')
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()


