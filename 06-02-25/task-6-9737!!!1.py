from turtle import *
tracer(0) # отключить анимацию
pensize(2) # Размер пера
screensize(2000,2000) #размер экрана

lt(90)#база
m = 10 #маштаб (меняется)

#первая фигура
color('green') # необязательно
for i in range (2):
    fd(10* m)
    rt(90)
    fd(18* m)
    rt(90)

#перемещение
up()
fd(5* m)
rt(90)
fd(7* m)
lt(90)
down()

color('orange')
#вторая фигура
for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

up() #всегда!!!
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m,y*m)
        dot(4,'red')




update()# с tracer
done() # всегда пишется!!!!!