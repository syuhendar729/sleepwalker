import pygame
from player.player import Player
from settings import BLUE, PLAYER_MAX_SPEED


class PlayerHuman(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=40, color=BLUE, max_speed=PLAYER_MAX_SPEED)
        
        # Load semua frame animasi jalan ke kanan
        self.frames_right = [
            pygame.image.load("assets/player_human/R1.png").convert_alpha(),
            pygame.image.load("assets/player_human/R2.png").convert_alpha(),
            pygame.image.load("assets/player_human/R3.png").convert_alpha()
        ]
        self.frames_right = [pygame.transform.scale(img, (30, 40)) for img in self.frames_right]
        
        # Load semua frame animasi jalan ke kiri
        self.frames_left = [
            pygame.image.load("assets/player_human/L1.png").convert_alpha(),
            pygame.image.load("assets/player_human/L2.png").convert_alpha(),
            pygame.image.load("assets/player_human/L3.png").convert_alpha()
        ]
        self.frames_left = [pygame.transform.scale(img, (30, 40)) for img in self.frames_left]

        self.current_frame = 0
        self.animation_speed = 0.15
        self.frame_timer = 0
        
        # Default image dan rect
        self.image = self.frames_right[0]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.is_won = False
        self.is_lose = False
        self.is_alive = True

        self.direction = "right"  # default arah player


    def move_and_collide(self, walls):
        # Gerak di X
        # self.rect.x += int(self.vx)
        self.rect.x += self.vx
        for wall in walls:
            if self.rect.colliderect(wall.rect if hasattr(wall, 'rect') else wall):
                if self.vx > 0:  # Gerak ke kanan, tabrak kanan
                    self.rect.right = (wall.rect if hasattr(wall, 'rect') else wall).left
                elif self.vx < 0:  # Gerak ke kiri, tabrak kiri
                    self.rect.left = (wall.rect if hasattr(wall, 'rect') else wall).right
                self.vx = 0  # Hentikan gerak X

        # Gerak di Y
        # self.rect.y += int(self.vy)
        self.rect.y += self.vy
        for wall in walls:
            if self.rect.colliderect(wall.rect if hasattr(wall, 'rect') else wall):
                if self.vy > 0:  # Gerak ke bawah, tabrak bawah
                    self.rect.bottom = (wall.rect if hasattr(wall, 'rect') else wall).top
                elif self.vy < 0:  # Gerak ke atas, tabrak atas
                    self.rect.top = (wall.rect if hasattr(wall, 'rect') else wall).bottom
                self.vy = 0  # Hentikan gerak Y

    def update(self):
        
        keys = pygame.key.get_pressed()
        
        moving_right = keys[pygame.K_d]
        moving_left = keys[pygame.K_a]
        moving_up = keys[pygame.K_w]
        moving_down = keys[pygame.K_s]

        if moving_right:
            self.direction = "right"
            self.frame_timer += self.animation_speed
            if self.frame_timer >= 1:
                self.frame_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames_right)
            self.image = self.frames_right[self.current_frame]

        elif moving_left:
            self.direction = "left"
            self.frame_timer += self.animation_speed
            if self.frame_timer >= 1:
                self.frame_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames_left)
            self.image = self.frames_left[self.current_frame]

        elif moving_up or moving_down:
            if self.direction == "right":
                self.frame_timer += self.animation_speed
                if self.frame_timer >= 1:
                    self.frame_timer = 0
                    self.current_frame = (self.current_frame + 1) % len(self.frames_right)
                self.image = self.frames_right[self.current_frame]
            elif self.direction == "left":
                self.frame_timer += self.animation_speed
                if self.frame_timer >= 1:
                    self.frame_timer = 0
                    self.current_frame = (self.current_frame + 1) % len(self.frames_left)
                self.image = self.frames_left[self.current_frame]


        else:
            # Jika tidak bergerak kiri/kanan, reset animasi ke frame pertama dari arah terakhir
            self.current_frame = 0
            self.frame_timer = 0
            if self.direction == "right":
                self.image = self.frames_right[0]
            else:
                self.image = self.frames_left[0]

        self.rect.topleft = (self.rect.x, self.rect.y)

    def draw(self, screen, camera=None):
        # screen.blit(self.image, self.rect)
        if camera:
            screen.blit(self.image, camera.apply(self.rect))
        else:
            screen.blit(self.image, self.rect)
