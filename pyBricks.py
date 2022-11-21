# small bricks breaker inb Python 3 for Openclassrooms project
# by Tom NICOLAS

import turtle

# Window Setup

window = turtle.Screen()
window.title('Casse-Brique by Tom Nicolas')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# Score



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

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.color('white')
ball.penup()
ball.goto(0,0)

# Functions 

def paddle_left():
    x = paddle.xcor()
    x += -20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


# Keyboard binding

window.listen()
window.onkeypress(paddle_left, 'Left')
window.onkeypress(paddle_right, 'Right')

# Main Lopp
while True:
    window.update()