import pygame
from abc import ABC, abstractmethod
from settings import GREEN, YELLOW

class Property(ABC):
    def __init__(self):
        self.is_taken = False

    def set_is_taken(self, taken):
        self.is_taken = taken

    @abstractmethod
    def draw(self, screen):
        pass


class Battery(Property):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)

class Bed(Property):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

        
