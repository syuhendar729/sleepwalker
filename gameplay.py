import pygame
import sys
import random
from player.monster import Monster
from settings import *
from audio import Audio
from player.player_human import PlayerHuman
from property.property import Battery, Bed, Flash
from obstacle.stone import Stone
from obstacle.wall import walls
from scene.lose_condition import show_lose_screen
from scene.winning_condition import show_win_screen
from camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        # self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Sleep Walker Maze - Darkness")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.camera = Camera()

        self.player = PlayerHuman(40, 40)
        self.flash = Flash()
        self.monster = Monster(500, 740)
        self.stones = [Stone(720, 80), Stone(800, 700)]
        # self.stones = []
        self.batteries = [Battery(300, 280), Battery(800, 420)]

        self.start_ticks = pygame.time.get_ticks()

        self.running = True
        self.bed_pos = self.get_random_position()
        self.bed = Bed(self.bed_pos[0], self.bed_pos[1])

        # Music
        self.audio = Audio()

    # Membuat posisi acak / memilih tempat acak
    def get_random_position(self):
        margin = 50 
        x = random.randint(margin, WORLD_WIDTH - margin)
        y = random.randint(margin, WORLD_HEIGHT - margin)
        return (x, y)

    def run(self):
        self.audio.play('bs-gameplay.mp3')
        while self.running:
            self.clock.tick(60)
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
        # old_x, old_y = self.player.rect.x, self.player.rect.y
        self.player.update()
        self.player.move_and_collide(walls)
        self.camera.update(self.player)

        # Hitung waktu mundur
        seconds_passed = (pygame.time.get_ticks() - self.start_ticks) // 1000
        self.time_left = max(0, 30 - seconds_passed)

        # Cek sentuhan antara player dan stones
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

        # Cek sentuhan antara player dan baterai
        for battery in self.batteries:
            if self.player.rect.colliderect(battery.rect) and not battery.is_taken:
                print("Berhasil mengambil baterai")
                battery.is_taken = True
                self.start_ticks += 30 * 1000  # tambah waktu

        # Cek sentuhan antara monster dan player
        if self.player.rect.colliderect(self.monster.rect):
            self.player.is_alive = False            
            self.running = False
            self.audio.stop_music()
            show_lose_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Memerbarui monster
        self.monster.update() 

        # Cek sentuhan antara player dan finish
        if self.player.rect.colliderect(self.bed.rect):
            print("Berhasil ke Finish")
            self.running = False
            self.audio.stop_music()
            show_win_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)


    def draw(self):
        self.screen.fill(GRAY)

        for wall in walls:
            # pygame.draw.rect(self.screen, BROWN, wall)
            rect = wall.rect if hasattr(wall, 'rect') else wall
            pygame.draw.rect(self.screen, BROWN, self.camera.apply(rect))

        for stone in self.stones:
            # stone.draw(self.screen)
            stone.draw(self.screen, self.camera)

        for battery in self.batteries:
            if not battery.is_taken:
                # battery.draw(self.screen)
                battery.draw(self.screen, self.camera)

        # Gambar player di posisi sekarang
        if self.player.is_alive:
            # self.player.draw(self.screen)
            self.player.draw(self.screen, self.camera)

        # Gambar posisi monster
        # self.monster.draw(self.screen)
        self.monster.draw(self.screen, self.camera)

        # Gambar lingkaran finish
        # pygame.draw.circle(self.screen, (0, 255, 0), self.bed_pos, 20)
        pygame.draw.circle(
            self.screen,
            (0, 255, 0),
            (self.bed_pos[0] + self.camera.offset_x, self.bed_pos[1] + self.camera.offset_y),
            20
        )

        # Efek gelap dengan lubang cahaya
        dark_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        dark_surface.fill((0, 0, 0, DARKNESS))  # full hitam 255

        # Jika waktu habis maka senter akan mati dan kalah
        if self.time_left > 0:
            self.flash.drawlight(dark_surface, self.player, self.camera)
            # self.flash.drawlight(dark_surface, self.player)
            # light_radius = 50
            # pygame.draw.circle(dark_surface, (0, 0, 0, 0), self.player.rect.center, light_radius)
        else:             
            self.audio.stop_music()
            show_lose_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.screen.blit(dark_surface, (0, 0))

        # Timer (jika mau tampilkan)
        timer_text = self.font.render(f"Waktu: {self.time_left}", True, (255, 255, 255))
        self.screen.blit(timer_text, (10, 10))

        pygame.display.flip()
