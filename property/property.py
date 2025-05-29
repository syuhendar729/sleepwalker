import pygame
from abc import ABC, abstractmethod
from settings import GREEN, WORLD_HEIGHT, WORLD_WIDTH, YELLOW

class Property(ABC):
    @abstractmethod
    def draw(self, screen):
        pass

class Battery(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.is_taken = False

    def draw(self, screen, camera=None):
        # pygame.draw.rect(screen, YELLOW, self.rect)
        rect_to_draw = self.rect
        if camera:
            rect_to_draw = camera.apply(self.rect)
        pygame.draw.rect(screen, YELLOW, rect_to_draw)

class Bed(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self, screen, camera=None):
        # pygame.draw.rect(screen, GREEN, self.rect)
        rect_to_draw = self.rect
        if camera:
            rect_to_draw = camera.apply(self.rect)
        pygame.draw.rect(screen, GREEN, rect_to_draw)

class Flash(Property):
    def __init__(self):
        self.left_time = 60
        self.radius = 50

    def draw(self, screen):
        print(screen)

    def drawlight(self, dark_surface, player, camera=None):
        # pygame.draw.circle(dark_surface, (0, 0, 0, 0), player.rect.center, self.radius)
        center = player.rect.center
        if camera:
            center = (center[0] + camera.offset_x, center[1] + camera.offset_y)
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), center, self.radius)
        

        
