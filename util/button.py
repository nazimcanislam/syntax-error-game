#!/usr/bin/python3
# -*- coding: utf-8 -*-


import typing
import pygame
import pygame.image
import pygame.event
import pygame.mouse


class Button:
    """Oyunun menüsü için tuş üretme sınıfı"""

    window: pygame.Surface
    image: pygame.Surface
    x: int
    y: int
    width: int
    height: int

    def __init__(self, window: pygame.Surface, image: pygame.Surface, pos: typing.List[int], size: typing.List[int]):
        self.window = window
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]

    def draw(self) -> None:
        """Ekrana çiz"""

        self.window.blit(self.image, (self.x, self.y))

    def is_clicked(self) -> bool:
        """
        Tuşun üzerine tıklanınca
        Bu metod, 'game.py' dosyasında event_handler() metodunun içindeki MOUSEBUTTONDOWN bölümünde çağırılmalı
        """

        mouse_pos: tuple = pygame.mouse.get_pos()

        if self.x <= mouse_pos[0] <= self.x + self.width and \
                self.y <= mouse_pos[1] <= self.y + self.height:
            return True
