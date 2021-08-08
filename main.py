import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, REFRESH_RATE
from gameObjectsHandler import paddle, drawAllGameItems, createBricksArray, createBallsArray, addBallToGame

# pygame stuff
pygame.init()
pygame.display.set_caption("Breakout")
background = pygame.image.load('background.png')
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('comicsans', 50)

# game audio
brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
bounceSound.set_volume(.2)

# initial game items
bricks = createBricksArray()
allBalls = createBallsArray()
winMessage = winMessage = font.render("You Won!", 1, (255, 255, 255))
loseMessage = font.render("You Lost!", 1, (255, 255, 255))
playAgainMessage = font.render("Press Space to Play Again", 1, (255, 255, 255))

# handle game window redraws
gameover = False
def redrawGameWindow():
    window.blit(background, (0, 0))
    drawAllGameItems(window)

    if gameover:
        window.blit(winMessage if len(bricks) else loseMessage, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        window.blit(playAgainMessage, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(REFRESH_RATE)
    if not gameover:
        for ball in allBalls:
            ball.moveBall()
        if pygame.mouse.get_pos()[0] - paddle.width // 2 < 0:
            paddle.xPos = 0
        elif pygame.mouse.get_pos()[0] + paddle.width // 2 > SCREEN_WIDTH:
            paddle.xPos = SCREEN_WIDTH - paddle.width
        else:
            paddle.xPos = pygame.mouse.get_pos()[0] - paddle.width // 2

        for ball in allBalls:
            if (paddle.xPos <= ball.xPos <= paddle.xPos + paddle.width) or (
                    paddle.xPos <= ball.xPos + ball.width <= paddle.xPos + paddle.width):
                if paddle.yPos <= ball.yPos + ball.height <= paddle.yPos + paddle.height:
                    ball.velocityY *= -1
                    ball.yPos = paddle.yPos - ball.height - 1
                    bounceSound.play()

            if ball.xPos + ball.width >= SCREEN_WIDTH:
                bounceSound.play()
                ball.velocityX *= -1
            if ball.xPos < 0:
                bounceSound.play()
                ball.velocityX *= -1
            if ball.yPos <= 0:
                bounceSound.play()
                ball.velocityY *= -1

            if ball.yPos > SCREEN_HEIGHT:
                allBalls.pop(allBalls.index(ball))

        for brick in bricks:
            for ball in allBalls:
                if (
                        brick.xPos <= ball.xPos <= brick.xPos + brick.width) or brick.xPos <= ball.xPos + ball.width <= brick.xPos + brick.width:
                    if (
                            brick.yPos <= ball.yPos <= brick.yPos + brick.height) or brick.yPos <= ball.yPos + ball.height <= brick.yPos + brick.height:
                        brick.exists = False
                        if brick.containsBall:
                            addBallToGame()
                        ball.velocityY *= -1
                        brickHitSound.play()
                        break

        for brick in bricks:
            if not brick.exists:
                bricks.pop(bricks.index(brick))

        if len(allBalls) == 0:
            gameover = True

    keys = pygame.key.get_pressed()
    if len(bricks) == 0:
        won = True
        gameover = True
    if gameover:
        if keys[pygame.K_SPACE]:
            gameover = False
            won = False
            createBallsArray()
            createBricksArray()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()

# end the game
pygame.quit()
