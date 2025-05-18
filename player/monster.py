import pygame
from player.player import PlayerHuman
from settings import BLACK


class Monster:
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)
        

