import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from gameObjectsHandler import drawAllGameItems, createBricksArray

# pygame stuff
pygame.init()
pygame.display.set_caption("Breakout")
background = pygame.image.load('background.png')
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# game audio
brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
bounceSound.set_volume(.2)

# initial game items
bricks = createBricksArray()

# handle game window redraws
gameover = False
def redrawGameWindow():
    window.blit(background, (0, 0))
    drawAllGameItems(window)

    font = pygame.font.SysFont('comicsans', 50)

    if gameover:
        if len(bricks) == 0:
            winMessage = font.render("Congrats!", 1, (255, 255, 255))
        else:
            loseMessage = font.render("That's rough!", 1, (255, 255, 255))
        window.blit(resText,
                    ((SCREEN_WIDTH // 2 - resText.get_width() // 2), screen_height // 2 - resText.get_height() // 2))
        playAgainText = font.render("Press Space to Play Again", 1, (255, 255, 255))
        window.blit(playAgainText, ((screen_width // 2 - playAgainText.get_width() // 2), screen_height // 2 + 30))

    pygame.display.update()



clock = pygame.time.Clock()
running = True
while running:
    clock.tick(100)
    if not gameover:
        for ball in allBalls:
            ball.moveBall()
        if pygame.mouse.get_pos()[0] - paddle.width // 2 < 0:
            paddle.xPos = 0
        elif pygame.mouse.get_pos()[0] + paddle.width // 2 > screen_width:
            paddle.xPos = screen_width - paddle.width
        else:
            paddle.xPos = pygame.mouse.get_pos()[0] - paddle.width // 2

        for ball in allBalls:
            if (paddle.xPos <= ball.xPos <= paddle.xPos + paddle.width) or (
                    paddle.xPos <= ball.xPos + ball.width <= paddle.xPos + paddle.width):
                if paddle.yPos <= ball.yPos + ball.height <= paddle.yPos + paddle.height:
                    ball.velocityY *= -1
                    ball.yPos = paddle.yPos - ball.height - 1
                    bounceSound.play()

            if ball.xPos + ball.width >= screen_width:
                bounceSound.play()
                ball.velocityX *= -1
            if ball.xPos < 0:
                bounceSound.play()
                ball.velocityX *= -1
            if ball.yPos <= 0:
                bounceSound.play()
                ball.velocityY *= -1

            if ball.yPos > screen_height:
                allBalls.pop(allBalls.index(ball))

        for brick in bricks:
            for ball in allBalls:
                if (
                        brick.xPos <= ball.xPos <= brick.xPos + brick.width) or brick.xPos <= ball.xPos + ball.width <= brick.xPos + brick.width:
                    if (
                            brick.yPos <= ball.yPos <= brick.yPos + brick.height) or brick.yPos <= ball.yPos + ball.height <= brick.yPos + brick.height:
                        brick.exists = False
                        if brick.containsBall:
                            allBalls.append(Ball(3, 3, brick.xPos, brick.yPos, 20, 20, (255, 255, 255)))
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
            ball = Ball(3, 3, screen_width / 2 - 10, screen_height - 400, 20, 20, (255, 255, 255))
            if len(allBalls) == 0:
                allBalls.append(ball)

            bricks.clear()
            for i in range(6):
                for j in range(10):
                    bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (120, 205, 250)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()

# end the game
pygame.quit()
