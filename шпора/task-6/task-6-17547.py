from turtle import *

tracer(0)
screensize(10000, 10000)
m = 20
lt(90)

color('green')
for i in range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
color('orange')
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        dot(3, 'red')
        goto(x * m, y * m)
done()
update()
