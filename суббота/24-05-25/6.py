from turtle import *

screensize(10000, 100000)
tracer(0)
pensize(3)
m = 10
lt(90)

color('green')
for i in range(2):
    fd(21 * m)
    rt(90)
    fd(27 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
fd(10 * m)
lt(90)
down()
color('blue')
for i in range(2):
    fd(86 * m)
    rt(90)
    fd(47 * m)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        dot(5, 'red')
        goto(x * m, y * m)
update()
done()
