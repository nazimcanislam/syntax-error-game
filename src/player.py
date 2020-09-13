#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import os
import os.path
import sys
import random

from src.enemy import Enemy
from src.constants import BLACK, FONT18, FONT32


class Player:
    """Oyun için oyuncu üretme sınıfı"""

    def __init__(self, name, live, window):
        self.name = name.strip().title()
        self.width = 50
        self.height = 50
        self.live = live
        self.window = window
        self.x = 30
        self.y = 80
        self.vel = 4.0
        self.run_vel = 1.2
        self.image = pygame.transform.smoothscale(pygame.image.load(os.path.join("assets", "player.png")), (self.width, self.height)).convert_alpha()

    def move(self, keys):
        """Karakterin hareketini sağlayan metod"""

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 10:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.x -= self.vel + self.run_vel
            else:
                self.x -= self.vel

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 50:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.y -= self.vel + self.run_vel
            else:
                self.y -= self.vel

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < self.window.get_width() - 10 - self.width:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.x += self.vel + self.run_vel
            else:
                self.x += self.vel

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.y + self.height) < self.window.get_height() - 50:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.y += self.vel + self.run_vel
            else:
                self.y += self.vel

    def show_name(self):
        """Karakterin ismini üstünde gösteren metod"""

        text = FONT18.render(self.name, True, BLACK).convert_alpha()
        self.window.blit(
            text,
            (
                self.x + self.width // 2 - text.get_width() // 2,
                self.y + self.height // 2 - text.get_height() // 2 - self.width + text.get_height() // 2,
            )
        )

    def show_live(self):
        """Karakterin canını ekranda gösteren metod"""

        self.window.blit(FONT32.render(f"Can: {self.live}", True, BLACK).convert_alpha(), (10, 10))

    def draw(self):
        """Karakteri yükleyip ekrana çizen metod"""

        self.window.blit(self.image, (self.x, self.y))

    def lost_live(self, value=1):
        """Karakterin can kaybetme metodu"""

        if self.live > 0:
            self.live -= value

    def is_collied(self, enemy):
        """Karakter ile rakiplerin çarpışmasını kontrol eden metod"""

        # Teşekkürler!
        # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection

        return (self.x < enemy.x + enemy.display.get_width()) and (self.x + self.width > enemy.x) and (self.y < enemy.y + enemy.display.get_height()) and (self.y + self.height > enemy.y)
