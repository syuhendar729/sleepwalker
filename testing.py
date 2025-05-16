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
BROWN = (41, 38, 31)
GRAY = (91, 110, 117)

# Data pemain
player_size = 40
player_x = 60
player_y = 60
player_speed = 5

# kecepatan dan percepatan pemain
velocity_x = 0
velocity_y = 0
acceleration = 0.5
max_speed = 5
friction = 0.1
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)


# Data batu
stone_rect = pygame.Rect(60, 60, 50, 50)
stone_velocity_x = 0
stone_velocity_y = 0
stone_friction = 0.05

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

# Buat daftar pasangan rect dan velocity untuk setiap batu
stones = [
    {"rect": pygame.Rect(800, 100, 40, 40), "vx": 0, "vy": 0},
    {"rect": pygame.Rect(800, 700, 40, 40), "vx": 0, "vy": 0},
]


# Game loop
running = True
clock = pygame.time.Clock()


# def stone_movement():
#     # Simpan posisi lama batu
#     old_rock_x, old_rock_y = rock_rect.x, rock_rect.y
#     # Gerakkan batu
#     stone_rect.x += int(stone_velocity_x)
#     stone_rect.y += int(stone_velocity_y)
#
#     # Terapkan gesekan
#     stone_velocity_x *= (1 - stone_friction)
#     stone_velocity_y *= (1 - stone_friction)
#
#     # Hentikan jika kecepatannya sangat kecil
#     if abs(stone_velocity_x) < 0.1:
#         stone_velocity_x = 0
#     if abs(stone_velocity_y) < 0.1:
#         stone_velocity_y = 0
#
#     # Cegah batu masuk ke tembok
#     for wall in walls:
#         if stone_rect.colliderect(wall):
#             stone_rect.x, stone_rect.y = old_stone_x, old_stone_y
#             stone_velocity_x = 0
#             stone_velocity_y = 0

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
        velocity_y -= acceleration
        # player_rect.y -= player_speed
    if keys[pygame.K_s]:
        velocity_y += acceleration
        # player_rect.y += player_speed
    if keys[pygame.K_a]:
        velocity_x -= acceleration
        # player_rect.x -= player_speed
    if keys[pygame.K_d]:
        velocity_x += acceleration
        # player_rect.x += player_speed

    # Batasi kecepatan maksimum
    velocity_x = max(-max_speed, min(max_speed, velocity_x))
    velocity_y = max(-max_speed, min(max_speed, velocity_y))

    # Terapkan gesekan
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        velocity_x *= (1 - friction)
    if not keys[pygame.K_w] and not keys[pygame.K_s]:
        velocity_y *= (1 - friction)

    # Gerakkan pemain
    player_rect.x += int(velocity_x)
    player_rect.y += int(velocity_y)

    # Deteksi tabrakan dengan semua tembok
    for wall in walls:
        if player_rect.colliderect(wall):
            player_rect.x, player_rect.y = old_x, old_y
            velocity_x = 0
            velocity_y = 0
            break


    # Cek tabrakan dengan batu dan dorong batu
    for stone in stones:
        stone_rect = stone["rect"]
        if player_rect.colliderect(stone_rect):
            dx = stone_rect.centerx - player_rect.centerx
            dy = stone_rect.centery - player_rect.centery

            if abs(dx) > abs(dy):  # dorong horizontal
                if dx > 0:
                    stone["vx"] = 3
                    velocity_x *= 0.5
                else:
                    stone["vx"] = -3
                    velocity_x *= 0.5
            else:  # dorong vertikal
                if dy > 0:
                    stone["vy"] = 3
                    velocity_y *= 0.5
                else:
                    stone["vy"] = -3
                    velocity_y *= 0.5



    for stone in stones:
        stone_rect = stone["rect"]
        old_x, old_y = stone_rect.x, stone_rect.y

        stone_rect.x += int(stone["vx"])
        stone_rect.y += int(stone["vy"])

        # Tambahkan gesekan
        stone["vx"] *= (1 - stone_friction)
        stone["vy"] *= (1 - stone_friction)

        if abs(stone["vx"]) < 0.1:
            stone["vx"] = 0
        if abs(stone["vy"]) < 0.1:
            stone["vy"] = 0

        # Jika tabrakan dengan tembok, hentikan batu
        for wall in walls:
            if stone_rect.colliderect(wall):
                stone_rect.x = old_x
                stone_rect.y = old_y
                stone["vx"] = 0
                stone["vy"] = 0
                break



    # Gambar latar dan objek
    screen.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(screen, BROWN, wall)

    for stone in stones:
        pygame.draw.rect(screen, GRAY, stone["rect"])

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