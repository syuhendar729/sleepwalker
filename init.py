import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Movement with WASD")

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Data pemain
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Game loop
running = True
while running:
    pygame.time.Clock().tick(60)  # Batasi ke 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ambil semua tombol yang ditekan
    keys = pygame.key.get_pressed()
    
    # Gerakkan pemain
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Gambar latar belakang dan pemain
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
