import pygame
from abc import ABC, abstractmethod
from settings import GREEN, HEIGHT, WIDTH, YELLOW

class Property(ABC):
    @abstractmethod
    def draw(self, screen):
        pass

class Battery(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.is_taken = False

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)

class Bed(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

class Flash(Property):
    def __init__(self):
        self.left_time = 60
        self.radius = 50

    def draw(self, screen):
        print(screen)

    def drawlight(self, dark_surface, player):
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), player.rect.center, self.radius)
        

        
