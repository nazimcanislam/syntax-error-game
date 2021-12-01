#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pygame
import pygame.font


class Label:
    """
    Label text constructor for game ui
    """

    def __init__(self, text, font_name, size, color, is_sys_font=False, bold=False, italic=False, background=None):
        """
        :param: font_name: str
        :param: size: int
        :param: color: Tuple[int, int, int]
        :param: is_sys_font: bool
        """

        super().__init__()

        pygame.font.init()

        self.text = text
        self.font_name = font_name
        self.size = size
        self.color = color
        self.is_sys_font = is_sys_font
        
        if self.is_sys_font:
        	self.font = pygame.font.SysFont(self.font_name, self.size, bold, italic)
        else:
        	self.font = pygame.font.Font(self.font_name, self.size)

        self.surface = self.get(self.text)

    def get(self, text, background=None):
    	"""
    	:param: text: str
    	:param: background: str
    	:return: pygame.Surface
    	"""

    	return self.font.render(text, True, self.color, background).convert_alpha()

    def draw(self, surface, pos):
    	"""
    	:param: surface: pygame.Surface
    	:param: pos: Tuple[int, int]
    	"""

    	self.pos = pos
    	surface.blit(self.get(self.text), self.pos)
