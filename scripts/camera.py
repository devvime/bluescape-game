import pygame as pg
from scripts.settings import *

class Camera(pg.sprite.Group):

    def __init__(self):
        super().__init__()
        
        self.display = pg.display.get_surface()
        self.offset = pg.math.Vector2()
        
    def render(self, player):
        
        self.offset.x = player.rect.centerx - WIDTH / 2
        self.offset.y = player.rect.centery - HEIGHT / 2
        
        for sprite in self.sprites():
            off_rect = sprite.rect.copy()
            off_rect.center -= self.offset
            self.display.blit(sprite.image, off_rect)