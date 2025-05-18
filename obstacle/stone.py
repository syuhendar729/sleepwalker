import pygame
from obstacle.obstacle import Obstacle
from settings import *

class Stone(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rect = pygame.Rect(self.x, self.y, STONE_SIZE, STONE_SIZE)
        self.vx = 0
        self.vy = 0

    def push(self, direction_x, direction_y):
        self.vx = direction_x
        self.vy = direction_y

    def update(self, walls):
        old_x, old_y = self.rect.x, self.rect.y
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)

        self.vx *= (1 - STONE_FRICTION)
        self.vy *= (1 - STONE_FRICTION)

        if abs(self.vx) < 0.1: self.vx = 0
        if abs(self.vy) < 0.1: self.vy = 0

        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x = old_x
                self.rect.y = old_y
                self.vx = 0
                self.vy = 0

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)

    def interact(self, player):
        print(f"Interaksi kepada {player}")
