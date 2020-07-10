import pygame
import os
import random

from .label import Label


class Enemy:
    def __init__(self, level: int, window: pygame.Surface):
        self.level: int = level
        self.names: tuple = ("Noktalı Virgül", "i Artı Artı", "Küme Açılış", "Küme Kapanış", "Switch Koşulu", "Bir Çeşit Döngü", "Java'nın Şeyi", "Dizi Döngüsü")
        self.marks: tuple = (";", "i++", "{", "}", "switch()", "do while", "implements", "foreach()")

        self.choice: int = random.randint(0, len(self.names) - 1)
        self.current_name: str = self.names[self.choice]
        self.current_mark: str = self.marks[self.choice]

        self.vel: int = random.uniform(2.0, 3.0)

        self.x: int = random.randint(window.get_width() + 100, 2500 + self.level * 100)
        self.y: int = random.randint(50, window.get_height() - 50)

        """
        self.font: pygame.font.Font = pygame.font.SysFont("Times", 48)
        self.text: pygame.Surface = self.font.render(self.current_mark, True, (0, 0, 0))
        """

        self.label: Label = Label(self.current_mark, "Times", 48, (0, 0, 0))

        self.width: int = self.label.text_width()
        self.height: int = self.label.text_height()

    def draw(self, window: pygame.Surface) -> None:
        """Düşmanın kendisini ekrana çizen metod"""

        self.label.print(window, (self.x, self.y))
        self.show_name(window)
        
        self.move()

    def move(self) -> None:
        """Düşmanın hareketini sağlayan metod"""

        self.x -= self.vel

    def is_outsided(self) -> bool:
        """Düşman sol tarafntan yani ekrandan çıktı mı?"""

        return self.x <= -50
    
    def show_name(self, window: pygame.Surface) -> None:
        """Düşmanın ismini kafasında gösteren metod"""

        self.showen_name: Label = Label(self.current_name, "Helvatica", 18, (0, 0, 0))

        # Burada; karakterin ismi, karakter resminin üzerinde durmasını sağladım. Biraz zor oldu ama neyse :P
        
        self.showen_name.print(
            window=window,
            position=(
                self.x + self.label.text_width() // 2 - self.showen_name.text_width() // 2,
                self.y - self.label.text_height() // 2 + self.showen_name.text_height()
            )
        )
