import pygame
import sys

def show_win_screen(screen, width, height):
    # Settingan warna
    white = (255, 255, 255)
    hover_color = (238, 64, 0)

    # Settingan font
    font = pygame.font.SysFont("arial", 48)
    button_font = pygame.font.SysFont("arial", 32)

    # Load gambar background kemenangan
    bg_image = pygame.image.load("winning.png")
    bg_image = pygame.transform.scale(bg_image, (width, height))

    # Rect posisi text
    play_again_rect = pygame.Rect(0, 0, 200, 50)
    play_again_rect.center = (width // 2, height // 2 + 120)

    quit_rect = pygame.Rect(0, 0, 200, 50)
    quit_rect.center = (width // 2, height // 2 + 170)

    while True:
        screen.blit(bg_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect teks
        if play_again_rect.collidepoint(mouse_pos):
            play_again_text = button_font.render("Play Again", True, hover_color)
        else:
            play_again_text = button_font.render("Play Again", True, white)

        if quit_rect.collidepoint(mouse_pos):
            quit_text = button_font.render("Quit", True, hover_color)
        else:
            quit_text = button_font.render("Quit", True, white)

        # Mengcopy text ke layar
        screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))
        screen.blit(quit_text, quit_text.get_rect(center=quit_rect.center))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    return "play_again"
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
