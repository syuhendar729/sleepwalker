import pygame
import sys

pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sleep Walker Maze - Darkness")

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Data pemain
player_size = 40
player_x = 60
player_y = 60
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

# Daftar tembok membentuk labirin

walls = [
    # pygame.Rect(x, y, width, heigh)
    pygame.Rect(0, -20, 1200, 20),         # batas atas
    pygame.Rect(-20, 0, 20, 800),         # batas kiri
    pygame.Rect(0, 800, 1200, 20),       # batas bawah
    pygame.Rect(1200, 0, 20, 800),       # batas kanan

    # wall di dalam
    pygame.Rect(100, 500, 20, 50),
    pygame.Rect(100, 100, 700, 20),
    pygame.Rect(890, 100, 100, 20),
    pygame.Rect(100, 100, 20, 300),
    pygame.Rect(100, 480, 500, 20),
    pygame.Rect(1060, 100, 20, 400),
    pygame.Rect(680, 180, 20, 250),
    pygame.Rect(500, 50, 20, 60),
    pygame.Rect(200, 200, 400, 20),
    pygame.Rect(780, 200, 300, 20),
    pygame.Rect(850, 200, 20, 200),
    pygame.Rect(850, 300, 150, 20),
    pygame.Rect(680, 500, 400, 20),
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(200, 200, 20, 230),
    pygame.Rect(400, 380, 20, 100),
    pygame.Rect(800, 500, 20, 60),
    pygame.Rect(350, 500, 20, 50),
    pygame.Rect(500, 550, 20, 50),
    pygame.Rect(480, 200, 20, 200),
    pygame.Rect(300, 300, 200, 20),
    pygame.Rect(100, 600, 980, 20),
]



# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Batasi ke 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simpan posisi lama
    old_x, old_y = player_rect.x, player_rect.y

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed

    # Deteksi tabrakan dengan semua tembok
    for wall in walls:
        if player_rect.colliderect(wall):
            player_rect.x, player_rect.y = old_x, old_y
            break

    # Gambar latar dan objek
    screen.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    # Gambar pemain
    pygame.draw.rect(screen, BLUE, player_rect)

    # Tambahkan layer gelap
    dark_surface = pygame.Surface((WIDTH, HEIGHT))
    dark_surface.fill(BLACK)
    dark_surface.set_alpha(230)  # Semakin kecil semakin terang

    # Buat "lubang" transparan di sekitar pemain (efek cahaya)
    light_radius = 60
    pygame.draw.circle(dark_surface, (0, 0, 0, 0), player_rect.center, light_radius)

    # Tempelkan layer gelap di atas semuanya
    screen.blit(dark_surface, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()