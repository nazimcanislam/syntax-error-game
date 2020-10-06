#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import pygame.mixer
import pygame.font

from syntaxerrorgame.window import Window
from syntaxerrorgame.game import Game
from syntaxerrorgame.player import Player
from syntaxerrorgame.constants import WIDTH, HEIGHT, FULLMODE


def play():
	"""
	Oyunu oynamak için bu fonksiyonu çağır ve keyfine bak :)
	Yani tabii, bu oyun öyle o kadar zevkli değildir, henüz...
	"""

<<<<<<< HEAD
=======
	# Araçları çalıştır!
>>>>>>> 1d360683842047a60998f2e1014902d4cb1032a8
	pygame.init()
	pygame.mixer.init()
	pygame.font.init()

	# Pencereyi oluştur
	window = Window((WIDTH, HEIGHT), 'Yazım Hatası', FULLMODE).get()

	# Oyuncuyu oluştur
	player = Player('Python', 10, window)

	# Oyun objesi oluştur
	game = Game(window, player)
	game.start()
