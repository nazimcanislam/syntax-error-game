#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import platform


# Renkler!
BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)
RED: tuple = (255, 0, 0)
GREEN: tuple = (0, 255, 0)
BACKGROUND_COLOR: tuple = (240, 240, 240)


def clear_terminal() -> None:
    """Terminal ekranını temizler."""

    p: str = platform.system()

    if p.lower().startswith("windows"):
        os.system("cls")

    else:
        os.system("clear")
