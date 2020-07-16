import os
import platform


def clear() -> None:
    """Terminal ekranını temizler."""

    p: str = platform.system()

    if p.lower().startswith("windows"):
        os.system("cls")
    
    else:
        os.system("clear")
