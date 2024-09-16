import turtle
import time
import random

scrn=turtle.Screen()
scrn.title(" ")
scrn.bgcolor("black")
scrn.setup(600,600)


text=turtle.Turtle()
text.speed(0)
text.penup()
text.color("white")
text.goto(0,270)
text.write("",align="center",font=("arial",20,"normal"))
text.hideturtle()

border=turtle.Turtle()
border.penup()
border.speed(0)
border.pencolor("white")
border.pensize(5)
border.goto(-270,-200)
border.pendown()
border.forward(540)
border.hideturtle()

head=turtle.Turtle()
head.speed(0)
head.penup()
head.shape("turtle")
head.color("white")
head.goto(-200,-200)
head.jp= "no"

v1=turtle.Turtle()
v1.penup()
v1.speed(0)
v1.color("red")
v1.shape("square")
v1.shapesize(stretch_len=5,stretch_wid=1)
v1.goto(200,-200)
v1.dx=0.1

v2=turtle.Turtle()
v2.penup()
v2.speed(0)
v2.color("yellow")
v2.shape("square")
v2.shapesize(stretch_len=3,stretch_wid=5)
v2.goto(270,-200)
v2.dx=-0.1

def jump():
    if head.ycor() == -200:
        for _ in range (10):
            head.sety(head.ycor()+8)

scrn.listen()
scrn.onkey(jump, "space")


while True:
    scrn.update()
    v1.setx(v1.xcor() + v1.dx)
    v1.setx(v2.xcor() + v2.dx)
    gravity = 0.8
    head.sety(head.ycor()-gravity)
    if head.ycor()< -200:
        head.sety(-200)
    





turtle.done()