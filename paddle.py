from gameObject import GameObject


class Paddle(GameObject):
    def __init__(self, velocity, xPos, yPos, width, height, color):
        super().__init__(xPos, yPos, width, height, color)
        self.velocity = velocity

    def movePaddle(self, velocity):
        self.xPos += velocity
