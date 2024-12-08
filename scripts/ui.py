import pygame as pg

from scripts.obj import Obj

class Ui:
    
    def __init__(self):
        
        self.display = pg.display.get_surface()
        self.ui_group = pg.sprite.Group()
        
        self.life = 3
        
        self.hud1 = Obj("assets/player/idle_0.png", [0, 10], [self.ui_group])
        self.hud2 = Obj("assets/player/idle_0.png", [74, 10], [self.ui_group])
        self.hud3 = Obj("assets/player/idle_0.png", [144, 10], [self.ui_group])
        
    def count_lifes(self):
        if self.life == 2:
            self.hud3.kill()
        elif self.life == 1:
            self.hud2.kill()
        elif self.life == 0:
            self.hud1.kill()
        
    def draw(self):
        self.ui_group.draw(self.display)
        
    def update(self):
        self.count_lifes()