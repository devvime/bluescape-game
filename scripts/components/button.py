import pygame as pg

from scripts.settings import *
from scripts.components.text import Text

class Button:
    
    def __init__(self, color="white", hover_color=[55, 55, 55], pos=(0, 0), size=(250, 64), text="Button", font_size=40, font_color="black", call_back=None, display=None):
        
        self.display = display
        self.initial_color = color
        self.color = color
        self.hover_color = hover_color
        self.pos = pg.Vector2(pos)
        self.size = pg.Vector2(size)
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
        self.call_back = call_back
        
        self.text = text
        self.fonst_size = font_size
        self.font_color = font_color
        self.font_pos = [(self.pos.x + self.rect.width / 2), (self.pos.y + self.rect.height / 2)]
        self.text_render = Text("assets/fonts/airstrike.ttf", self.fonst_size, self.text, self.font_color, self.font_pos, display=self.display)
        
    def events(self, event):
        if event.type == pg.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
                self.text_render.update_text(self.text, self.initial_color)
            else:
                self.color = self.initial_color
                self.text_render.update_text(self.text, self.hover_color)
                
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.call_back()
                

    def draw(self):
        pg.draw.rect(self.display, self.color, self.rect)
        self.text_render.draw_center()