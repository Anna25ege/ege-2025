from turtle import *
tracer(0)
screensize(1000, 1000)
pensize(3)
m = 20
lt(90)

for i in range(15):
    fd(4 * m)
    rt(60)

up()

for x in range(40, -40):
    for y in range(40, -40):
        dot(3, 'red')
        goto(x * m, y * m)


update()
done()
