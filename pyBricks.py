# small bricks breaker in Python 3 for Openclassrooms project
# by Tom NICOLAS

import turtle
import random


# Window Setup

wn = turtle.Screen()
wn.title('-- Bricks Breaker -- by Tom Nicolas')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_len=5, stretch_wid=0.5)
paddle.color('white')
paddle.penup()
paddle.goto(0,-250)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.color('white')
ball.penup()
ball.goto(0,-239)
ball.setheading(random.randint(20,160))
ballspeed = 0.18

# Score
score = 15
scoreT = turtle.Turtle()
scoreT.speed(0)  
scoreT.color("grey")
scoreT.shape("blank")
scoreT.penup()
scoreT.setposition(280,260)
scoreT.pendown()
scoreT.write("Score = " + str(score), font = ("Fira code", 12))

# Start message

startmessage = turtle.Turtle()
startmessage.speed(0)
startmessage.color("white")
startmessage.shape("blank")
startmessage.penup()
startmessage.setposition(0,-30)
startmessage.pendown()
startmessage.write("            Press SPACE To Start, \n\nUse the keys <- and -> to move LEFT or RIGHT", align = "center", font = ("Fira code", 12))

# Bricks

def makeRow(x,y):
    global row
    row = []
    for i in range(8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape('square')
        brick.shapesize(stretch_len=3.5, stretch_wid=1.5)
        brick.color('white')
        brick.penup()
        brick.goto(x + 95*i,y)
        brick.pendown()
        row.append(brick)
    return row

row1 = makeRow(-335,230)
row2 = makeRow(-335,180)
row3 = makeRow(-335,130)

# Functions 
deltax = 10

def paddle_left():
    if paddle.xcor() > -350:
        x = paddle.xcor()
        x += -deltax
        paddle.setx(x)

def paddle_right():
    if paddle.xcor() < 345:
        x = paddle.xcor()
        x += deltax
        paddle.setx(x)

""" def collisionBrick():
    if ball.xcor() """

def start_game():
    global gameContinue
    gameContinue = True

def restart_game():
    ball.goto(0,-239)
    paddle.goto(0,-250)
    ball.setheading(random.randint(20,160))
    global gameContinue
    gameContinue = False
    startmessage.penup()
    startmessage.setposition(0,-70)
    startmessage.pendown()
    startmessage.write("       GAME OVER,\n\nto Restart, press SPACE,\n\n   to Quit, press ESC", align = "center", font = ("Fira code", 12))

def quit_game():
    global GAME
    GAME = False

# Keyboard binding

wn.onkeypress(paddle_left, 'Left')
wn.onkeypress(paddle_right, 'Right')
wn.onkeypress(start_game, 'space')
wn.onkeypress(quit_game, 'Escape')
wn.listen()
wn.update()

GAME = True
gameContinue = False


# Main Loop  
while GAME:

    wn.update()

    # Start the Ball

    if gameContinue:
        ball.forward(ballspeed)
        startmessage.clear()
    
    # Borders

    if ball.ycor() > 295:
        ball.setheading(360 - ball.heading())
    
    if ball.ycor() < -300:
        restart_game()
    
    if ball.xcor() < -395 or ball.xcor() > 390:
        ball.setheading(180 - ball.heading())

    # Paddle and Ball collisions

    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() < paddle.xcor() +50 and ball.xcor() > paddle.xcor() +10):
        ball.setheading(-20 - ball.heading())

    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() > paddle.xcor() -50 and ball.xcor() < paddle.xcor() -10):
        ball.setheading(20 - ball.heading())

    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() < paddle.xcor() +9.9 and ball.xcor() > paddle.xcor() -9.9):
        ball.setheading(0 - ball.heading())