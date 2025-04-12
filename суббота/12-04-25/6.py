from turtle import *

tracer(0)
screensize(1000, 1000)
pensize(3)
lt(90)
m = 10

color('pink')
for i in range(4):
    fd(16 * m)
    lt(90)
    fd(20 * m)
    lt(90)
up()
fd(4 * m)
lt(90)
fd(8 * m)
rt(180)
down()
color('blue')
for i in range(3):
    fd(35 * m)
    lt(90)
    fd(6 * m)
    lt(90)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        dot(6, 'white')
        goto(x * m, y * m)

update()
done()
