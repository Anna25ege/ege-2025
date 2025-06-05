from turtle import *

screensize(10000, 1000)
tracer(0)
m = 20
lt(90)

color('red')
for i in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(5 * m)
lt(90)
down()
color('green')
for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        dot(6, 'white')
        goto(x * m, y * m)

update()
done()
