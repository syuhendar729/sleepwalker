import pygame, sys
import random
from settings import *
from player import Player
from stone import Stone
from wall import walls
from winningCondition import show_win_screen

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sleep Walker Maze - Darkness")
clock = pygame.time.Clock()

# Membuat posisi acak / memilih tempat acak
def get_random_position():
    margin = 50 
    x = random.randint(margin, WIDTH - margin)
    y = random.randint(margin, HEIGHT - margin)
    return (x, y)


player = Player(60, 60)
stones = [Stone(800, 100), Stone(800, 700)]

# Menyimpan posisi acak
win_pos = get_random_position()
win_radius = 20 # Ukuran lingkaran

won = False
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    old_x, old_y = player.rect.x, player.rect.y
    player.update()

    for wall in walls:
        if player.rect.colliderect(wall):
            player.rect.x, player.rect.y = old_x, old_y
            player.vx = 0
            player.vy = 0

    for stone in stones:
        if player.rect.colliderect(stone.rect):
            dx = stone.rect.centerx - player.rect.centerx
            dy = stone.rect.centery - player.rect.centery
            if abs(dx) > abs(dy):
                stone.push(3 if dx > 0 else -3, 0)
                player.vx *= 0.5
            else:
                stone.push(0, 3 if dy > 0 else -3)
                player.vy *= 0.5

    for stone in stones:
        stone.update(walls)

    screen.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(screen, BROWN, wall)
    for stone in stones:
        stone.draw(screen)
    player.draw(screen)
    
    # Menggambar lingkaran kemenangan
    pygame.draw.circle(screen, (0, 255, 0), win_pos, win_radius)
    
    # Pengecekan apakah player pada posisi menang?
    player_center = player.rect.center
    dist = ((player_center[0] - win_pos[0]) ** 2 + (player_center[1] - win_pos[1]) ** 2) ** 0.5
    if dist < win_radius + player.rect.width // 2:
        won = True
        running = False
        show_win_screen(screen, WIDTH, HEIGHT)


    # === Efek gelap dengan lubang cahaya di sekitar pemain ===
    dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    dark_surface.fill((0, 0, 0, 255))  # full hitam 255

    light_radius = 60
    pygame.draw.circle(dark_surface, (0, 0, 0, 0), player.rect.center, light_radius)

    screen.blit(dark_surface, (0, 0))
    # ==========================================================

    pygame.display.flip()
    

pygame.quit()
sys.exit()