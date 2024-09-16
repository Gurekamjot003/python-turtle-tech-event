import turtle
import random

screen = turtle.Screen()
screen.setup(500,500)
screen.title("Turtle race")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.width(5)
pen.goto(180, 250)
pen.pendown()
pen.goto(180, -250)

cor = 200

turtle1 = turtle.Turtle()
turtle1.color("yellow")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-180, cor)
cor-=50

turtle2 = turtle.Turtle()
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-180, cor)
cor-=50

turtle3 = turtle.Turtle()
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-180, cor)
cor-=50

turtle4 = turtle.Turtle()
turtle4.color("green")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-180, cor)

while True:
    
    turtle1.forward(random.randrange(0, 6))
    turtle2.forward(random.randrange(0, 6))
    turtle3.forward(random.randrange(0, 6))
    turtle4.forward(random.randrange(0, 6))
    winner = ""
    if turtle1.xcor() > 180:
        winner = "YELLOW"
    if turtle2.xcor() > 180:
        winner = "RED"
    if turtle3.xcor() > 180:
        winner = "BLUE"
    if turtle4.xcor() > 180:
        winner = "GREEN"
    if len(winner) > 0:
        pen.penup()
        pen.goto(-100, -200)
        pen.write(f"{winner} won!", font = ("Arial", 20))
        break
    

# def createTurtle(color, x):

turtle.done()