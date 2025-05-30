import pygame
from obstacle.obstacle import Obstacle
from settings import *

class Water(Obstacle):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.rect = pygame.Rect(self.x, self.y, w, h)
        self.vx = 0
        self.vy = 0

    def push(self):
        pass

    def update(self):
        pass

    def draw(self, screen, camera=None):
        pass

    def interact(self, player):
        pass
