#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame

from src.game import Game
from src.player import Player
from src.window import MyWindow
from src.constants import WIDTH, HEIGHT, FULLMODE


def main(*args, **kwargs):
    """Oyunun ana kalkış noktası"""

    # Pencereyi olutşru
    window = MyWindow((WIDTH, HEIGHT), 'Yazım Hatası', FULLMODE).get()

    # Oyuncuyu oluştur
    player = Player('Python', 10, window)

    # Oyun objesi oluştur
    game = Game(window, player)
    game.start()
