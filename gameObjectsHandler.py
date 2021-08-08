from paddle import Paddle
from ball import Ball
from brick import Brick
from constants import PADDLE_START_X, PADDLE_START_Y

paddle = Paddle(PADDLE_START_X, PADDLE_START_Y, 700, 120, 20, (245, 227, 255))
allBalls = []
bricks = []

def createBricksArray():
    bricks.clear()
    for i in range(6):
        for j in range(10):
            bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (120, 205, 250)))
    return bricks

def createBallsArray():
    allBalls.clear()
    startingBall = Ball(1, 1, 380, 680, 10, 10, (245, 227, 255))
    allBalls.append(startingBall)
    return allBalls

def addBallToGame():
    allBalls.append(Ball(1, 1, 380, 680, 10, 10, (245, 227, 255)))

def drawAllBalls(window):
    for ball in allBalls:
        ball.draw(window)


def drawAllBricks(window):
    for brick in bricks:
        brick.draw(window)


def drawPaddle(window):
    paddle.draw(window)


def drawAllGameItems(window):
    drawPaddle(window)
    drawAllBricks(window)
    drawAllBalls(window)
