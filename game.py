import pygame
import sys
import random
from player.monster import Monster
from settings import *
from audio import Audio
from player.player_human import PlayerHuman
from property.property import Battery, CircleVictory, Flash
from obstacle.stone import Stone
from obstacle.wall import walls
from scene.lose_condition import show_lose_screen
from scene.winning_condition import show_win_screen
from camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sleep Walker Maze - Darkness")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 36)
        self.camera = Camera()

        self._player = PlayerHuman(40, 40)
        self._flash = Flash()
        self._monster = Monster(500, 740)
        self._stones = [Stone(720, 80), Stone(800, 700)]
        self._batteries = [Battery(300, 280), Battery(800, 420)]

        self._start_ticks = pygame.time.get_ticks()
        self._running = True
        self._finish_pos = self._get_random_position()
        self._finish = CircleVictory(self._finish_pos[0], self._finish_pos[1])

        self._audio = Audio()
        self._time_left = 30

    def _get_random_position(self):
        margin = 50
        x = random.randint(margin, WORLD_WIDTH - margin)
        y = random.randint(margin, WORLD_HEIGHT - margin)
        return (x, y)

    def run(self):
        self._audio.play('bs-gameplay.mp3')
        while self._running:
            self.clock.tick(60)
            self._handle_events()
            self._update()
            self._draw()
        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _update(self):
        keys = pygame.key.get_pressed()
        self._player.handle_input(keys)
        self._player.update()
        self._player.move_and_collide(walls)
        self.camera.update(self._player)

        self._update_time()

        self._handle_stone_collisions()
        self._update_stones()
        self._handle_battery_pickup()
        self._handle_monster_collision()
        self._monster.update()
        self._handle_finish_reached()

    def _update_time(self):
        seconds_passed = (pygame.time.get_ticks() - self._start_ticks) // 1000
        self._time_left = max(0, 30 - seconds_passed)

    def _handle_stone_collisions(self):
        for stone in self._stones:
            if self._player.rect.colliderect(stone.rect):
                dx = stone.rect.centerx - self._player.rect.centerx
                dy = stone.rect.centery - self._player.rect.centery
                if abs(dx) > abs(dy):
                    stone.push(3 if dx > 0 else -3, 0)
                    self._player.vx *= 0.5
                else:
                    stone.push(0, 3 if dy > 0 else -3)
                    self._player.vy *= 0.5

    def _update_stones(self):
        for stone in self._stones:
            stone.update(walls)

    def _handle_battery_pickup(self):
        for battery in self._batteries:
            if self._player.rect.colliderect(battery.rect) and not battery.is_taken:
                print("Berhasil mengambil baterai")
                battery.is_taken = True
                self._start_ticks += 30 * 1000  # tambah waktu
                self._batteries.remove(battery)

    def _handle_monster_collision(self):
        if self._player.rect.colliderect(self._monster.rect):
            self._player.is_alive = False
            self._running = False
            self._audio.stop_music()
            show_lose_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    def _handle_finish_reached(self):
        if self._player.rect.colliderect(self._finish.rect):
            print("Berhasil ke Finish")
            self._running = False
            self._audio.stop_music()
            show_win_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    def _draw(self):
        self.screen.fill(GRAY)

        # Gabungkan semua objek ke list untuk digambar
        objects = [self._player, self._monster] + self._stones + self._batteries + walls + [self._finish]
        for obj in objects:
            obj.draw(self.screen, self.camera)

        dark_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        dark_surface.fill((0, 0, 0, DARKNESS))

        if self._time_left > 0:
            self._flash.drawlight(dark_surface, self._player, self.camera)
        else:
            self._audio.stop_music()
            show_lose_screen(self.screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        self.screen.blit(dark_surface, (0, 0))

        timer_text = self.font.render(f"Waktu: {self._time_left}", True, (255, 255, 255))
        self.screen.blit(timer_text, (10, 10))

        pygame.display.flip()
