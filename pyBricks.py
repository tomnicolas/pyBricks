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

# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_len=5, stretch_wid=0.5)
paddle.color('white')
paddle.penup()
paddle.goto(0,-250)
deltaPaddle = 20

# Score

score = 0
scoreText = turtle.Turtle()
scoreText.speed(0)  
scoreText.color("grey")
scoreText.shape("blank")
scoreText.penup()
scoreText.setposition(275,260)
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
startmessage.write("Press SPACE To Start", align = "center", font = ("Fira code", 24))

# Info message

infomessage = turtle.Turtle()
infomessage.speed(0)
infomessage.color("white")
infomessage.shape("blank")
infomessage.penup()
infomessage.setposition(0,-40)
infomessage.pendown()
infomessage.write("Use the keys <- and -> to move LEFT or RIGHT", align = "center", font = ("Fira code", 12))

# Bricks
        
def make_row(x,y):
    # Make a ROW of bricks in range() starting at the x and y position
    global row
    row = []
    for i in range(10):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape('square')
        brick.shapesize(stretch_len=3.8, stretch_wid=1.5)
        brick.color('white')
        brick.penup()
        brick.goto(x + 79*i,y)
        brick.pendown()
        row.append(brick)
    return row

# Functions 

def collision_brick(row):
    # If the Ball collide with a Brick, the ball bounce, score and ballspeed increase and brick move outside the screen
    global score, ballspeed
    for brick in row:
        if ((brick.ycor() - 25) < ball.ycor() < (brick.ycor() + 25) and (brick.xcor() - 38) < ball.xcor() < (brick.xcor() + 38)):
            if ((ball.ycor() < brick.ycor() - 24) or (ball.ycor() > brick.ycor() + 24)):
                ball.setheading(360 - ball.heading())
            if ((ball.xcor() < brick.xcor() - 37) or (ball.xcor() > brick.xcor() + 37)):
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

def collision_paddle():
    # If the Ball collide withe the Paddle, the ball bounce
    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() +50 and ball.xcor() > paddle.xcor() +10):
        ball.setheading(-20 - ball.heading())
        if ((ball.xcor() < paddle.xcor() - 37) or (ball.xcor() > paddle.xcor() + 37)):
            ball.setheading(180 - ball.heading())

    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() > paddle.xcor() -50 and ball.xcor() < paddle.xcor() -10):
        ball.setheading(20 - ball.heading())
        if ((ball.xcor() < paddle.xcor() - 37) or (ball.xcor() > paddle.xcor() + 37)):
            ball.setheading(180 - ball.heading())

    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() +10 and ball.xcor() > paddle.xcor() -10):
        ball.setheading(0 - ball.heading())

def collision_wall():
    # If the Ball collide withe the borders of the screen, the ball bounce
    if ball.ycor() > 295:
        ball.setheading(360 - ball.heading())    
    if ball.ycor() < -300:
        game_over()    
    if ball.xcor() < -395 or ball.xcor() > 390:
        ball.setheading(180 - ball.heading())
  
def paddle_move_left():
    # Paddle move Left
    if paddle.xcor() > -345:
        x = paddle.xcor()
        x += -deltaPaddle
        paddle.setx(x)

def paddle_move_right():
    # Paddle move Right
    if paddle.xcor() < 335:
        x = paddle.xcor()
        x += deltaPaddle
        paddle.setx(x)

def start_game():
    # Delete messages on screen and start the game
    global gameContinue
    startmessage.clear()
    infomessage.clear()
    ball.setheading(random.randint(20,160))
    gameContinue = True

def reset_bricks(row):
    # Replace all the collided bricks at their original places
    for brick in row:
        if brick.undobufferentries() < 6:
           brick.undo() 
        wn.update()

def restart_game():
    # Reset all the components at original state
    global score, ballspeed
    score = 0
    ballspeed = 0.2
    reset_bricks(row1)
    reset_bricks(row2)
    reset_bricks(row3)
    paddle.goto(0,-250)
    paddle.st()
    ball.goto(0,-239)   
    ball.st()
    scoreText.clear()
    scoreText.write("Score = " + str(score), font = ("Fira code", 12, 'normal'))
    startmessage.clear()          
    startmessage.penup()
    startmessage.setposition(0,0)
    startmessage.pendown()
    startmessage.write("Press SPACE To Start", align = "center", font = ("Fira code", 24))
    infomessage.clear()
    infomessage.penup()
    infomessage.setposition(0,-40)
    infomessage.pendown()
    infomessage.write("Use the keys <- and -> to move LEFT or RIGHT", align = "center", font = ("Fira code", 12))
    wn.update()
    wn.listen()
    return score, ballspeed


def game_over():
    # Game over message and restart the game
    global gameContinue
    gameContinue = False
    restart_game()
    startmessage.clear()
    startmessage.penup()
    startmessage.setposition(0,10)
    startmessage.pendown()
    startmessage.write("GAME OVER", align = "center", font = ("Fira code", 32,'normal'))
    infomessage.clear()
    infomessage.penup()
    infomessage.setposition(0,-70)
    infomessage.pendown()
    infomessage.write("Press SPACE to try again\n\n   Press ESC to Quit", align = "center", font = ("Fira code", 12,'normal')) 
    wn.update()

def game_win():
    # You win message, ask if the player want to restart the game
    global gameContinue
    gameContinue = False
    ball.ht()
    paddle.ht()
    startmessage.clear()
    startmessage.penup()
    startmessage.setposition(0,10)
    startmessage.pendown()
    startmessage.write("YOU WIN !", align = "center", font = ("Fira code", 32, 'normal'))
    infomessage.clear()
    infomessage.penup()
    infomessage.setposition(0,-70)
    infomessage.pendown()
    infomessage.write("Press 'R' to try again\n\n  Press ESC to Quit", align = "center", font = ("Fira code", 12,'normal'))
    wn.listen()
    wn.update()    

def quit_game():
    # Close the window, end the game
    global GAME
    GAME = False

# Keyboard binding

wn.onkeypress(paddle_move_left, 'Left')
wn.onkeypress(paddle_move_right, 'Right')
wn.onkeypress(start_game, 'space')
wn.onkeypress(quit_game, 'Escape')
wn.onkeypress(restart_game, 'r')
wn.listen()
wn.update()

# Settings

GAME = True
gameContinue = False
row1 = make_row(-358,230)
row2 = make_row(-358,197)
row3 = make_row(-358,164)
ballspeed = 0.2
deltaPaddle = 20

# Main Loop  

while GAME:

    wn.update()

    if gameContinue:                
        # Start the Ball
        ball.forward(ballspeed)

    if score == 150:
        # Condition for winning the game
        game_win()
    
    # Collisions surveillance
    collision_paddle()
    collision_wall()
    collision_brick(row1)
    collision_brick(row2)
    collision_brick(row3)

wn.update()