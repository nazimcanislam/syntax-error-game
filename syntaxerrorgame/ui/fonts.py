#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import os.path
import pygame
import pygame.font


class Fonts:
	pygame.font.init()

	ENEMY_FONT = pygame.font.SysFont('Times New Roman', 48)

	FONT18 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 18)
	FONT32 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 32)
	FONT64 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 64)
