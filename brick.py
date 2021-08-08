from gameObject import GameObject
import random


class Brick(GameObject):
    def __init__(self, xPos, yPos, width, height, color):
        super().__init__(xPos, yPos, width, height, color)

        self.exists = True
        self.randNum = random.randint(0, 10)
        self.containsBall = self.randNum < 3
