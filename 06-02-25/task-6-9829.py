from turtle import *

tracer(0)
screensize(2000,2000)
m = 20

for i in range (3):
    rt(45)
    fd(10*m)
    rt(45)
rt(315)
fd(10*m)

for i in range(2):
    rt(90)
    fd(10*m)
up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()