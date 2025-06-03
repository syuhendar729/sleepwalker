import unittest
import pygame
import sys
import types
from collections import defaultdict

# Patch settings and audio (sama seperti sebelumnya)
sys.modules['settings'] = types.SimpleNamespace(
    PLAYER_ACCEL=1,
    PLAYER_FRICTION=0.1,
    PLAYER_MAX_SPEED=5,
    BLUE=(0, 0, 255)
)
sys.modules['audio'] = types.SimpleNamespace(
    Audio=lambda: type("Audio", (), {"play": lambda self, sound, loop=False: None})()
)

pygame.display.init()
pygame.display.set_mode((1, 1))

_dummy_surface = pygame.Surface((30, 40))
def _dummy_load(path):
    return _dummy_surface.copy()
def _dummy_scale(img, size):
    return img.copy()
pygame.image.load = _dummy_load
pygame.transform.scale = _dummy_scale

from player.player_human import PlayerHuman

def make_keys_mock(*pressed_keys):
    keys = defaultdict(int)
    for code in pressed_keys:
        keys[code] = 1
    return keys

class TestPlayerHumanMovement(unittest.TestCase):
    def setUp(self):
        self.player = PlayerHuman(100, 100)

    def test_move_right(self):
        keys = make_keys_mock(pygame.K_d)
        old_vx = self.player.vx
        self.player.handle_input(keys)
        self.assertGreater(self.player.vx, old_vx)

    def test_move_left(self):
        keys = make_keys_mock(pygame.K_a)
        old_vx = self.player.vx
        self.player.handle_input(keys)
        self.assertLess(self.player.vx, old_vx)

    def test_move_up(self):
        keys = make_keys_mock(pygame.K_w)
        old_vy = self.player.vy
        self.player.handle_input(keys)
        self.assertLess(self.player.vy, old_vy)

    def test_move_down(self):
        keys = make_keys_mock(pygame.K_s)
        old_vy = self.player.vy
        self.player.handle_input(keys)
        self.assertGreater(self.player.vy, old_vy)

if __name__ == "__main__":
    unittest.main()
