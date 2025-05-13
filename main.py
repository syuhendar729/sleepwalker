import pygame, sys
from settings import *
from player import Player
from stone import Stone
from wall import walls

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sleep Walker Maze - Darkness")
clock = pygame.time.Clock()

player = Player(60, 60)
stones = [Stone(800, 100), Stone(800, 700)]


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
