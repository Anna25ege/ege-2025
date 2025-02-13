from turtle import *

tracer(0)
lt(90)
m = 10

color('red')
for i in range (2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(8*m)
rt(90)
bk(3*m)
lt(90)
down()
color('green')
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)
up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()