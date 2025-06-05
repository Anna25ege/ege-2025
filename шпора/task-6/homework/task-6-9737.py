from turtle import *

screensize(10000, 10000)
tracer(0)
m = 20
lt(90)

color('purple')
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()
color('blue')
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        dot(3, 'red')
        goto(x * m, y * m)

update()
done()
