from gameObject import GameObject


class Ball(GameObject):
    def __init__(self, velocityX, velocityY, xPos, yPos, width, height, color):
        super().__init__(xPos, yPos, width, height, color)
        self.velocityX = velocityX
        self.velocityY = velocityY

    def changeDirection(self):
        self.velocityX * -1
        self.velocityY * -1

    def moveBall(self):
        self.xPos += self.velocityX
        self.yPos += self.velocityY
