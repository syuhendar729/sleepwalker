import pygame
from abc import ABC, abstractmethod
from settings import YELLOW

class Property:
    def __init__(self):
        self.is_taken = False

    def set_is_taken(self, taken):
        self.is_taken = taken

    @abstractmethod
    def hit_collision(self):
        pass

    def draw(self, screen):
        pass


class Battery(Property):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 20, 20)

    def hit_collision(self):
        # set timer to 60 second
        # set rect Battery hilang
        # set 
        print("Menyentuh batterai")

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
        
