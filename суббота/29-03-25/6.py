from turtle import *
tracer(0)
screensize(1000,1000)
pensize(3)
m = 10
lt(90)
color('green')
for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()
color('red')
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
up()

for x in range(-40,40):
    for y in range(-40,40):
        dot(5,'white')
        goto(x*m,y*m)

done()
update()

15