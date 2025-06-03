import pygame
from abc import ABC, abstractmethod
from settings import GREEN, YELLOW

class Property(ABC):
    @abstractmethod
    def draw(self, screen):
        pass

class Battery(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.is_taken = False

    def draw(self, screen, camera=None):
        rect_to_draw = self.rect
        if camera:
            rect_to_draw = camera.apply(self.rect)
        pygame.draw.rect(screen, YELLOW, rect_to_draw)

class CircleVictory(Property):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.pos = (x, y)
        self.radius = 20

    def draw(self, screen, camera=None):
        pos = self.pos
        if camera:
            pos = (pos[0] + camera.offset_x, pos[1] + camera.offset_y)
        pygame.draw.circle(screen, GREEN, pos, self.radius)

class Flash(Property):
    def __init__(self):
        self.left_time = 60
        self.radius = 50

    def draw(self, screen):
        print(screen)

    def drawlight(self, dark_surface, player, camera=None):
        center = player.rect.center
        if camera:
            center = (center[0] + camera.offset_x, center[1] + camera.offset_y)
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), center, self.radius)
        

class Life(Property):
    def __init__(self) -> None:
        super().__init__()

    def draw(self, screen):
        pass

        
