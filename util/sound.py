import pygame
import os


pygame.mixer.init()


class Sound:
    """Müzik dosyalarını aç ve oynat"""

    def __init__(self, folder: str, file: str):
        self.music: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join(folder, file))

    def play(self) -> None:
        """Çal keke!"""

        self.music.play()
    
    def play_and_repeat(self) -> None:
        """Çal ve asla durma!"""

        self.music.play(loops=-1)
