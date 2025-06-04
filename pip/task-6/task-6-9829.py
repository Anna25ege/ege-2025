from turtle import *

tracer(0)
screensize(10000, 10000)
m = 30
lt(90)

rt(90)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)

rt(315)
fd(10 * m)

for i in range(2):
    rt(90)
    fd(10 * m)
up()

for x in range(-40, 40):
    for y in range(-40, 40):
        dot(3, 'red')
        goto(x * m, y * m)
update()
done()
