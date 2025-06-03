from settings import SCREEN_HEIGHT, SCREEN_WIDTH, WORLD_HEIGHT, WORLD_WIDTH

class Camera:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0

    def apply(self, target_rect):
        return target_rect.move(self.offset_x, self.offset_y)

    def update(self, target):
        self.offset_x = -target.rect.centerx + SCREEN_WIDTH // 2
        self.offset_y = -target.rect.centery + SCREEN_HEIGHT // 2

        self.offset_x = min(0, self.offset_x)  # Kiri
        self.offset_x = max(-(WORLD_WIDTH - SCREEN_WIDTH), self.offset_x)  # Kanan
        self.offset_y = min(0, self.offset_y)  # Atas
        self.offset_y = max(-(WORLD_HEIGHT - SCREEN_HEIGHT), self.offset_y)  # Bawah
