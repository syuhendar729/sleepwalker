import pygame, sys
from property import Battery
from settings import *
from player import PlayerHuman, PlayerMonster
from stone import Stone
from wall import walls

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sleep Walker Maze - Darkness")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = PlayerHuman(60, 60)
stones = [Stone(800, 100), Stone(800, 700)]
batteries = [Battery(5, 5), Battery(1175, 780)]

# Timer: 30 detik
start_ticks = pygame.time.get_ticks()


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

    # Hitung waktu mundur
    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, 30 - seconds_passed)

    # Pengecekan player menyentuh wall
    for wall in walls:
        if player.rect.colliderect(wall):
            player.rect.x, player.rect.y = old_x, old_y
            player.vx = 0
            player.vy = 0

    # Pengecekan player menyentuh stone
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

    # Pengecekan player menyentuh baterai
    for battery in batteries:
        if player.rect.colliderect(battery.rect) and not battery.is_taken:
            print("Berhasil mengambil baterai")
            battery.is_taken = True
            # time_left = time_left + 30
            start_ticks += 30 * 1000

    screen.fill(WHITE)

    # Gambar semua wall
    for wall in walls:
        pygame.draw.rect(screen, BROWN, wall)

    # Gambar semua stone
    for stone in stones:
        stone.draw(screen)

    # Gambar semua battery yang belum diambil
    for battery in batteries:
        if not battery.is_taken:
            battery.draw(screen)

    player.draw(screen)



    # === Efek gelap dengan lubang cahaya di sekitar pemain ===
    dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    dark_surface.fill((0, 0, 0, 230))  # full hitam 255

    if time_left != 0:
        # Membuat cahaya senter di sekitar player
        light_radius = 50
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), player.rect.center, light_radius)


    screen.blit(dark_surface, (0, 0))
    # ==========================================================

    # Gambar timer
    timer_text = font.render(f"Waktu: {time_left}", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
