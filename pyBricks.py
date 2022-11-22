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

# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_len=5, stretch_wid=0.5)
paddle.color('white')
paddle.penup()
paddle.goto(0,-250)
deltaPaddle = 30

# Score

score = 0
scoreText = turtle.Turtle()
scoreText.speed(0)  
scoreText.color("grey")
scoreText.shape("blank")
scoreText.penup()
scoreText.setposition(280,260)
scoreText.pendown()
scoreText.write("Score = " + str(score), font = ("Fira code", 12))

# Start message

startmessage = turtle.Turtle()
startmessage.speed(0)
startmessage.color("white")
startmessage.shape("blank")
startmessage.penup()
startmessage.setposition(0,0)
startmessage.pendown()
startmessage.write("Press SPACE To Start,", align = "center", font = ("Fira code", 24))

# Info message

infomessage = turtle.Turtle()
infomessage.speed(0)
infomessage.color("white")
infomessage.shape("blank")
infomessage.penup()
infomessage.setposition(0,-30)
infomessage.pendown()
infomessage.write("Use the keys <- and -> to move LEFT or RIGHT", align = "center", font = ("Fira code", 12))

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

def collisionBrick(row):
    global score, ballspeed
    for brick in row:
        if ((brick.ycor() - 25) < ball.ycor() < (brick.ycor() + 25) and (brick.xcor() - 35) < ball.xcor() < (brick.xcor() + 35)):
            if ((ball.ycor() < brick.ycor() - 20) or (ball.ycor() > brick.ycor() + 20)):
                ball.setheading(360 - ball.heading())
            if ((ball.xcor() < brick.xcor() - 30) or (ball.xcor() > brick.xcor() + 30)):
                ball.setheading(180 - ball.heading())
            brick.clear()
            brick.penup()
            brick.goto(1000, 1000)
            ballspeed += 0.008
            score += 5
            scoreText.clear()
            scoreText.write("Score = " + str(score), font = ("Fira code", 12))
            wn.update()
            return ballspeed, score

def hideBricks(row):
    for brick in row:
        brick.penup()
        brick.goto(1000, 1000)

def collisionPaddle():
    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() < paddle.xcor() +50 and ball.xcor() > paddle.xcor() +10):
        ball.setheading(-20 - ball.heading())
    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() > paddle.xcor() -50 and ball.xcor() < paddle.xcor() -10):
        ball.setheading(20 - ball.heading())
    if (ball.ycor() < -240 and ball.ycor() > -260) and (ball.xcor() < paddle.xcor() +9.99 and ball.xcor() > paddle.xcor() -9.99):
        ball.setheading(0 - ball.heading())

def collisionWall():
    if ball.ycor() > 295:
        ball.setheading(360 - ball.heading())    
    if ball.ycor() < -300:
        restartGame()    
    if ball.xcor() < -395 or ball.xcor() > 390:
        ball.setheading(180 - ball.heading())
  
def paddleMoveLeft():
    if paddle.xcor() > -350:
        x = paddle.xcor()
        x += -deltaPaddle
        paddle.setx(x)

def paddleMoveRight():
    if paddle.xcor() < 340:
        x = paddle.xcor()
        x += deltaPaddle
        paddle.setx(x)

def startGame():
    startmessage.clear()
    infomessage.clear()
    global gameContinue
    gameContinue = True

def restartGame():
    global gameContinue
    gameContinue = False
    paddle.ht()
    ball.ht()
    hideBricks(row1)
    hideBricks(row2)
    hideBricks(row3)
    ball.setheading(random.randint(20,160))
    scoreText.clear()
    scoreText.write("Score = " + str(score), font = ("Fira code", 12, 'normal'))
    startmessage.clear()
    startmessage.penup()
    startmessage.setposition(0,10)
    startmessage.pendown()
    startmessage.write("GAME OVER,", align = "center", font = ("Fira code", 32,'normal'))
    infomessage.clear()
    infomessage.penup()
    infomessage.setposition(0,-70)
    infomessage.pendown()
    infomessage.write("press ESC, to Quit.", align = "center", font = ("Fira code", 12,'normal'))

def winGame():
    paddle.ht()
    ball.ht()
    startmessage.clear()
    startmessage.penup()
    startmessage.setposition(0,0)
    startmessage.pendown()
    startmessage.write("YOU WIN !", align = "center", font = ("Fira code", 32, 'normal'))
    infomessage.clear()
    infomessage.penup()
    infomessage.setposition(0,-50)
    infomessage.pendown()
    infomessage.write("press ESC, to Quit.", align = "center", font = ("Fira code", 12,'normal'))    

def quitGame():
    global GAME
    GAME = False

# Keyboard binding

wn.onkeypress(paddleMoveLeft, 'Left')
wn.onkeypress(paddleMoveRight, 'Right')
wn.onkeypress(startGame, 'space')
wn.onkeypress(quitGame, 'Escape')
wn.listen()
wn.update()

GAME = True
gameContinue = False


# Main Loop  

while GAME:

    wn.update()

    if gameContinue:                # Start the Ball
        ball.forward(ballspeed)
        startmessage.clear()

    if score == 120:
        winGame()

    collisionBrick(row1)
    collisionBrick(row2)
    collisionBrick(row3)
    collisionPaddle()
    collisionWall()

wn.update()