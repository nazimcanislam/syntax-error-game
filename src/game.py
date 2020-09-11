#!/usr/bin/python3
# -*- coding: utf-8 -*-


import typing
import os
import sys
import pygame
import pygame.time
import pygame.display
import pygame.event
import pygame.font
import pygame.mixer
import pygame.draw
import pygame.mouse

from src import others
from src.player import Player
from src.enemy import Enemy
from src.button import Button


# Araçları çalıştır!
pygame.init()
pygame.mixer.init()
pygame.font.init()


class Game:
    """Pygame oyunu yapmak için bir sınıf"""

    max_fps: int
    level: int
    player_start_live: int
    enemy_count: int
    dodged: int

    clock: pygame.time.Clock

    window: pygame.Surface
    game_image_surface: pygame.Surface
    button_play_surface: pygame.Surface
    button_exit_surface: pygame.Surface
    button_again_surface: pygame.Surface
    button_main_menu_surface: pygame.Surface
    button_resume_surface: pygame.Surface

    player: Player

    font: pygame.font.Font
    font2: pygame.font.Font
    font3: pygame.font.Font

    bg_music: pygame.mixer.Sound

    enemies: typing.List[Enemy]

    playing: bool
    menu: bool
    death_menu: bool
    pasue_menu: bool

    keys: tuple

    button_play: Button
    button_exit: Button
    button_again: Button
    button_main_menu: Button
    button_resume: Button

    def __init__(self, window: pygame.Surface, player: Player):
        """Oyunun inşaa etme metodu"""

        # Pygame'in kendi Clock() sınıfından bir obje oluştur.
        self.clock = pygame.time.Clock()  # Pygame Clock sınıfı
        self.max_fps = 60

        # Pencereyi oluştur.
        self.window = window
        self.window.set_alpha(None)
        pygame.event.set_allowed(
            [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])

        self.player = player
        self.player_start_live = self.player.live

        self.font = pygame.font.SysFont('Helvetica', 30, True)
        self.font2 = pygame.font.SysFont('Arial', 64, True)
        self.font3 = pygame.font.SysFont('Arial', 20, True)

        self.bg_music = pygame.mixer.Sound(
            f'{os.getcwd()}/assets/bg_music.wav')

        self.init_menu_components()

    def init_menu_components(self) -> None:
        """Menü elemanlarını oluştur"""

        self.game_image_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/game_image.png').convert_alpha(), (450, 193))

        self.button_play_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/button_play.png').convert_alpha(), (250, 100))
        self.button_play = Button(
            self.window,
            self.button_play_surface,
            [
                self.window.get_width() // 2 - self.button_play_surface.get_width() // 2,
                100 + self.game_image_surface.get_height() + 50,
            ],
            [
                self.button_play_surface.get_width(),
                self.button_play_surface.get_height(),
            ],
        )

        self.button_exit_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/button_exit.png').convert_alpha(), (250, 100))
        self.button_exit = Button(
            self.window,
            self.button_exit_surface,
            [
                self.window.get_width() // 2 - self.button_exit_surface.get_width() // 2,
                100 + self.game_image_surface.get_height() + 50 +
                self.button_play_surface.get_height() + 10,
            ],
            [
                self.button_exit_surface.get_width(),
                self.button_exit_surface.get_height(),
            ],
        )

        self.button_again_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/button_again.png').convert_alpha(), (250, 100))
        self.button_again = Button(
            self.window,
            self.button_again_surface,
            [
                self.window.get_width() // 2 - self.button_again_surface.get_width() // 2,
                self.window.get_height() // 2 - self.button_again_surface.get_height() // 2,
            ],
            [
                self.button_again_surface.get_width(),
                self.button_again_surface.get_height(),
            ],
        )

        self.button_main_menu_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/button_main_menu.png').convert_alpha(), (250, 100))
        self.button_main_menu = Button(
            self.window,
            self.button_main_menu_surface,
            [
                self.window.get_width() // 2 - self.button_main_menu_surface.get_width() // 2,
                self.window.get_height() // 2 - self.button_main_menu_surface.get_height() // 2 +
                self.button_again_surface.get_height() + 10,
            ],
            [
                self.button_main_menu_surface.get_width(),
                self.button_main_menu_surface.get_height(),
            ],
        )

        self.button_resume_surface = pygame.transform.smoothscale(pygame.image.load(
            'assets/button_resume.png').convert_alpha(), (250, 100))
        self.button_resume = Button(
            self.window,
            self.button_resume_surface,
            [
                self.window.get_width() // 2 - self.button_resume_surface.get_width() // 2,
                self.window.get_height() // 2 - self.button_resume_surface.get_height() // 2,
            ],
            [
                self.button_resume_surface.get_width(),
                self.button_resume_surface.get_height(),
            ],
        )

    def start(self) -> None:
        """Oyunu başlatın!"""

        self.bg_music.play(loops=-1)

        self.level = 1
        self.enemy_count = 3
        self.dodged = 0

        self.enemies = self.create_enemies()

        self.menu = True
        self.playing = False
        self.keys = tuple()

        self.menu_loop()

    def death_menu_loop(self) -> None:
        """Ölüm ekranı döngüsü"""

        self.bg_music.set_volume(0.5)
        pygame.mouse.set_visible(True)

        while self.death_menu:
            self.event_handler()
            self.window.fill(others.BACKGROUND_COLOR)

            dodged_text: pygame.Surface = self.font2.render(
                f'Toplam Kaçılan: {self.dodged}', True, others.BLACK)
            self.window.blit(
                dodged_text,
                (
                    self.window.get_width() // 2 - dodged_text.get_width() // 2,
                    self.window.get_height() // 2 - dodged_text.get_height() // 2 - 120,
                )
            )

            self.button_again.draw()
            self.button_main_menu.draw()

            self.redraw_window()

    def pasue_menu_loop(self) -> None:
        """Oyunun durdurma ekranı"""

        self.bg_music.set_volume(0.6)
        pygame.mouse.set_visible(True)

        while self.pasue_menu:
            self.event_handler()
            self.window.fill(others.BACKGROUND_COLOR)

            waiting_text: pygame.Surface = self.font2.render(
                'Seni burda bekliyorum!', True, others.BLACK)
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

    def menu_loop(self) -> None:
        """Menü döngüsü"""

        self.bg_music.set_volume(0.5)
        pygame.mouse.set_visible(True)

        while self.menu:
            self.event_handler()

            # Arka planı boya
            self.window.fill(others.BACKGROUND_COLOR)

            self.window.blit(self.game_image_surface, (self.window.get_width(
            ) // 2 - self.game_image_surface.get_width() // 2, 100))

            self.button_play.draw()
            self.button_exit.draw()

            self.redraw_window()

    def game_loop(self) -> None:
        """Oyun döngüsü"""

        self.bg_music.set_volume(1.0)
        pygame.mouse.set_visible(False)

        # Oyunun döngüsü burada :)
        while self.playing:
            self.event_handler()

            self.keys = pygame.key.get_pressed()
            self.player.move(self.keys)

            # Arka planı boya
            self.window.fill(others.BACKGROUND_COLOR)

            # Karakteri yükle
            self.player.draw()
            self.player.show_name()

            for e in self.enemies:
                if e.is_outsided():
                    self.enemies.remove(e)
                    self.dodged += 1

                    if self.dodged % 50 == 0:
                        self.player.live += 5

                    if len(self.enemies) == 0:
                        self.level += 1
                        self.enemy_count += self.level
                        self.enemies = self.create_enemies()
                elif self.player.is_collied(e):
                    self.enemies.remove(e)
                    self.player.lost_live()

                    if len(self.enemies) == 0:
                        self.level += 1
                        self.enemy_count += self.level
                        self.enemies = self.create_enemies()
                        self.player.show_live()

                e.draw()

            self.level_text: pygame.Surface = self.font.render(
                f"Seviye: {self.level}", True, (0, 0, 0)).convert_alpha()
            self.window.blit(self.level_text, (self.window.get_width(
            ) - 10 - self.level_text.get_width(), 10))

            self.dodge_text: pygame.Surface = self.font.render(
                f"Kaçılan: {self.dodged}", True, (0, 0, 0)).convert_alpha()
            self.window.blit(self.dodge_text, (10, self.window.get_height(
            ) - 10 - self.dodge_text.get_height()))

            self.player.show_live()

            if self.player.live == 0:
                self.menu = False
                self.playing = False
                self.death_menu = True
                self.death_menu_loop()

            self.redraw_window()

    def redraw_window(self) -> None:
        """Ekranı tazeleyen metod"""

        # FPS değerini ekranda göster
        self.show_fps()

        # Ekranı tazele
        pygame.display.update()

        # FPS: 60 olarak ayarla.
        self.clock.tick(self.max_fps)

    def event_handler(self) -> None:
        """Eylemleri kontrol eden metod"""

        # Eylemleri ve olayları yakala ve onlara göre işlem yap.
        events: typing.List[pygame.event.Event] = pygame.event.get()
        for event in events:
            # Çıkış yapılmak isteniyor ise...
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu:
                    if self.button_play.is_clicked():
                        self.show_playing_screen()
                    elif self.button_exit.is_clicked():
                        pygame.quit()
                        sys.exit(0)
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

    def show_menu(self) -> None:
        """Menüyü göster"""

        self.menu = True
        self.playing = False
        self.death_menu = False
        self.reset_all()
        self.menu_loop()

    def show_playing_screen(self) -> None:
        """Oynanış ekranını göster"""

        self.menu = False
        self.pasue_menu = False
        self.death_menu = False
        self.playing = True
        self.game_loop()

    def show_pasue_menu(self) -> None:
        """Oyunu durdurma menüsünü göster"""

        self.menu = False
        self.death_menu = False
        self.playing = False
        self.pasue_menu = True
        self.pasue_menu_loop()

    def create_enemies(self) -> list:
        """Düşmanları getiren metod"""

        return [Enemy(self.level, self.window) for x in range(0, self.enemy_count, 1)]

    def show_fps(self) -> None:
        """Oyunun FPS değerini ekranda gösterir"""

        fps_text: pygame.Surface = self.font.render(
            f"FPS: {round(self.clock.get_fps())}", True, (0, 0, 0)).convert_alpha()
        self.window.blit(fps_text, (self.window.get_width(
        ) - fps_text.get_width() - 10, self.window.get_height() - fps_text.get_height() - 10))

    def quit(self) -> None:
        """Oyundan çıkma metodu"""

        pygame.quit()
        sys.exit(0)

    def reset_all(self) -> None:
        """Oyun değerlerini sıfırla"""

        self.player.live = self.player_start_live
        self.level = 1
        self.enemy_count: int = 3
        self.dodged = 0
        self.player.x = 30
        self.player.y = 80
        self.enemies = self.create_enemies()
