#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path
import pygame
import pygame.image
import pygame.transform
import pygame.draw
import pygame.event

from typing import Dict

from syntaxerrorgame.ui import FONT18
from syntaxerrorgame.ui.label import Label
from syntaxerrorgame.entities.entity import Entity


class Player(Entity):
    """
    Player constructor class for game
    Construct only one player!
    """

    def __init__(self, name, live, window):
        """
        :param: name: str
        :param: live: int
        :param: window: pygame.Surface
        """

        super().__init__()

        with open(file=os.path.join('gamedata', 'data.json'), mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

        self.name = name.strip().title()
        self.width = 50
        self.height = 50
        self.live = live
        self.window = window
        self.image = pygame.transform.smoothscale(
            pygame.image.load(os.path.join("assets", "images/player.png")),
            (self.width, self.height)
        ).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 80
        self.vel = 4.0
        self.run_vel = 1.2
        self.moving = {
            'left': False,
            'up': False,
            'right': False,
            'down': False
        }
        self.name_label = Label(
            text=self.name,
            font_name=os.path.join('assets', 'fonts/VT323-Regular.ttf'),
            size=18,
            color=self.data['colors']['black'],
            is_sys_font=False,
        )

    def move(self, event):
        """
        This method moves the player
        :param: event: pygame.event.Event
        """

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving['left'] = True
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.moving['up'] = True
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving['right'] = True
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving['down'] = True

            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                self.vel += self.run_vel
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving['left'] = False
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.moving['up'] = False
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving['right'] = False
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving['down'] = False

            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                self.vel -= self.run_vel

    def draw(self):
        """
        This method draws player to window
        """

        if self.moving['left'] and self.rect.x > 0 + 10:
            self.rect.x -= self.vel

        if self.moving['up'] and self.rect.y > 0 + 30:
            self.rect.y -= self.vel

        if self.moving['right'] and self.rect.x + self.image.get_width() + 10 < self.window.get_width():
            self.rect.x += self.vel

        if self.moving['down'] and self.rect.y + self.image.get_height() + 10 < self.window.get_height():
            self.rect.y += self.vel

        self.window.blit(self.image, (self.rect.x, self.rect.y))

    def show_name(self):
        """
        This method shows player name on player head
        """

        self.name_label.draw(
            self.window,
            (
                self.rect.x + self.width // 2 - self.name_label.surface.get_width() // 2,
                self.rect.y + self.height // 2 - self.name_label.surface.get_height() // 2 - self.width + self.name_label.surface.get_height() // 2,
            )
        )

    def lost_live(self, value=1):
        """
        This method decreases one live from player if player already has lives
        So if player hasn't any lives, this method won't work
        :param: value: int
        """

        if self.live > 0:
            self.live -= value
