from turtle import *
tracer(0)
pensize(2)
screensize(1000,1000)

lt(90)
m = 15

#1
color('green')
for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)

up()
fd(1)
rt(90)
fd(1)
lt(90)
down()

#2
color('orange')
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

up()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m,y*m)
        dot(10,'white')

update()
done()
