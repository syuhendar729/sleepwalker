import pygame
import sys
import random
from settings import *
from player import Player
from stone import Stone
from wall import walls

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sleep Walker Maze - Darkness")
clock = pygame.time.Clock()

# ========== MENU CONFIGURATION ==========
SCREEN_WIDTH = WIDTH
SCREEN_HEIGHT = HEIGHT
menu_font = pygame.font.SysFont("arial", 30)
background = pygame.image.load("sleepwalk_menu.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

warnaStartQuit = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

start_text = menu_font.render("Start Game", True, warnaStartQuit)
quit_text = menu_font.render("Quit", True, warnaStartQuit)
start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2.94, 515))
quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 1.42, 515))


def draw_menu():
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    start_color = LIGHT_BLUE if start_rect.collidepoint(mouse_pos) else warnaStartQuit
    quit_color = LIGHT_BLUE if quit_rect.collidepoint(mouse_pos) else warnaStartQuit

    start_text = menu_font.render("Start Game", True, start_color)
    quit_text = menu_font.render("Quit", True, quit_color)

    screen.blit(start_text, start_rect)
    screen.blit(quit_text, quit_rect)
    pygame.display.update()


def menu_loop():
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    return
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


def get_random_position():
    margin = 50
    x = random.randint(margin, WIDTH - margin)
    y = random.randint(margin, HEIGHT - margin)
    return (x, y)


def show_win_screen():
    font = pygame.font.SysFont("arial", 60)
    text = font.render("You Win!", True, (0, 255, 0))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill((0, 0, 0))
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.delay(3000)


def start_game():
    player = Player(60, 60)
    stones = [Stone(800, 100), Stone(800, 700)]

    win_pos = get_random_position()
    win_radius = 25

    running = True
    won = False

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        old_x, old_y = player.rect.x, player.rect.y
        player.update()

        for wall in walls:
            if player.rect.colliderect(wall):
                player.rect.x, player.rect.y = old_x, old_y
                player.vx = 0
                player.vy = 0

        for stone in stones:
            if player.rect.colliderect(stone.rect):
                dx = stone.rect.centerx - player.rect.centerx
                dy = stone.rect.centery - player.rect.centery
                if abs(dx) > abs(dy):
                    stone.push(3 if dx > 0 else -3, 0)
                    player.vx *= 0.5
                else:
                    stone.push(0, 3 if dy > 0 else -3)
                    player.vy *= 0.5

        for stone in stones:
            stone.update(walls)

        screen.fill(WHITE)
        for wall in walls:
            pygame.draw.rect(screen, BROWN, wall)
        for stone in stones:
            stone.draw(screen)
        player.draw(screen)

        # Gambar lingkaran kemenangan
        pygame.draw.circle(screen, (0, 255, 0), win_pos, win_radius)

        # Cek kemenangan
        player_center = player.rect.center
        dist = ((player_center[0] - win_pos[0]) ** 2 + (player_center[1] - win_pos[1]) ** 2) ** 0.5
        if dist < win_radius + player.rect.width // 2:
            won = True
            running = False

        # Efek gelap
        dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        dark_surface.fill((0, 0, 0, 255))
        pygame.draw.circle(dark_surface, (0, 0, 0, 0), player.rect.center, 60)
        screen.blit(dark_surface, (0, 0))

        pygame.display.flip()

    if won:
        show_win_screen()


# MAIN LOOP
if __name__ == "__main__":
    menu_loop()
    start_game()
    pygame.quit()
    sys.exit()
