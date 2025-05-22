from turtle import *
tracer(0)
screensize(1000, 1000)
pensize(3)
m = 10
lt(90)
color('green')
for i in range(2):
    fd(13 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(9 * m)
lt(90)
down()
color('pink')
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