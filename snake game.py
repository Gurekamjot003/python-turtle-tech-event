import turtle
import random
import time

delay=0.1
score=0
hscore=0

scrn=turtle.Screen()
scrn.title("SNAKE GAME")
scrn.bgcolor("black")
scrn.setup(600,600)
scrn.tracer(0)

border=turtle.Turtle()
border.penup()
border.speed(0)
border.pencolor("white")
border.pensize(5)
border.goto(-270,270)
border.pendown()
for i in range(4):
    border.forward(540)
    border.right(90)
border.hideturtle()

text=turtle.Turtle()
text.speed(0)
text.penup()
text.color("white")
text.goto(0,270)
text.write("SCORE: {} HIGH SCORE: {}".format(score,hscore),align="center",font=("arial",24,"normal"))
text.hideturtle()

head=turtle.Turtle()
head.speed(0)
head.penup()
head.color("white")
head.shape("square")
head.goto(0,0)
head.direction="stop"

segments=[]

food=turtle.Turtle()
food.speed(0)
food.penup()
food.color("red")
food.shape("circle")
food.goto(100,100)

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_right():
    if head.direction!="left":
        head.direction="right"
def go_left():
    if head.direction!="right":
        head.direction="left"
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
scrn.listen()
scrn.onkey(go_up,"Up")
scrn.onkey(go_down,"Down")
scrn.onkey(go_right,"Right")
scrn.onkey(go_left,"Left")

while True:
    scrn.update()
    if head.xcor()>270 or head.xcor()<-270 or head.ycor()<-270 or head.ycor()>270:
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        score=0
        text.clear()
        text.write("SCORE: {} HIGH SCORE: {}".format(score,hscore),align="center",font=("arial",24,"normal"))
    if head.distance(food)<20:
        food.goto(random.randint(-260,260),random.randint(-260,260))
        ns=turtle.Turtle()
        ns.speed(0)
        ns.color("gray")
        ns.shape("square")
        ns.penup()
        segments.append(ns)

        score+=1
        if score>hscore:
            hscore=score
        text.clear()
        text.write("SCORE: {} HIGH SCORE: {}".format(score,hscore),align="center",font=("arial",24,"normal"))
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(),segments[i-1].ycor())
    if len(segments)>0:
        segments[0].goto(head.xcor(),head.ycor())
    move()
    for segment in segments:
        if segment.distance(head)<20:
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score=0
            text.clear()
            text.write("SCORE: {} HIGH SCORE: {}".format(score,hscore),align="center",font=("arial",24,"normal"))
    time.sleep(delay)
turtle.done()