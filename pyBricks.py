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

# Score

""" text = turtle.Turtle()
text.shape('blank')
text.color('white')
text.speed(0)
text.setposition(200, 250)
text.write('x = {} y = {}'.format(ball.xcor(),ball.ycor()), align = "center", font = ("Courier", 8, "bold")) """

# Level



# Bricks



# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_len=5)
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
    ball.forward(0.03)
    print(ball.xcor(),ball.ycor())


    # Border
    if ball.ycor() > 295:
        ball.setheading(360 - ball.heading())
    
    if ball.xcor() < -395 or ball.xcor() > 395:
        ball.setheading(180 - ball.heading())

    
