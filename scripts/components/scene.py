import pygame as pg

from scripts.settings import *
from scripts.components.fade import Fade

class Scene:

    def __init__(self, display=None):
        
        self.display = display
        self.all_sprites = pg.sprite.Group()
        self.all_colision = pg.sprite.Group()
        self.active = True
        self.fade = Fade(speed=5, display=self.display)

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)
        self.fade.draw()

    def update(self):
        if not self.display: return
        self.all_sprites.update()







