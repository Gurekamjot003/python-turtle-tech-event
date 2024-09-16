import turtle
import random
import time

scrn=turtle.Screen()
scrn.title(" ")
scrn.bgcolor("black")
scrn.setup(600,600)
scrn.tracer(0)

text=turtle.Turtle()
text.speed(0)
text.penup()
text.color("white")
text.goto(0,270)
text.write("",align="center",font=("arial",20,"normal"))
text.hideturtle()

finish=turtle.Turtle()
finish.speed(0)
finish.penup()
finish.goto(-270,270)
finish.pensize(5)
finish.pencolor("white")
finish.pendown()
finish.forward(540)
finish.hideturtle()

v1=turtle.Turtle()
v1.penup()
v1.speed(0)
v1.color("red")
v1.shape("square")
v1.goto(-270,-200)
v1.dx=0.5

v2=turtle.Turtle()
v2.penup()
v2.speed(0)
v2.color("yellow")
v2.shape("square")
v2.goto(270,-100)
v2.dx=-0.5

v3=turtle.Turtle()
v3.penup()
v3.speed(0)
v3.color("green")
v3.shape("square")
v3.goto(-270,0)
v3.dx=0.5

v4=turtle.Turtle()
v4.penup()
v4.speed(0)
v4.color("pink")
v4.shape("square")
v4.goto(270,100)
v4.dx=-0.5

v5=turtle.Turtle()
v5.penup()
v5.speed(0)
v5.color("grey")
v5.shape("square")
v5.goto(-270,250)
v5.dx=0.5

head=turtle.Turtle()
head.speed(0)
head.penup()
head.shape("turtle")
head.color("white")
head.goto(0,-270)
head.direction="stop"

def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_right():
    head.direction="right"
def go_left():
    head.direction="left"
def move():
    if head.direction=="up":
        head.sety(head.ycor()+0.2)
    if head.direction=="down":
        head.sety(head.ycor()-0.2)
    if head.direction=="right":
        head.setx(head.xcor()+0.2)
    if head.direction=="left":
        head.setx(head.xcor()-0.2)
scrn.listen()
scrn.onkey(go_up,"Up")
scrn.onkey(go_down,"Down")
scrn.onkey(go_right,"Right")
scrn.onkey(go_left,"Left")

while True:

    scrn.update()

    v1.setx(v1.xcor()+v1.dx)
    v2.setx(v2.xcor()+v2.dx)
    v3.setx(v3.xcor()+v3.dx)
    v4.setx(v4.xcor()+v4.dx)
    v5.setx(v5.xcor()+v5.dx)

    if v1.xcor()>270:
        v1.setx(-270)
    if v2.xcor()<-270:
        v2.setx(270)
    if v3.xcor()>270:
        v3.setx(-270)
    if v4.xcor()<-270:
        v4.setx(270)
    if v5.xcor()>270:
        v5.setx(-270)

    if head.ycor()>270:
        text.clear()
        text.write("YOU WON",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
    move()
    if head.distance(v1)<20:
        text.clear()
        text.write("YOU LOST",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
    if head.distance(v2)<20:
        text.clear()
        text.write("YOU LOST",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
    if head.distance(v3)<20:
        text.clear()
        text.write("YOU LOST",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
    if head.distance(v4)<20:
        text.clear()
        text.write("YOU LOST",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
    if head.distance(v5)<20:
        text.clear()
        text.write("YOU LOST",align="center",font=("Arial",20,"normal"))
        time.sleep(5)
        head.goto(0,-270)
        break
turtle.done()