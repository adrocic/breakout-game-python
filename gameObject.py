import pygame


class GameObject(object):
    def __init__(self, xPos, yPos, width, height, color):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.xPos, self.yPos, self.width, self.height])

