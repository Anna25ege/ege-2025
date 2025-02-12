from turtle import *
tracer(0)
pensize(2)
screensize(2000,20000)
lt(90)
m = 10

for i in range(2):
    fd(5*m)
    rt(90)
    fd(15*m)
    rt(90)
up()

fd(7*m)
rt(90)
fd(12*m)
lt(90)

down()

for i in range(2):
    fd(65*m)
    rt(90)
    fd(120)
    rt(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(5,'white')

update()
done()