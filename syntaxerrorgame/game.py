#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import os
import os.path
import sys
import pygame
import pygame.time
import pygame.display
import pygame.event
import pygame.font
import pygame.mixer
import pygame.draw
import pygame.mouse
import pygame.image
import pygame.transform

from syntaxerrorgame.entities.player import Player
from syntaxerrorgame.entities.enemy import Enemy
from syntaxerrorgame.ui import init_menu_components, show_fps, FONT32, FONT64
from syntaxerrorgame.ui.button import Button
from syntaxerrorgame.util import save_high_score


class Game:
    """
    Main game class
    """

    def __init__(self):
        super().__init__()

        with open(file=os.path.join('gamedata', 'data.json'), mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

        with open(file=os.path.join('gamedata', 'player.json'), mode='r', encoding='utf-8') as file:
            self.high_score = json.load(file)['highScore']

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        self.window = pygame.display.set_mode(
            (self.data['window']['width'], self.data['window']['height']),
            pygame.FULLSCREEN if self.data['window']['fullScreen'] else False,
        )
        pygame.display.set_caption(self.data['window']['title'])
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN])
        pygame.display.set_icon(
            pygame.transform.scale(
                pygame.image.load(os.path.join("assets", "images/favicon.png")),
                (128, 128)
            ).convert_alpha()
        )

        self.clock = pygame.time.Clock()
        self.max_fps = self.data['window']['fps']

        self.player = Player('Python', 10, self.window)
        self.player_start_live = self.player.live

        self.bg_music = pygame.mixer.Sound(os.path.join('assets', 'sounds/bg_music.wav'))

        init_menu_components(self)

    def start(self):
        """
        Just start the game!
        """

        self.bg_music.play(loops=-1)

        self.level = 1
        self.enemy_count = 3
        self.score = 0

        self.enemies = self.create_enemies()

        self.menu = True
        self.playing = False

        self.menu_loop()

    def death_menu_loop(self):
        """
        Shows death menu
        """

        self.bg_music.set_volume(0.5)
        pygame.mouse.set_visible(True)

        while self.death_menu:
            self.event_handler()
            self.window.fill(self.data['colors']['backgroundColor'])

            score_text = FONT64.render(f'Toplam Kaçılan: {self.score}', True, self.data['colors']['black'])
            self.window.blit(
                score_text,
                (
                    self.window.get_width() // 2 - score_text.get_width() // 2,
                    self.window.get_height() // 2 - score_text.get_height() // 2 - 120,
                )
            )

            self.button_again.draw()
            self.button_main_menu.draw()

            self.redraw_window()

    def pasue_menu_loop(self):
        """
        Shows pause menu
        """

        self.bg_music.set_volume(0.6)
        pygame.mouse.set_visible(True)

        while self.pasue_menu:
            self.event_handler()
            self.window.fill(self.data['colors']['backgroundColor'])

            waiting_text = FONT64.render('Seni burda bekliyorum!', True, self.data['colors']['black'])
            self.window.blit(
                waiting_text,
                (
                    self.window.get_width() // 2 - waiting_text.get_width() // 2,
                    self.window.get_height() // 2 - waiting_text.get_height() // 2 -
                    self.button_resume.image.get_height(),
                )
            )
            self.button_resume.draw()
            self.button_main_menu.draw()

            self.redraw_window()

    def menu_loop(self):
        """
        Shows main menu
        """

        self.bg_music.set_volume(0.5)
        pygame.mouse.set_visible(True)

        while self.menu:
            self.event_handler()

            self.window.fill(self.data['colors']['backgroundColor'])

            self.window.blit(
                self.game_image_surface,
                (self.window.get_width() // 2 - self.game_image_surface.get_width() // 2, 100)
            )

            self.button_play.draw()
            self.button_exit.draw()

            self.redraw_window()

    def game_loop(self):
        """
        Shows game
        """

        self.bg_music.set_volume(1.0)
        pygame.mouse.set_visible(False)

        while self.playing:
            self.event_handler()
            self.window.fill(self.data['colors']['backgroundColor'])

            self.player.draw()
            # self.player.draw_hitbox()
            self.player.show_name()

            for enemy in self.enemies:
                enemy.draw()
                # e.draw_hitbox()

                if enemy.is_outsided():
                    self.enemies.remove(enemy)
                    self.score += 1

                    if self.score > self.high_score:
                        self.high_score = self.score
                        if not self.playing:
                            pass

                    if self.score % 50 == 0:
                        self.player.live += 5

                    if len(self.enemies) == 0:
                        self.level += 1
                        self.enemy_count += self.level
                        self.enemies = self.create_enemies()
                elif enemy.rect.colliderect(self.player.rect):
                    self.enemies.remove(enemy)
                    self.player.lost_live()

                    if len(self.enemies) == 0:
                        self.level += 1
                        self.enemy_count += self.level
                        self.enemies = self.create_enemies()

            self.level_text = FONT32.render(f'Seviye: {self.level}', True, self.data['colors']['black']).convert_alpha()
            self.window.blit(self.level_text, (10, 10))

            self.live_label = FONT32.render(f"Can: {self.player.live}", True, self.data['colors']['black']).convert_alpha()
            self.window.blit(self.live_label, (10, self.level_text.get_rect().y + self.level_text.get_height() + 10))

            self.high_score_text = FONT32.render(f'En çok kaçılan: {self.high_score}', True, self.data['colors']['black']).convert_alpha()
            self.window.blit(self.high_score_text, (10, self.window.get_height() - self.high_score_text.get_height() - 10))

            self.score_text = FONT32.render(f'Kaçılan: {self.score}', True, self.data['colors']['black']).convert_alpha()
            self.window.blit(self.score_text, (10, self.window.get_height() - self.high_score_text.get_height() - self.high_score_text.get_height()))

            if self.player.live == 0:
                self.show_death_menu()

            self.redraw_window()

    def redraw_window(self) -> None:
        """
        This method redraws the window
        Call this method the bottom of any game loop
        """

        show_fps(self)
        pygame.display.update()
        self.clock.tick(self.max_fps)

    def event_handler(self) -> None:
        """
        This method listens to events and does anything we want!
        """

        for event in pygame.event.get():
            self.player.move(event)

            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu:
                    if self.button_play.is_clicked():
                        self.show_playing_screen()
                    elif self.button_exit.is_clicked():
                        self.quit()
                elif self.death_menu:
                    if self.button_again.is_clicked():
                        self.reset_all()
                        self.show_playing_screen()
                    elif self.button_main_menu.is_clicked():
                        self.show_menu()
                elif self.pasue_menu:
                    if self.button_resume.is_clicked():
                        self.show_playing_screen()
                    elif self.button_main_menu.is_clicked():
                        self.show_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.show_pasue_menu()
                    elif self.menu:
                        self.quit()
                    elif self.death_menu:
                        self.show_menu()
                    elif self.pasue_menu:
                        self.show_playing_screen()

    def show_menu(self):
        """
        Reset menu loop vars
        """

        self.menu = True
        self.playing = False
        self.death_menu = False
        self.reset_all()
        self.menu_loop()

    def show_playing_screen(self):
        """
        Reset game loop vars
        """

        self.menu = False
        self.pasue_menu = False
        self.death_menu = False
        self.playing = True
        self.game_loop()

    def show_pasue_menu(self):
        """
        Reset pasue loop vars
        """

        self.menu = False
        self.death_menu = False
        self.playing = False
        self.pasue_menu = True
        self.pasue_menu_loop()

    def show_death_menu(self):
        """
        Reset death loop vars
        """

        self.menu = False
        self.pasue_menu = False
        self.death_menu = True
        self.playing = False
        self.death_menu_loop()

    def create_enemies(self):
        """
        Construct all enemies by level and return them with List object
        :return: List[Enemy]
        """

        return [Enemy(self.level, self.window) for x in range(0, self.enemy_count, 1)]

    def quit(self):
        """
        Firstly, save high score then exit from game
        """

        save_high_score(self)
        pygame.quit()
        sys.exit(0)

    def reset_all(self):
        """
        This method reset game vars
        """

        self.player.live = self.player_start_live
        self.level = 1
        self.enemy_count: int = 3
        self.score = 0
        self.player.rect.x = 30
        self.player.rect.y = 80
        self.enemies = self.create_enemies()
