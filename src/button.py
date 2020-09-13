#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import pygame.image
import pygame.event
import pygame.mouse


class Button:
    """Oyunun menüsü için tuş üretme sınıfı"""

    def __init__(self, window, image, pos, size):
        self.window = window
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]

    def draw(self):
        """Ekrana çiz"""

        self.window.blit(self.image, (self.x, self.y))

    def is_clicked(self):
        """
        Tuşun üzerine tıklanınca
        Bu metod, 'game.py' dosyasında event_handler() metodunun içindeki MOUSEBUTTONDOWN bölümünde çağırılmalı
        """

        return self.x <= pygame.mouse.get_pos()[0] <= self.x + self.width and self.y <= pygame.mouse.get_pos()[1] <= self.y + self.height
