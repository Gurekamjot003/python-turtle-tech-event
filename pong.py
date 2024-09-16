import turtle
import time

sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

hit_ball = turtle.Turtle()
hit_ball.speed(0) 
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5.0
hit_ball.dy = -5.0

left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

def paddleaup():
    y = left_pad.ycor()
    if y < 250:
        y += 40
        left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    if y > -240:
        y -= 40
        left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    if y < 250:
        y += 40
        right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    if y > -240:
        y -= 40
        right_pad.sety(y)
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

while True:
    sc.update()
    time.sleep(0.01)

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -490:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))
    if (hit_ball.xcor() > 350 and hit_ball.xcor() < 360) and \
            (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(350)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -350 and hit_ball.xcor() > -360) and \
            (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-350)
        hit_ball.dx *= -1