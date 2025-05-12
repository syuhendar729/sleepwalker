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
    # pygame.Rect(x, y, width, height)
    pygame.Rect(0, -20, 1200, 20),         # batas atas
    pygame.Rect(-20, 0, 20, 800),         # batas kiri
    pygame.Rect(0, 800, 1200, 20),         # batas bawah
    pygame.Rect(1200, 0, 20, 800),         # batas kanan

    # wall utama
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 100, 20, 300),
    pygame.Rect(100, 480, 600, 20),
    pygame.Rect(680, 100, 20, 400),
    pygame.Rect(200, 200, 400, 20),
    pygame.Rect(200, 200, 20, 200),
    pygame.Rect(580, 200, 20, 200),
    pygame.Rect(300, 300, 200, 20),

    # tambahan wall dalam - tidak rapat
    pygame.Rect(150, 150, 20, 100),      # vertikal kecil
    pygame.Rect(150, 230, 80, 20),       # horizontal bawahnya

    pygame.Rect(250, 120, 20, 150),      # vertikal
    pygame.Rect(250, 120, 100, 20),      # horizontal atas

    pygame.Rect(400, 130, 20, 150),      # vertikal
    pygame.Rect(330, 200, 100, 20),      # horizontal atas

    pygame.Rect(360, 350, 20, 100),      # vertikal bawah area tengah
    pygame.Rect(360, 350, 100, 20),      # horizontal

    pygame.Rect(500, 320, 20, 100),      # kanan tengah vertikal

    pygame.Rect(150, 530, 200, 20),      # bawah kiri horizontal
    pygame.Rect(150, 530, 20, 120),      # vertikal ujungnya

    pygame.Rect(350, 600, 20, 80),       # tengah bawah vertikal
    pygame.Rect(200, 680, 200, 20),      # dasar kiri horizontal

    pygame.Rect(700, 500, 20, 150),      # kanan bawah vertikal
    pygame.Rect(700, 650, 180, 20),      # horizontal kanan bawah
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
