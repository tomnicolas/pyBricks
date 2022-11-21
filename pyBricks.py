# small bricks breaker inb Python 3 for Openclassrooms project
# by Tom NICOLAS

import turtle
import random

# Window Setup

wn = turtle.Screen()
wn.title('Casse-Brique by Tom Nicolas')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.color('white')
ball.penup()
ball.goto(0,-200)
ball.setheading(random.randint(20,160))
ballspeed = 0.04

# Score
startmessage = turtle.Turtle()
startmessage.speed(0)
startmessage.color("white")
startmessage.shape("blank")
startmessage.penup()
startmessage.setposition(0,75)
startmessage.pendown()
startmessage.write("", align = "center", font = ("Courier", 12))

# Level



# Bricks



# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_len=5, stretch_wid=0.5)
paddle.color('white')
paddle.penup()
paddle.goto(0,-250)


# Functions 

def paddle_left():
    x = paddle.xcor()
    x += -20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)




""" def start_game():
    global running
    running = True
    ball_start() """


# Keyboard binding

wn.listen()
wn.onkeypress(paddle_left, 'Left')
wn.onkeypress(paddle_right, 'Right')
#wn.onkeypress(start_game, 'space')

# Main Lopp
while True:
    wn.update()
    ball.forward(ballspeed)
    print(ball.xcor(),ball.ycor())


    # Borders
    if ball.ycor() > 295:
        ball.setheading(360 - ball.heading())

    
    if ball.ycor() < -300:
        startmessage.write("Game Over", align = "center", font = ("Courier", 12))
    
    
    if ball.xcor() < -395 or ball.xcor() > 395:
        ball.setheading(180 - ball.heading())

    # Paddle and Ball collisions

    if ball.ycor() < -245 and (ball.xcor() < paddle.xcor() +48 and ball.xcor() > paddle.xcor() -48):
        ball.setheading(0 - ball.heading())