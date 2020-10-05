#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import pygame.font


pygame.font.init()


# Pencere özellikleri
WIDTH = 1920
HEIGHT = 1080
FULLMODE = True

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (240, 240, 240)

# Düşman özellikleri
ENEMY_MARKS = (';', 'i++', 'j++', '{', '}', 'switch()', 'do while', 'implements', 'foreach()', 'public', 'protected', 'private', 'void', 'using', 'namespace','static', 'final', 'var', 'let', 'const', 'catch', 'throw', 'new', 'string[]', 'int[]', 'short', 'byte', 'long', 'double', 'char', 'char[]')
ENEMY_FONT = pygame.font.SysFont('Times New Roman', 48)

# Oyunun yazı tipleri
FONT18 = pygame.font.SysFont('Helvetica', 18, True)
FONT32 = pygame.font.SysFont('Helvetica', 30, True)
FONT64 = pygame.font.SysFont('Helvetica', 64, True)
