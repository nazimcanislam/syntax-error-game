import pygame
import os
import random
import termcolor

from .label import Label


class Player:
    def __init__(self, name: str, live: int, window: pygame.Surface):
        self.name: str = name.strip()
        self.width: int = 50
        self.height: int = 50
        self.live: int = live

        self.x: int = 30
        self.y: int = 80
        self.vel: int = 3

        try:
            self.image_path: str = os.path.join("assets", "player.png")
            self.image: pygame.Surface = pygame.image.load(self.image_path)
            self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

        except pygame.error:
            print(termcolor.colored("HATA: Karakter resmi bulunamadı!", "red"))
            print(termcolor.colored(f"İPUCU: Lütfen assets klasöründeki 'player.png' resmin olduğundan emin olun veya '{os.path.basename(__file__)}'' dosyasını kontrol edin...", "yellow"))
            quit()
        
        except Exception:
            print(termcolor.colored("HATA: Bilinmeyen bir hata meydana geldi!", "red"))

        self.black: tuple = (0, 0, 0)

        self.limits: dict = {
            "left": 10,
            "top": 50,
            "right": window.get_width() - 10 - self.width,
            "bottom": window.get_height() - 50
        }

    def move(self, keys: tuple) -> None:
        """Karakterin hareketini sağlayan metod"""

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > self.limits["left"]:
            self.x -= self.vel
        
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > self.limits["top"]:
            self.y -= self.vel

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < self.limits["right"]:
            self.x += self.vel
        
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.y + self.height) < self.limits["bottom"]:
            self.y += self.vel
    
    def show_name(self, window: pygame.Surface) -> None:
        """Karakterin ismini üstünde gösteren metod"""

        self.showen_name: Label = Label(self.name, "Helvatica", 18, self.black)

        # Burada; karakterin ismi, karakter resminin üzerinde durmasını sağladım. Biraz zor oldu ama neyse :P
        
        self.showen_name.print(
            window=window,
            position=(
                self.x + self.width // 2 - self.showen_name.text_width() // 2,
                self.y - self.height // 2 + self.showen_name.text_height() // 2
            )
        )
    
    def show_live(self, window: pygame.Surface) -> None:
        """Karakterin canını gösteren metod"""

        self.live_label: Label = Label(f"Can: {self.live}", "Helvatica", 32, self.black)

        self.live_label.print(window, (10, 10))

    def draw(self, window: pygame.Surface) -> None:
        """Karakteri yükleyen metod"""

        window.blit(self.image, (self.x, self.y)) 
        self.show_name(window)
    
    def lost_live(self, value: int = 1) -> None:
        """Karakterin can kaybetme metodu"""

        if self.live > 0:
            self.live -= value
