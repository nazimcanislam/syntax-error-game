import pygame
import os
import random


class Enemy:
    def __init__(self, level: int, window: pygame.Surface):
        self.level: int = level
        self.window: pygame.Surface = window
        self.names: tuple = ("Noktalı Virgül", "i Artı Artı", "Küme Açılış", "Küme Kapanış", "Switch Koşulu", "Bir Çeşit Döngü", "Java'nın Şeyi", "Dizi Döngüsü")
        self.marks: tuple = (";", "i++", "{", "}", "switch()", "do while", "implements", "foreach()")

        self.choice: int = random.randint(0, len(self.names) - 1)
        self.current_name: str = self.names[self.choice]
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
        self.font2: pygame.font.Font = pygame.font.SysFont("Helvetica", 18)

        self.display: pygame.Surface = self.font1.render(self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width: int = self.display.get_width()
        self.height: int = self.display.get_height()

    def draw(self) -> None:
        """Düşmanın kendisini ekrana çizen metod"""

        self.display = self.font1.render(self.current_mark, True, (0, 0, 0)).convert_alpha()

        self.width = self.display.get_width()
        self.height = self.display.get_height()

        self.window.blit(self.display, (self.x, self.y))
        
        self.move()

    def move(self) -> None:
        """Düşmanın hareketini sağlayan metod"""

        self.x -= self.vel

    def is_outsided(self) -> bool:
        """Düşman sol tarafntan yani ekrandan çıktı mı?"""

        return self.x <= -50
    
    def show_name(self) -> None:
        """Düşmanın ismini kafasında gösteren metod"""

        text: pygame.Surface = self.font2.render(self.current_name, True, (0, 0, 0)).convert_alpha()

        self.window.blit(
            text,
            (
                self.x + text.get_width() // 2 - self.display.get_width() // 2,
                self.y - text.get_height() // 2 + self.display.get_height()
            )
        )
