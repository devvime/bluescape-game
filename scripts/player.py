import pygame as pg

from scripts.obj import Obj

class Player(pg.sprite.Sprite):
    
    def __init__(self, pos=pg.math.Vector2(0, 0), groups=None):
        super().__init__(groups)
        
        self.pos = pos
        self.image = pg.image.load("assets/player/idle_1.png")
        self.rect = self.image.get_rect(topleft=pos)
        
        self.speed = 2
        self.direction = pg.math.Vector2()
        
    def input(self):
        key = pg.key.get_pressed()
        
        if key[pg.K_a]:
            self.direction.x = -self.speed
        elif key[pg.K_d]:
            self.direction.x = self.speed
        else:
            self.direction.x = 0
            
    def move(self):
        self.rect.x += self.direction.x * self.speed
        
    def update(self):
        self.input()
        self.move()