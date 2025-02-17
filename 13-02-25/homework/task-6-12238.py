from turtle import *
tracer(0)
screensize(1000,1000)
pensize(3)
m =15
lt(90)

color('red')
for i in range(2):
    fd(5*m)
    lt(90)
    bk(13*m)
    lt(90)
up()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
down()
color('blue')
for i in range(2):
    fd(11*m)
    rt(90)
    fd(75*m)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'black')

update()
done()