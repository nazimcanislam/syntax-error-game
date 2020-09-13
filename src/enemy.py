#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import random
import pygame
import pygame.font

from src.constants import BLACK, ENEMY_MARKS, ENEMY_FONT


pygame.font.init()


class Enemy:
    """Oyun için düşman üretme sınıfı"""

    def __init__(self, level, window):
        self.level = level
        self.window = window

        self.mark = random.choice(ENEMY_MARKS)

        self.vel = random.uniform(4.0, 7.0)
        self.x = random.randint(self.window.get_width() + 100, 2500 + self.level * 100)
        self.y = random.randint(50, self.window.get_height() - 100)

        self.display = ENEMY_FONT.render(self.mark, True, BLACK).convert_alpha()

    def draw(self):
        """Düşmanın kendisini ekrana çizen metod"""

        self.window.blit(self.display, (self.x, self.y))
        self.x -= self.vel

    def is_outsided(self):
        """Düşman ekrandan yani sol tarafntan çıktı mı?"""

        return self.x + self.display.get_width() <= 0
