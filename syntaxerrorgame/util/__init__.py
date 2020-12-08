#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path


def save_high_score(game):
	"""
	This method saves the high player score if current high score bigger than old one
	:param: game: syntaxerrorgame/game.py/Game
	"""

	with open(file=os.path.join('gamedata', 'player.json'), mode='r', encoding='utf-8') as file:
		content = json.load(file)

	if game.high_score > content['highScore']:
		content['highScore'] = game.high_score

	with open(file=os.path.join('gamedata', 'player.json'), mode='w', encoding='utf-8') as file:
		json.dump(content, file, indent=4)
