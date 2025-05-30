import pygame
from scene import menu
from game import Game

def main():
    pygame.init()
    pygame.display.set_caption("Game")

    try:
        while True:
            action = menu.menu_loop()  # jalankan menu, tunggu input

            if action == "start":
                game = Game()
                game.run()  # jalankan game
    except Exception as e:
        print(f"Critical error in main loop: {e}")
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
