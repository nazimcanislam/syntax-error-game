#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pygame

from util import others
from util.game import Game
from util.player import Player
from util.window import MyWindow


def main(*args: list, **kwargs: dict) -> None:
    """Oyunun ana kalkış noktası"""

    # Ekranı temizle
    others.clear_terminal()

    # Pencereyi olutşru
    window: pygame.Surface = MyWindow((1280, 720), 'Yazım Hatası', False).get()

    # Oyuncuyu oluştur
    player: Player = Player('Python', 10, window)

    # Oyun objesi oluştur
    game: Game = Game(window, player)
    game.start()


# Oyunu başlat!
if __name__ == '__main__':
    main(sys.argv)
