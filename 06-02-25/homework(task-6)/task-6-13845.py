from turtle import *

tracer(0)
pensize(2)
screensize(1000,1000)
m = 10
lt(90)

#1
up()
for i in range(10):
    rt(120)
    fd(10*m)
down()
color('green')
for i in range(7):
    fd(15*m)
    rt(90)
color('orange')
for i in range(5):
    rt(60)
    fd(20*m)
    rt(30)

up()

for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(4,'red')

























update()
done()