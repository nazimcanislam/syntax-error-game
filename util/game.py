import pygame
import os

from .player import Player
from .enemy import Enemy


# Araçları çalıştır!
pygame.init()


class Game:
	"""Pygame oyunu yapmak için bir sınıf"""

	def __init__(self, player_name: str):
		"""Oyunun inşaa etme metodu"""

		self.player_name: str = player_name

		# Ekranı ortala
		os.environ['SDL_VIDEO_CENTERED'] = '1'

		# Renkler!
		self.black: tuple = (0, 0, 0)
		self.white: tuple = (255, 255, 255)
		self.red: tuple = (255, 0, 0)
		self.green: tuple = (0, 255, 0)

		# Oyunun genişlik, yükleklik ve başlığını tanımla.
		self.width: int = 1280
		self.height: int = 720
		self.title: str = "Yazım Hatası"

		# Pygame'in kendi Clock() sınıfından bir obje oluştur.
		self.clock: pygame.time.Clock = pygame.time.Clock()  # Pygame Clock sınıfı
		self.max_fps: int = 144

		# Pencereyi oluştur.
		self.window: pygame.Surface = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.title)

		self.favicon_image: pygame.Surface = pygame.image.load(os.path.join("assets", "favicon.png")).convert_alpha()
		pygame.display.set_icon(pygame.transform.scale(self.favicon_image, (128, 128)))

		self.window.set_alpha(None)

		self.player: Player = Player(self.player_name, 10, self.window)

		self.run()

	def run(self) -> None:
		"""Oyunu başlatın!"""

		self.font: pygame.font.Font = pygame.font.SysFont("Helvetica", 30, True)

		self.bg_music: pygame.mixer.Sound = pygame.mixer.Sound(f"{os.getcwd()}/assets/bg_music.wav")
		self.bg_music.play(loops=-1)

		self.level: int = 1
		self.enemy_count: int = 3
		self.dodged: int = 0

		self.enemies: list = self.create_enemies()

		pygame.event.set_allowed([pygame.QUIT])

		self.running: bool = True
		self.keys: tuple = tuple()

		# Oyunun döngüsü burada :)
		while self.running:

			# FPS: 60 olarak ayarla.
			self.clock.tick(self.max_fps)

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
			self.window.fill((240, 240, 240))

				# Karakteri yükle
			self.player.draw()
			self.player.show_name()

			for e in self.enemies:
				e: Enemy = e

				if e.is_outsided():
					self.enemies.remove(e)
					self.dodged += 1

					if self.dodged % 25 == 0:
						self.player.live += 1

					if len(self.enemies) == 0:
						self.level += 1
						self.enemy_count += self.level

						self.enemies = self.create_enemies()

				if self.player.is_collied(e):
					self.enemies.remove(e)
					self.player.lost_live()

					if len(self.enemies) == 0:
						self.level += 1
						self.enemy_count += self.level

						self.enemies = self.create_enemies()

						self.player.show_live(self.window)
						
				e.draw()

			self.player.show_live()

			self.level_text: pygame.Surface = self.font.render(f"Seviye: {self.level}", True, (0, 0, 0)).convert_alpha()
			self.window.blit(self.level_text, (self.window.get_width() - 10 - self.level_text.get_width(), 10))

			self.dodge_text: pygame.Surface = self.font.render(f"Kaçılan: {self.dodged}", True, (0, 0, 0)).convert_alpha()
			self.window.blit(self.dodge_text, (10, self.window.get_height() - 10 - self.dodge_text.get_height()))

			self.show_fps()

			# Ekranı tazele
			pygame.display.update()

	def create_enemies(self) -> list:
		"""Düşmanları getiren metod"""

		return [Enemy(self.level, self.window) for x in range(0, self.enemy_count, 1)]

	def show_fps(self) -> None:
		"""Oyunun FPS değerini ekranda gösterir"""

		fps_text: pygame.Surface = self.font.render(f"FPS: {round(self.clock.get_fps())}", True, (0, 0, 0)).convert_alpha()
		self.window.blit(fps_text, (self.window.get_width() - fps_text.get_width() - 10, self.window.get_height() - fps_text.get_height() - 10))