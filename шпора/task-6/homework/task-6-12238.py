from turtle import *

screensize(10000, 1000)
tracer(0)
m = 20
lt(90)

color('orange')
for i in range(2):
    fd(5 * m)
    lt(90)
    bk(13 * m)
    lt(90)
up()
bk(10 * m)
rt(90)
fd(9 * m)
lt(90)
down()
color('green')
for i in range(2):
    fd(11 * m)
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
