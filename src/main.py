#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame

from src import others
from src.game import Game
from src.player import Player
from src.window import MyWindow


def main(*args: list, **kwargs: dict) -> None:
    """Oyunun ana kalkış noktası"""

    # Ekranı temizle
    others.clear_terminal()

    # Pencereyi olutşru
    window: pygame.Surface = MyWindow((1920, 1080), 'Yazım Hatası', True).get()

    # Oyuncuyu oluştur
    player: Player = Player('Python', 10, window)

    # Oyun objesi oluştur
    game: Game = Game(window, player)
    game.start()
