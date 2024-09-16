import turtle 

screen = turtle.Screen()
screen.title("tictactoe")
screen.setup(600, 600)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(5)
pen.hideturtle()

pen.penup()
pen.goto(-100, 300)
pen.pendown()
pen.goto(-100, -300)

pen.penup()
pen.goto(100, 300)
pen.pendown()
pen.goto(100, -300)

pen.penup()
pen.goto(-300, 100)
pen.pendown()
pen.goto(300, 100)

pen.penup()
pen.goto(-300, -100)
pen.pendown()
pen.goto(300, -100)

grid = [
    ["","",""],
    ["","",""],
    ["","",""]
]

current_player = "X"

def draw_x(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.goto(x+50, y+50)
    pen.penup()
    pen.goto(x, y+50)
    pen.pendown()
    pen.goto(x+50, y)

def draw_o(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.circle(50)
    pen.penup()

def display_grid():
    global grid
    x = -180
    y = 180
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                draw_x(x + j*200,y -i*200)
            elif grid[i][j] == "O":
                draw_o(x +j*200,y-i*200)

def check_winner():
    global current_player
    global grid

    winner = False
    for i in range(3):
        if grid[i][0] == current_player and grid [i][1] ==current_player and grid[i][2] == current_player:
            winner = True
    for i in range(3):
        if grid[0][i] == current_player and grid [1][i] ==current_player and grid[2][i] == current_player:
            winner = True

    if grid[0][0] == current_player and grid[1][1] == current_player and grid[2][2] == current_player:
        winner = True
    if grid[0][2] == current_player and grid[1][1] == current_player and grid[2][0] == current_player:
        winner = True
    
    return winner
        


def handle_click(x,y):
    row = -1
    col = -1
    global grid
    global current_player
    if x < -100 and x>=-300:
        col = 0
    elif x < 100 and x>=-100:
        col = 1
    elif x < 300 and x>=100:
        col = 2
    if y < -100 and y>=-300:
        row = 2
    elif y < 100 and y>=-100:
        row = 1
    elif y < 300 and y>=100:
        row = 0

    if grid[row][col] == "":
        grid[row][col] = current_player
    
    if check_winner():
        print(f"{current_player} won!")
        screen.bye()

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    
    display_grid()


screen.listen()
screen.onclick(handle_click)

turtle.done()