import pygame
from settings import BROWN

LENGTH = 100
THICKNESS = 20

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, BROWN, self.rect)

class HorizontalWall(Wall):
    def __init__(self, x, y):
        super().__init__(x, y, LENGTH, THICKNESS)

class VerticalWall(Wall):
    def __init__(self, x, y):
        super().__init__(x, y, THICKNESS, LENGTH)


# Ketentuan maze cell:
# 0: wall tidak dibuat
# 1: wall dibuat horizontal
# 2: wall dibuat vertical
# 3: wall dibuat horizontal dan vertical
# Grid size: 13 columns x 9 rows mengikuti ukuran screen 1200x800


maze = [
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 2],
    [2, 2, 3, 1, 0, 1, 3, 0, 1, 1, 3, 2, 2],
    [2, 2, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2],
    [2, 2, 3, 1, 1, 1, 3, 1, 0, 3, 3, 0, 2],
    [2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2],
    [2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 2, 0, 1, 1, 2, 0, 3, 1, 0, 2],
    [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
]


def generate_walls_from_maze(maze):
    walls = []
    rows = len(maze)
    cols = len(maze[0])
    print(rows)
    print(cols)
    for y in range(rows):
        for x in range(cols):
            cell = maze[y][x]
            if cell == 1: # horizontal
                print(f"Maze: {maze[y][x]}")
                print(f"x: {x} dan y: {y}")
                walls.append(HorizontalWall(x*LENGTH, y*LENGTH))
            elif cell == 2: # vertical
                print(f"Maze: {maze[y][x]}")
                print(f"x: {x} dan y: {y}")
                walls.append(VerticalWall(x*LENGTH, y*LENGTH))
            elif cell == 3: # horizontal dan vertical
                print(f"Maze: {maze[y][x]}")
                print(f"x: {x} dan y: {y}")
                walls.append(HorizontalWall(x*LENGTH, y*LENGTH))
                walls.append(VerticalWall(x*LENGTH, y*LENGTH))
            else:
                pass

    return walls

walls = generate_walls_from_maze(maze)



# maze = [
#     [3, 1, 1, 1, 2],
#     [2, 3, 1, 2, 2],
#     [2, 2, 2, 2, 2],
#     [2, 0, 1, 0, 2],
#     [2, 1, 1, 1, 0],
# ]

# maze = [
#     [3, 1, 2, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

# x0 x1 x2 x3 x4 (y1)
# 
#
#
#
