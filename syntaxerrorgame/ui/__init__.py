#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import os.path
import pygame
import pygame.transform
import pygame.image
import pygame.font

from syntaxerrorgame.ui.button import Button


pygame.font.init()

ENEMY_FONT = pygame.font.SysFont('Times New Roman', 48)

FONT18 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 18)
FONT32 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 32)
FONT64 = pygame.font.Font(os.path.join('assets', 'fonts/VT323-Regular.ttf'), 64)


def show_fps(game):
    """
    This method shows FPS value on window
    :param: game: syntaxerrorgame/game.py/Game
    """

    fps_text = FONT32.render(f'FPS: {round(game.clock.get_fps())}', True, game.data['colors']['black']).convert_alpha()
    game.window.blit(fps_text, (game.window.get_width() - fps_text.get_width() - 10, 10))


def init_menu_components(game):
    """
    Build menu components
    :param: game: syntaxerrorgame/game.py/Game
    """

    game.game_image_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/game_image.png')).convert_alpha(), (450, 193))

    game.button_play_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/button_play.png')).convert_alpha(), (250, 100))
    game.button_play = Button(
        game.window,
        game.button_play_surface,
        [
            game.window.get_width() // 2 - game.button_play_surface.get_width() // 2,
            100 + game.game_image_surface.get_height() + 50,
        ],
        [
            game.button_play_surface.get_width(),
            game.button_play_surface.get_height(),
        ],
    )

    game.button_exit_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/button_exit.png')).convert_alpha(), (250, 100))
    game.button_exit = Button(
        game.window,
        game.button_exit_surface,
        [
            game.window.get_width() // 2 - game.button_exit_surface.get_width() // 2,
            100 + game.game_image_surface.get_height() + 50 +
            game.button_play_surface.get_height() + 10,
        ],
        [
            game.button_exit_surface.get_width(),
            game.button_exit_surface.get_height(),
        ],
    )

    game.button_again_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/button_again.png')).convert_alpha(), (250, 100))
    game.button_again = Button(
        game.window,
        game.button_again_surface,
        [
            game.window.get_width() // 2 - game.button_again_surface.get_width() // 2,
            game.window.get_height() // 2 - game.button_again_surface.get_height() // 2,
        ],
        [
            game.button_again_surface.get_width(),
            game.button_again_surface.get_height(),
        ],
    )

    game.button_main_menu_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/button_main_menu.png')).convert_alpha(), (250, 100))
    game.button_main_menu = Button(
        game.window,
        game.button_main_menu_surface,
        [
            game.window.get_width() // 2 - game.button_main_menu_surface.get_width() // 2,
            game.window.get_height() // 2 - game.button_main_menu_surface.get_height() // 2 +
            game.button_again_surface.get_height() + 10,
        ],
        [
            game.button_main_menu_surface.get_width(),
            game.button_main_menu_surface.get_height(),
        ],
    )

    game.button_resume_surface = pygame.transform.smoothscale(pygame.image.load(os.path.join('assets', 'images/button_resume.png')).convert_alpha(), (250, 100))
    game.button_resume = Button(
        game.window,
        game.button_resume_surface,
        [
            game.window.get_width() // 2 - game.button_resume_surface.get_width() // 2,
            game.window.get_height() // 2 - game.button_resume_surface.get_height() // 2,
        ],
        [
            game.button_resume_surface.get_width(),
            game.button_resume_surface.get_height(),
        ],
    )
