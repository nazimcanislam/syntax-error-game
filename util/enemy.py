import pygame
import os
import random


class Enemy:
    def __init__(self, level: int, window: pygame.Surface):
        self.level: int = level
        self.window: pygame.Surface = window

        self.marks: tuple = (";", "i++", "j++", "{", "}", "switch()", "do while", "implements", "foreach()", "public", "protected", "private", "void", "using", "namespace", "static", "final", "var")
        self.choice: int = random.randint(0, len(self.marks) - 1)
        self.current_mark: str = self.marks[self.choice]

        self.vel: int = random.uniform(1.2, 1.8)

        self.x: int = random.randint(self.window.get_width() + 100, 2500 + self.level * 100)
        self.y: int = random.randint(50, self.window.get_height() - 100)

        """
        self.font: pygame.font.Font = pygame.font.SysFont("Times", 48)
        self.text: pygame.Surface = self.font.render(self.current_mark, True, (0, 0, 0))
        """

        #self.label: Label = Label(self.current_mark, "Times", 48, (0, 0, 0))
        self.font1: pygame.font.Font = pygame.font.SysFont("Times", 48)

        self.display: pygame.Surface = self.font1.render(self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width: int = self.display.get_width()
        self.height: int = self.display.get_height()

    def draw(self) -> None:
        """Düşmanın kendisini ekrana çizen metod"""

        self.display = self.font1.render(self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width = self.display.get_width()
        self.height = self.display.get_height()

        self.window.blit(self.display, (self.x, self.y))
        
        self.x -= self.vel

    def is_outsided(self) -> bool:
        """Düşman sol tarafntan yani ekrandan çıktı mı?"""

        return self.x <= -50
