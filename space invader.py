import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(500, 500)
screen.tracer(0)

# Player turtle
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -200)

# Enemy v1 turtle
v1 = turtle.Turtle()
v1.penup()
v1.speed(0)
v1.color("red")
v1.shape("square")
v1.goto(-270, 100)
v1.dx = 0.5

# Enemy v2 turtle
v2 = turtle.Turtle()
v2.penup()
v2.speed(0)
v2.color("yellow")
v2.shape("square")
v2.goto(270, 150)
v2.dx = -0.5

# Fire turtle (initialized later)
fire = turtle.Turtle()
fire.hideturtle()
fire.shape("circle")
fire.color("red")
fire.penup()
fire.speed(0)
fire.sety(-200)
fire_active = False  # Track whether fire is active or not

# Move player left
def left_button():
    player.setx(player.xcor() - 20)

# Move player right
def right_button():
    player.setx(player.xcor() + 20)

# Fire function
def fire_bullet():
    global fire_active
    if not fire_active:  # If no active fire, create one
        fire_active = True
        fire.setx(player.xcor())  # Set fire at player's position
        fire.sety(player.ycor())  # Start fire at player's position
        fire.showturtle()

# Game loop
def game_loop():
    global fire_active

    # Move enemies
    v1.setx(v1.xcor() + v1.dx)
    v2.setx(v2.xcor() + v2.dx)

    # Boundary checks for v1
    if v1.xcor() > 270:
        v1.setx(-270)
    # Boundary checks for v2
    if v2.xcor() < -270:
        v2.setx(270)

    # Move fire upwards if active
    if fire_active:
        fire.sety(fire.ycor() + 10)
        if fire.ycor() > 250:  # Reset fire if it goes off screen
            fire.hideturtle()
            fire_active = False

    # Check for collision between fire and v1
    if fire.distance(v1) < 20:
        v1.setx(-270)  # Reset v1's position
        fire.hideturtle()  # Hide fire
        fire_active = False  # Reset fire state

    # Check for collision between fire and v2
    if fire.distance(v2) < 20:
        v2.setx(270)  # Reset v2's position
        fire.hideturtle()  # Hide fire
        fire_active = False  # Reset fire state

    screen.update()  # Update screen
    screen.ontimer(game_loop, 20)  # Run game loop continuously

# Key bindings
screen.listen()
screen.onkey(left_button, "Left")
screen.onkey(right_button, "Right")
screen.onkey(fire_bullet, "space")

# Start game loop
game_loop()

turtle.done()
