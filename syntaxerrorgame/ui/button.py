#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path
import pygame
import pygame.image
import pygame.event
import pygame.mouse

from syntaxerrorgame.entities.entity import Entity


class Button(Entity):
    """
    Button constructor class for game
    """

    def __init__(self, window, image, pos, size):
        """
        :param: window: pygame.Surface
        :param: image: pygame.Surface
        :param: pos: Tuple[int, int]
        :param: size: Tuple[int, int]
        """

        super().__init__()
        
        with open(file=os.path.join('gamedata', 'data.json'), mode='r', encoding='utf-8') as file:
            self.data = json.load(file)
        
        self.window = window
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.width = size[0]
        self.height = size[1]

    def draw(self):
        """
        Draw this button to window
        """

        self.window.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self):
        """
        This is a click listener
        Call this method in game.py/Game().event_handler() method, then inside for loop give it event
        :return: bool
        """

        return self.rect.x <= pygame.mouse.get_pos()[0] <= self.rect.x + self.width\
            and self.rect.y <= pygame.mouse.get_pos()[1] <= self.rect.y + self.height
