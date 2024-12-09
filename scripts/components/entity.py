import pygame as pg

class Entity(pg.sprite.Sprite):

    def __init__(self, img="", pos=pg.math.Vector2(0, 0), groups=[]):
        super().__init__(groups)

        self.image = pg.image.load(img)
        self.rect = self.image.get_rect(topleft = pos)

        self.frame = 0
        self.tick = 0
    
    def animation(self, speed=8, frames=3, path=""):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.image = pg.image.load(path+ str(self.frame) + ".png")

