import pygame


pygame.font.init()


class Label:
    def __init__(self, text: str, face: str, size: int, color: tuple):
        self.text: str = text
        self.face: str = pygame.font.SysFont(face, size)
        self.size: int = size
        self.color: tuple = color
        self.lbl: pygame.Surface = self.face.render(self.text, True, self.color)
    
    def print(self, window: pygame.Surface, position: tuple) -> None:
        
        self.position: tuple = position
        self.x: int = self.position[0]
        self.y: int = self.position[1]

        window.blit(self.lbl, (self.x, self.y))
    
    def text_width(self) -> float:
        n = self.lbl.get_width()
        return n

    def text_height(self) -> float:
        return self.lbl.get_height()
