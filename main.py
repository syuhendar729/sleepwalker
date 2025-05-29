import pygame
from scene import menu
from gameplay import Game

def main():
    pygame.init()
    # screen = pygame.display.set_mode((menu.SCREEN_WIDTH, menu.SCREEN_HEIGHT))
    pygame.display.set_caption("Game")

    while True:
        action = menu.menu_loop()  # jalankan menu, tunggu input

        if action == "start":
            game = Game()
            game.run()  # jalankan game


if __name__ == "__main__":
    main()
