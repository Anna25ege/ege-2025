from turtle import *
screensize(1000,1000)
m = 10
pensize(3)
tracer(0)
lt(90)

color('blue')
for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
color('pink')
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(4,'white')
update()
done()