import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
lebar, tinggi = 640, 480
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Kotak Bergerak")

# Warna
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)

# Properti kotak
kotak = pygame.Rect(300, 220, 40, 40)  # x, y, width, height
kecepatan = 5

# Game loop
running = True
while running:
    pygame.time.Clock().tick(60)  # Batasi FPS ke 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakan dengan tombol keyboard
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT]:
        kotak.x -= kecepatan
    if tombol[pygame.K_RIGHT]:
        kotak.x += kecepatan
    if tombol[pygame.K_UP]:
        kotak.y -= kecepatan
    if tombol[pygame.K_DOWN]:
        kotak.y += kecepatan

    # Menggambar ulang layar
    layar.fill(PUTIH)
    pygame.draw.rect(layar, MERAH, kotak)
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
