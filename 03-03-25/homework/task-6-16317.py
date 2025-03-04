from turtle import *
screensize(1000,1000)
pensize(3)
tracer(0)
m = 10
lt(90)

color('green')
for i in range(2):
    fd(21*m)
    rt(90)
    fd(27*m)
    rt(90)

up()
fd(9*m)
rt(90)
fd(10*m)
lt(90)
down()

color("orange")
for i in range(2):
    fd(86*m)
    rt(90)
    fd(47*m)
    rt(90)

up()

for x in range(-40,40):
    for y in range(-40,40):
        goto(x*m,y*m)
        dot(5,'red')

update()
done()