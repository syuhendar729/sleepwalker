import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.vx = 0
        self.vy = 0

    def handle_input(self, keys):
        if keys[pygame.K_w]: self.vy -= PLAYER_ACCEL
        if keys[pygame.K_s]: self.vy += PLAYER_ACCEL
        if keys[pygame.K_a]: self.vx -= PLAYER_ACCEL
        if keys[pygame.K_d]: self.vx += PLAYER_ACCEL

        self.vx = max(-PLAYER_MAX_SPEED, min(PLAYER_MAX_SPEED, self.vx))
        self.vy = max(-PLAYER_MAX_SPEED, min(PLAYER_MAX_SPEED, self.vy))

        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.vx *= (1 - PLAYER_FRICTION)
        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            self.vy *= (1 - PLAYER_FRICTION)

    def update(self):
        self.rect.x += int(self.vx)
        self.rect.y += int(self.vy)

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)