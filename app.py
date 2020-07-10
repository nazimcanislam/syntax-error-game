import sys

from util import terminal
from util.game import Game
from util.player import Player


def main(*args: list, **kwargs: dict) -> None:
    """Oyunun ana kalkış noktası"""

    # Ekranı temizle.
    terminal.clear()

    name: str = "Nazımcan"

    # Oyun objesi oluştur. Bu sayede oyun başlayacak.
    game: Game = Game(name)


# Oyunu başlat!
if __name__ == "__main__":
    main(sys.argv)
