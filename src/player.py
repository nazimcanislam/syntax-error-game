#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import os
import os.path
import sys
import random
import termcolor

from src.enemy import Enemy
from src import others


class Player:
    """Oyun için oyuncu üretme sınıfı"""

    name: str
    width: int
    height: int
    live: int
    window: pygame.Surface
    x: int
    y: int
    vel: float
    run_vel: float
    image_path: str
    image: pygame.Surface
    limits: dict
    font1: pygame.font.Font
    font2: pygame.font.Font

    def __init__(self, name: str, live: int, window: pygame.Surface):
        self.name = name.strip()
        self.width = 50
        self.height = 50
        self.live = live
        self.window = window

        self.x = 30
        self.y = 80
        self.vel = 4.0
        self.run_vel = 1.2

        try:
            self.image_path = os.path.join("assets", "player.png")
            self.image = pygame.transform.smoothscale(
                pygame.image.load(self.image_path),
                (self.width, self.height)
            ).convert_alpha()
        except pygame.error:
            print(termcolor.colored("HATA: Karakter resmi bulunamadı!", "red"))
            print(termcolor.colored(
                f"İPUCU: Lütfen assets klasöründeki 'player.png' resmin olduğundan emin olun veya '{os.path.basename(__file__)}'' dosyasını kontrol edin...", "yellow"))
            sys.exit(0)
        except Exception:
            print(termcolor.colored(
                "HATA: Bilinmeyen bir hata meydana geldi!", "red"))

        self.limits = {
            "left": 10,
            "top": 50,
            "right": self.window.get_width() - 10 - self.width,
            "bottom": self.window.get_height() - 50
        }

        self.font1 = pygame.font.SysFont(
            "Helvetica", 18, True)
        self.font2 = pygame.font.SysFont(
            "Helvetica", 32, True)

    def move(self, keys: tuple) -> None:
        """Karakterin hareketini sağlayan metod"""

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > self.limits["left"]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.x -= self.vel + self.run_vel
            else:
                self.x -= self.vel

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > self.limits["top"]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.y -= self.vel + self.run_vel
            else:
                self.y -= self.vel

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < self.limits["right"]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.x += self.vel + self.run_vel
            else:
                self.x += self.vel

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.y + self.height) < self.limits["bottom"]:
            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                self.y += self.vel + self.run_vel
            else:
                self.y += self.vel

    def show_name(self) -> None:
        """Karakterin ismini üstünde gösteren metod"""

        text: pygame.Surface = self.font1.render(
            self.name, True, others.BLACK).convert_alpha()
        self.window.blit(
            text,
            (
                self.x + self.width // 2 - text.get_width() // 2,
                self.y + self.height // 2 - text.get_height() // 2 - self.width +
                text.get_height() // 2,
            )
        )

    def show_live(self) -> None:
        """Karakterin canını gösteren metod"""

        self.window.blit(self.font2.render(
            f"Can: {self.live}", True, others.BLACK).convert_alpha(), (10, 10))

    def draw(self) -> None:
        """Karakteri yükleyen metod"""

        self.window.blit(self.image, (self.x, self.y))

    def lost_live(self, value: int = 1) -> None:
        """Karakterin can kaybetme metodu"""

        if self.live > 0:
            self.live -= value

    def is_collied(self, enemy: Enemy) -> bool:
        """Karakter ile rakiplerin çarpışmasını kontrol eden metod"""

        # Teşekkürler!
        # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
        if (self.x < enemy.x + enemy.width) and \
                (self.x + self.width > enemy.x) and \
            (self.y < enemy.y + enemy.height) and \
                (self.y + self.height > enemy.y):
            return True
