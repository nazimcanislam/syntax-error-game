from .player import Player
from .enemy import Enemy


class Collision:
    def __init__(self, player: Player):
        self.player: Player = player

    def is_collied(self, enemy: Enemy) -> bool:
        """Karakter ile rakiplerin çarpışmasını kontrol eden metod"""
        
        # Teşekkürler!
        # https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
        if (self.player.x < enemy.x + enemy.width) and \
                (self.player.x + self.player.width > enemy.x) and \
                    (self.player.y < enemy.y + enemy.height) and \
                        (self.player.y + self.player.height > enemy.y):
                        return True
