import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Mengatur ukuran layar 
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Game Menu")

# Load gambar background (Memuat gambar bacground)
background = pygame.image.load("assets/sleepwalk_menu.png")  
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Deklarasi warna untuk tulisan
warnaStartQuit = (0, 0, 0) # Untuk warna utama start dan quit (0,0,0) - RGB Black
LIGHT_BLUE = (173, 216, 230) # Untuk transformasi warna

# Mengatur jenis dan ukuran Font
menu_font = pygame.font.SysFont("arial", 30)

# Membuat teks start dan quit
start_text = menu_font.render("Start Game", True, warnaStartQuit)
quit_text = menu_font.render("Quit", True, warnaStartQuit)

# Mengatur posisi teks
start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2.94, 515)) # // pembagi bilangan bulat untuk kordinat x
quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 1.42, 515))  # // pembagi bilangan bulat untuk kordinat x


def draw_menu():
    screen.blit(background, (0,0)) # Blit, fungsi pygame untuk mengcopy dan menempelkan backgorund

    # Fungsi pada pygame untuk mendapatkan mouse kita
    mouse_pos = pygame.mouse.get_pos()
  
  # Pengecekan apakah mouse ada di teks start?
    if start_rect.collidepoint(mouse_pos):
        start_text_color = LIGHT_BLUE  # Ubah warna teks saat mouse berada di atas
    else:
        start_text_color = warnaStartQuit

    # Pengecekan apakah mouse ada di teks start?
    if quit_rect.collidepoint(mouse_pos):
        quit_text_color = LIGHT_BLUE  # Ubah warna teks saat mouse berada di atas
    else:
        quit_text_color = warnaStartQuit

    # Membuat gambar teks dengan warna yang sudah disesuaikan
    start_text = menu_font.render("Start Game", True, start_text_color)
    quit_text = menu_font.render("Quit", True, quit_text_color)

    screen.blit(start_text, start_rect)
    screen.blit(quit_text, quit_rect)

    pygame.display.update()

    #inisialisasi musik
    

def menu_loop():
    try:
        while True:
            draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(event.pos):
                        return "start"
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
    except Exception as e:
        print(f"Error in menu loop: {e}")



