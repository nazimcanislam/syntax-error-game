#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import pygame.mixer
import pygame.font

from syntaxerrorgame.game import Game


def play():
	"""
	Call this function to play game and enjot it :)
	I know, I know... This game isn't fun too much, yet...
	"""

	pygame.init()
	pygame.mixer.init()
	pygame.font.init()

	game = Game()
	game.start()
