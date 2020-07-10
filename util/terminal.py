import os
import platform


def clear() -> None:
    """Terminal ekranını temizler."""

    p: str = platform.system()

    if p == "Windows":
        os.system("cls")
    
    elif p == "Linux" or p == "Darwin":
        os.system("clear")
