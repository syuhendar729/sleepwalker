
import pygame
from settings import HEIGHT, WHITE, WIDTH

class Monster:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.vel_x = 1
        self.vel_y = 1

        # Load animasi kiri dan kanan
        self.left_frames = [pygame.image.load(f"assets/monster/L{i}E.png").convert_alpha() for i in range(1, 10)]
        self.right_frames = [pygame.image.load(f"assets/monster/R{i}E.png").convert_alpha() for i in range(1, 10)]
        self.left_frames = [pygame.transform.scale(img, (50, 50)) for img in self.left_frames]
        self.right_frames = [pygame.transform.scale(img, (50, 50)) for img in self.right_frames]

        self.current_frames = self.right_frames  # Default ke kanan
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 100  # ms per frame

        self.last_update = pygame.time.get_ticks()

    def update(self):
        # Update posisi
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Jika menyentuh sisi layar, balik arah (pantul)
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.vel_x *= -1
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.vel_y *= -1

        # Pilih animasi berdasarkan arah
        if self.vel_x < 0:
            self.current_frames = self.left_frames
        else:
            self.current_frames = self.right_frames

        # Update animasi (frame)
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.current_frames)

    def draw(self, screen):
        # Gambar frame animasi di posisi monster
        current_image = self.current_frames[self.frame_index]
        # Sesuaikan posisi gambar dengan rect
        screen.blit(current_image, self.rect)

