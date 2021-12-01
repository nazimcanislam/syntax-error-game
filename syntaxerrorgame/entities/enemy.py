#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path
import random
import pygame
import pygame.font

from syntaxerrorgame.ui import ENEMY_FONT
from syntaxerrorgame.entities.entity import Entity


class Enemy(Entity):
    """
    Enemy constructor for game
    """
    
    def __init__(self, level, window):
        super().__init__()

        with open(file=os.path.join('gamedata', 'data.json'), mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

        self.level = level
        self.window = window

        self.mark = random.choice(self.data['enemy']['marks'])
        self.image = ENEMY_FONT.render(self.mark, True, self.data['colors']['black']).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.window.get_width() + 100, 2500 + self.level * 100)
        self.rect.y = random.randint(50, self.window.get_height() - 100)
        self.vel = random.uniform(4.0, 7.0)

    def draw(self):
        """
        Draw the enemy to window
        """

        self.window.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.x -= self.vel

    def is_outsided(self):
        """
        Is enemy get outside?
        :return: bool
        """

        return self.rect.x + self.image.get_width() <= 0
