from turtle import *

tracer(0)
screensize(10000, 100000)
pensize(3)
m = 10
lt(90)

color('pink')
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
color('purple')
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        dot(4, 'red')
        goto(x * m, y * m)
update()
done()
