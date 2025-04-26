from turtle import *

tracer(0)
screensize(1000000, 1000000)
pensize(2)
m = 10
lt(90)

color('pink')
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
color('blue')
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        dot(4, 'black')
        goto(x * m, y * m)
update()
done()
