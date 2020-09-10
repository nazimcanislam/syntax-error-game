#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import os
import random
import typing


class Enemy:
    """Oyun için düşman üretme sınıfı"""

    level: int
    window: pygame.Surface
    marks: typing.Tuple[str]
    choice: int
    current_mark: str
    vel: int
    x: int
    y: int
    font1: pygame.font.Font
    display: pygame.Surface
    width: int
    height: int

    def __init__(self, level: int, window: pygame.Surface):
        self.level = level
        self.window = window

        self.marks = (";", "i++", "j++", "{", "}", "switch()", "do while", "implements", "foreach()",
                      "public", "protected", "private", "void", "using", "namespace", "static", "final", "var", "let", "const", "catch", "throw")
        self.choice = random.randint(0, len(self.marks) - 1)
        self.current_mark = self.marks[self.choice]

        self.vel = random.uniform(1.2, 1.8)

        self.x = random.randint(
            self.window.get_width() + 100, 2500 + self.level * 100)
        self.y = random.randint(50, self.window.get_height() - 100)

        self.font1 = pygame.font.SysFont("Times", 48)

        self.display = self.font1.render(
            self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width = self.display.get_width()
        self.height = self.display.get_height()

    def draw(self) -> None:
        """Düşmanın kendisini ekrana çizen metod"""

        self.display = self.font1.render(
            self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width = self.display.get_width()
        self.height = self.display.get_height()

        self.window.blit(self.display, (self.x, self.y))

        self.x -= self.vel

    def is_outsided(self) -> bool:
        """Düşman sol tarafntan yani ekrandan çıktı mı?"""

        return self.x <= -50
