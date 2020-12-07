#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path
import pygame
import pygame.draw


class Entity:
    """
    An entity class for game objects
    """

    def __init__(self):
        super().__init__()

        with open(file=os.path.join('gamedata', 'data.json'), mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

    def draw(self, window):
        """
        Draw entity to window
        """

        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_hitbox(self):
        """
        This method draws the hitbox
        """ 

        pygame.draw.line(self.window, self.data['colors']['red'], (self.rect.topleft), (self.rect.bottomleft), 2)
        pygame.draw.line(self.window, self.data['colors']['red'], (self.rect.topleft), (self.rect.topright), 2)
        pygame.draw.line(self.window, self.data['colors']['red'], (self.rect.topright), (self.rect.bottomright), 2)
        pygame.draw.line(self.window, self.data['colors']['red'], (self.rect.bottomleft), (self.rect.bottomright), 2)
