from turtle import *
from math import *
from time import *
tur=Turtle()
scr=Screen()
scr.screensize(300,300)
x,y=0,0
tur.speed(0)
tur.hideturtle()
tur,hideturtle()
tur.penup()
tur.goto(0,-100)
tur.pendown()
tur.begin_fill()
tur.fillcolor('lightblue')
tur.circle(100)
tur.penup()
tur.goto(0,-75)
tur.down()
tur.circle(75)
tur.end_fill()
tur.penup()
tur.home()
turm=Turtle()
turh=Turtle()

for i in range(12):
    tur.setheading(60-30*i)
    tur.forward(85)
    tur.write(i+1)
    tur.home()   

def hour_arm(h):
    turh.speed(0)
    turh.penup()
    turh.home()
    turh.pendown()
    turh.pencolor('black')
    turh.pensize('3')
    turh.setheading(90)
    turh.right(h*360/60)
    turh.forward(45)
    
    
def min_arm(m):
    if m>0:
        turm.undo()
    turm.speed(0)
    turm.penup()
    turm.home()
    turm.pendown()
    turm.pensize('2')
    turm.setheading(90)
    turm.right(m*360/60)
    turm.forward(55)
    
    if m==60:    
        hour_arm(h)
        h+=1
        m=1
    
def second_arm():
    s=0;m=0
    while True:
        tur.speed(0)
        tur.penup()
        tur.home()
        tur.pendown()
        tur.pencolor('white')
        tur.pensize('2')
        #x=60*sin(6*s)
        #y=60*cos(6*s)
        #tur.goto(x,y)
        tur.setheading(90)
        tur.right(s*360/60)
        tur.forward(68)
        sleep(1)
        s+=1
        tur.undo()
        if s==60:
            s=1
            m+=1
            min_arm(m)           
            continue

s,m,stm=0,0,0  
min_arm(0)
hour_arm(10) 
second_arm()






scr.exitonclick()
done()