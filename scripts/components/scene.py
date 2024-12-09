import pygame as pg

from scripts.settings import *
from scripts.components.fade import Fade

class Scene:

    def __init__(self):
        
        self.display = pg.display.get_surface()
        self.all_sprites = pg.sprite.Group()
        self.all_colision = pg.sprite.Group()
        self.active = True
        self.fade = Fade(speed=5)

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)
        self.fade.draw()

    def update(self):
        self.all_sprites.update()







