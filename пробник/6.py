from turtle import*
tracer(0)
pensize(3)
screensize(1000,1000)
m = 10
lt(90)

color('blue')
for i in range(9):
    fd(17*m)
    lt(90)
    fd(8*m)
    lt(90)
    fd(17*m)
up()
lt(90)
fd(3*m)
rt(90)
fd(5*m)
lt(90)
down()
color('green')
for i in range(4):
    fd(97*m)
    rt(90)
    fd(132*m)
    rt(90)
up()

for x in range(-40,40):
    for y in range(-40,40):
        dot(5,'white')
        goto(x*m,y*m)














update()
done()
