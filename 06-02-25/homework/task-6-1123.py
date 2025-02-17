from turtle import *
tracer(0)
pensize(3)
screensize(1000,1000)
m = 15
lt(90)

color('green')
for i in range(2):
    fd(7*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(-2*m)
rt(90)
fd(9*m)
lt(90)
down()

color('blue')
for i in range(2):
    fd(8*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(5,'red')

update()
done()