from turtle import *

tracer(0)
screensize(1000, 1000)
lt(90)
m = 20

color('red')
for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()
color('blue')
for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        dot(6, 'white')
        goto(x * m, y * m)

update()
done()
