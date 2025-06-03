import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
lebar, tinggi = 640, 480
layar = pygame.display.set_mode((lebar, tinggi)) # ngatur ukuran layar (lebar, tinggi)
pygame.display.set_caption("Segitiga Bergerak") # ngatur judul
# Memanggil fungsi di pygame untuk ....
# 

# Warna
PUTIH = (255, 255, 255) # RGB (Red Greed Blue)
MERAH = (201, 14, 14)

# Properti kotak
kotak = pygame.Rect(320, 220, 40, 40)  # x, y, width, height (Rectangle = kotak = persegi panjang)
kecepatan = 5
kotak2 = pygame.Rect(0, 0, 40, 40)

# Game loop
running = True

while running:
    # Batasi FPS ke 60
    pygame.time.Clock().tick(60)  

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # Gerakan dengan tombol keyboard
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT] or tombol[pygame.K_a]: # panah ke kiri
        kotak.x -= kecepatan
        # si x dikurang kecepatan
    if tombol[pygame.K_RIGHT] or tombol[pygame.K_d]:
        kotak.x += kecepatan
        # x ditambah kecepatan
    if tombol[pygame.K_UP] or tombol[pygame.K_w]:
        kotak.y -= kecepatan
        # y dikurang kecepatan
    if tombol[pygame.K_DOWN] or tombol[pygame.K_s]:
        kotak.y += kecepatan
        # si y ditambah dengan kecepatan

    # Menggambar ulang layar
    layar.fill(PUTIH)
    pygame.draw.rect(layar, MERAH, kotak)
    pygame.draw.rect(layar, MERAH, kotak2) 
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
