import pygame
import os

class Audio:
    def __init__(self):
        pygame.mixer.init()
        self.current_music = None
        self.audio_folder = os.path.join(os.path.dirname(__file__), 'audio')


    def play(self, filename, loop = True, volume = 0.5):
        path = os.path.join(self.audio_folder, filename)
        if self.current_music != path:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1 if loop else 0)
            self.current_music= path

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()



