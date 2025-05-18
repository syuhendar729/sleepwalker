import pygame
import sys
import random
from property import Battery
from settings import *
from player import PlayerHuman
from stone import Stone
from wall import walls
from winning_condition import show_win_screen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sleep Walker Maze - Darkness")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.player = PlayerHuman(60, 60)
        self.stones = [Stone(800, 100), Stone(800, 700)]
        self.batteries = [Battery(5, 5), Battery(1175, 780)]

        self.start_ticks = pygame.time.get_ticks()
        self.running = True

        self.win_pos = self.get_random_position()
        self.win_radius = 20
        self.running = True
        self.won = False

    # Membuat posisi acak / memilih tempat acak
    def get_random_position(self):
        margin = 50 
        x = random.randint(margin, WIDTH - margin)
        y = random.randint(margin, HEIGHT - margin)
        return (x, y)

    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

        old_x, old_y = self.player.rect.x, self.player.rect.y
        self.player.update()

        # Hitung waktu mundur
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.time_left = max(0, 30 - seconds_passed)

        # Cek tabrakan dengan walls
        for wall in walls:
            if self.player.rect.colliderect(wall):
                self.player.rect.x, self.player.rect.y = old_x, old_y
                self.player.vx = 0
                self.player.vy = 0

        # Cek tabrakan dengan stones
        for stone in self.stones:
            if self.player.rect.colliderect(stone.rect):
                dx = stone.rect.centerx - self.player.rect.centerx
                dy = stone.rect.centery - self.player.rect.centery
                if abs(dx) > abs(dy):
                    stone.push(3 if dx > 0 else -3, 0)
                    self.player.vx *= 0.5
                else:
                    stone.push(0, 3 if dy > 0 else -3)
                    self.player.vy *= 0.5

        for stone in self.stones:
            stone.update(walls)

        # Cek tabrakan baterai
        for battery in self.batteries:
            if self.player.rect.colliderect(battery.rect) and not battery.is_taken:
                print("Berhasil mengambil baterai")
                battery.is_taken = True
                self.start_ticks += 30 * 1000  # tambah waktu

        # Cek kondisi menang
        player_center = self.player.rect.center
        dist = ((player_center[0] - self.win_pos[0]) ** 2 + (player_center[1] - self.win_pos[1]) ** 2) ** 0.5
        if dist < self.win_radius + self.player.rect.width // 2:
            self.won = True
            self.running = False
            # Tampilkan layar kemenangan
            show_win_screen(self.screen, WIDTH, HEIGHT)

    def draw(self):
        self.screen.fill(WHITE)

        for wall in walls:
            pygame.draw.rect(self.screen, BROWN, wall)

        for stone in self.stones:
            stone.draw(self.screen)

        for battery in self.batteries:
            if not battery.is_taken:
                battery.draw(self.screen)

        self.player.draw(self.screen)

        # Gambar lingkaran kemenangan
        pygame.draw.circle(self.screen, (0, 255, 0), self.win_pos, self.win_radius)

        # Efek gelap dengan lubang cahaya
        dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark_surface.fill((0, 0, 0, 255))  # full hitam 255

        light_radius = 60
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), self.player.rect.center, light_radius)

        self.screen.blit(dark_surface, (0, 0))

        # Timer (jika mau tampilkan)
        timer_text = self.font.render(f"Waktu: {self.time_left}", True, (255, 255, 255))
        self.screen.blit(timer_text, (10, 10))

        pygame.display.flip()
