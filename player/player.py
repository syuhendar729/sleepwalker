from abc import ABC, abstractmethod
import pygame
from settings import *
from audio import Audio

class Player(ABC):
    def __init__(self, x, y, size, color, max_speed):
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)
        self.vx = 0
        self.vy = 0
        self.max_speed = max_speed
        self.sfx = Audio()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    def handle_input(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]: 
            self.vy -= PLAYER_ACCEL
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: 
            self.vy += PLAYER_ACCEL
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: 
            self.vx -= PLAYER_ACCEL
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
            self.vx += PLAYER_ACCEL

        self.vx = max(-self.max_speed, min(self.max_speed, self.vx))
        self.vy = max(-self.max_speed, min(self.max_speed, self.vy))

        if not (keys[pygame.K_a] or keys[pygame.K_d]):
            self.vx *= (1 - PLAYER_FRICTION)
        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            self.vy *= (1 - PLAYER_FRICTION)


class PlayerMonster(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=(200, 50, 50), max_speed=4)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        pass
