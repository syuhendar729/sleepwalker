import pygame
from settings import BROWN

# Konstanta ukuran tetap
HORIZONTAL_WALL_HEIGHT = 20
VERTICAL_WALL_WIDTH = 20

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, BROWN, self.rect)


class HorizontalWall(Wall):
    def __init__(self, x, y, width):
        super().__init__(x, y, width, HORIZONTAL_WALL_HEIGHT)


class VerticalWall(Wall):
    def __init__(self, x, y, height):
        super().__init__(x, y, VERTICAL_WALL_WIDTH, height)


walls = [
    # Batas luar
    HorizontalWall(0, -20, 1200),  # atas
    VerticalWall(-20, 0, 800),     # kiri
    HorizontalWall(0, 800, 1200),  # bawah
    VerticalWall(1200, 0, 800),    # kanan

    # Dalam
    VerticalWall(100, 500, 50),
    HorizontalWall(100, 100, 700),
    HorizontalWall(890, 100, 100),
    VerticalWall(100, 100, 300),
    HorizontalWall(100, 480, 500),
    VerticalWall(1060, 100, 400),
    VerticalWall(680, 180, 250),
    VerticalWall(500, 50, 60),
    HorizontalWall(200, 200, 400),
    HorizontalWall(780, 200, 300),
    VerticalWall(850, 200, 200),
    HorizontalWall(850, 300, 150),
    HorizontalWall(680, 500, 400),
    VerticalWall(200, 200, 230),
    VerticalWall(400, 380, 100),
    VerticalWall(800, 500, 60),
    VerticalWall(350, 500, 50),
    VerticalWall(500, 550, 50),
    VerticalWall(480, 200, 200),
    HorizontalWall(300, 300, 200),
    HorizontalWall(100, 600, 980),

]  # dll

