from turtle import *
tracer(0)
screensize(1000,1000)
pensize(3)
lt(90)
m=20

color('red')
for i in range(4):
    fd(3*m)
    lt(270)
    fd(5*m)
    rt(90)
lt(270)
color('green')
for i in range(3):
    fd(5*m)
    rt(90)
    fd(3*m)
    lt(270)
up()
for x in range(-40,40):
    for y in range(-40,40):
        dot(4,'black')
        goto(x*m,y*m)


























update()
done()