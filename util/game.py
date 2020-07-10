import pygame
import os

from .player import Player
from .enemy import Enemy
from .sound import Sound
from .label import Label
from .collision import Collision


# Araçları çalıştır!
pygame.init()


class Game:
    """Pygame oyunu yapmak için bir sınıf"""

    def __init__(self, player_name: str):
        """Oyunun inşaa etme metodu"""

        self.player_name: str = player_name

        # Ekranı ortala
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        os.environ["SDL_VIDEO_WINDOW_POS"] = "{0}, {1}".format(500, 100)

        # Renkler!
        self.black: tuple = (0, 0, 0)
        self.white: tuple = (255, 255, 255)
        self.red: tuple = (255, 0, 0)
        self.green: tuple = (0, 255, 0)

        # Oyunun genişlik, yükleklik ve başlığını tanımla.
        self.width: int = 1200
        self.height: int = 800
        self.title: str = "Yazım Hatası"

        self.favicon_image: pygame.Surface = pygame.image.load(
            os.path.join("assets", "favicon.png")
        )

        # Pygame'in kendi Clock() sınıfından bir obje oluştur.
        self.clock: pygame.time.Clock = pygame.time.Clock()  # Pygame Clock sınıfı
        self.fps: int = 60

        # Pencereyi oluştur.
        self.screen: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(pygame.transform.smoothscale(self.favicon_image, (128, 128)))

        self.player: Player = Player(self.player_name, 10, self.screen)
        self.collision: Collision = Collision(self.player)

        self.run()

    def run(self) -> None:
        """Oyunu başlatın!"""

        self.running: bool = True
        self.keys: tuple = tuple()

        self.bg_color: tuple = (240, 240, 240)
        self.bg_music: Sound = Sound("assets", "bg_music.wav")
        self.bg_music.play_and_repeat()

        self.level: int = 1
        self.enemy_count: int = 3
        self.dodged: int = 0

        
        self.enemies: list = self.create_enemies()

        # Oyunun döngüsü burada :)
        while self.running:

            # FPS: 60 olarak ayarla.
            self.clock.tick(self.fps)

            # Eylemleri ve olayları yakala ve onlara göre işlem yap.
            for event in pygame.event.get():
                event: pygame.event.EventType = event
                
                # Çıkış yapılmak isteniyor ise...
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()

            self.keys = pygame.key.get_pressed()
            
            self.player.move(self.keys)

            # Arka planı boya
            self.screen.fill(self.bg_color)

            # Karakteri yükle
            self.player.draw(self.screen)

            for e in self.enemies:
                e: Enemy = e

                if e.is_outsided():
                    self.enemies.remove(e)
                    self.dodged += 1

                    if self.dodged % 25 == 0:
                        self.player.live += 1

                e.draw(self.screen)

                if self.collision.is_collied(e):
                    self.enemies.remove(e)
                    self.player.lost_live()
                
                if len(self.enemies) == 0:
                    self.level += 1
                    self.enemy_count += self.level

                    self.enemies = self.create_enemies()
            
            self.player.show_live(self.screen)

            # Labellar
            self.label1: Label = Label(f"Seviye: {self.level}", "Helvatica", 32, self.black)
            self.label1.print(self.screen, (self.screen.get_width() - 10 - self.label1.text_width(), 10))
            self.dodge_label: Label = Label(f"Kaçılan: {self.dodged}", "Helvatica", 32, self.black)
            self.dodge_label.print(self.screen, (10, self.screen.get_height() - 10 - self.dodge_label.text_height()))
            self.show_fps()

            # Ekranı tazele
            pygame.display.update()
    
    def create_enemies(self) -> list:
        """Düşmanları getiren metod"""

        return [Enemy(self.level, self.screen) for x in range(0, self.enemy_count, 1)]

    def show_fps(self) -> None:
        """Oyunun FPS değerini ekranda gösterir"""

        self.fps_label: Label = Label(
            f"FPS: {int(self.clock.get_fps())}",
            "Helvatica",
            32,
            (self.red if self.clock.get_fps() <= 25 else self.green)
        )
        
        self.fps_label.print(
            self.screen,
            (
                self.screen.get_width() - 10 - self.fps_label.text_width(),
                self.screen.get_height() - 10 - self.fps_label.text_height()
            )
        )
