# Yazım Hatası Oyunu

---

Python'ın Pygame modülünü kullanarak yaptığım küçük bir oyun.

### Oyun İçi Görünüm
![Oyun içi görünüm](assets/intro.png)

### Oyunun Amacı
Normalde Python'da mevcut olmayan anahtar kelimeler, operatör vesaire şeylerden sıyrılmalısınız (dodge). :D

Oyun **yön tuşları** ve **WASD** ile oynanır.

Her 25 hatadan kaçtığınızda ekstra 1 can kazanırsınız.

### Kendi Adımı Yazmak İstiyorum?
Bunun için `app.py` adlı dosyanın içindeki `name` değişkenini değiştiriniz.

>app.py
```python
import sys

from util import terminal
from util.game import Game
from util.player import Player


def main(*args: list, **kwargs: dict) -> None:
    """Oyunun ana kalkış noktası"""

    # Ekranı temizle.
    terminal.clear()

    name: str = "Python"

    # Oyun objesi oluştur. Bu sayede oyun başlayacak.
    game: Game = Game(name)


# Oyunu başlat!
if __name__ == "__main__":
    main(sys.argv)

```

### Gerekli Python Versiyonu ve Kütüphaneleri
* Python==3.8.2
* Pygame==1.9.6

### Oyunu Çalıştır

**Windows** kullanıcıları bu yolu seçecek.
```bath
python app.py
```

**Linux** veya **MacOS** kullananlar ise bunu...
```bath
python3 app.py
```
