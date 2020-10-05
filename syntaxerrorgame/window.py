#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import os.path
import pygame
import pygame.display


class Window:
    """Oyunun penceresini oluşturma sınıfı"""

    def __init__(self, size, title, full_screen=False):
        # Oyunun genişlik, yükleklik ve başlığını tanımla.
        self.width = size[0]
        self.height = size[1]
        self.title = title

        # Ekranı ortala
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Pencereyi oluştur
        if full_screen:
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
                pygame.FULLSCREEN,
            )
        else:
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
            )

        pygame.display.set_caption(self.title)

        self.favicon_image = pygame.image.load(os.path.join("assets", "favicon.png")).convert_alpha()
        pygame.display.set_icon(pygame.transform.scale(self.favicon_image, (128, 128)))

    def get(self):
        """Oyun penceresini al"""

        return self.screen
