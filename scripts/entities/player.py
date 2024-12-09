import pygame as pg

from scripts.components.entity import Entity

class Player(pg.sprite.Sprite):
    
    def __init__(self, pos=pg.math.Vector2(0, 0), groups=None, collision_group=None):
        super().__init__(groups)
        
        self.tick = 0
        self.frame = 0
        self.pos = pos
        self.image = pg.image.load("assets/player/idle_1.png")
        self.rect = self.image.get_rect(topleft=pos)
        
        self.speed = 2
        self.direction = pg.math.Vector2()
        self.gravity = 0.8
        self.jump_force = 18
        self.on_ground = False
        self.flip = False
        
        self.collision_group = collision_group
        
    def input(self):
        key = pg.key.get_pressed()
        
        if key[pg.K_a]:
            self.animation(speed=8, frames=3, path="assets/player/walk_")
            self.direction.x = -self.speed
            self.flip = True
        elif key[pg.K_d]:
            self.animation(speed=8, frames=3, path="assets/player/walk_")
            self.direction.x = self.speed
            self.flip = False
        else:
            self.animation(speed=16, frames=2, path="assets/player/idle_")
            self.direction.x = 0
            
        if key[pg.K_SPACE] and self.on_ground:
            self.direction.y = -self.jump_force
            self.on_ground = False
            
    def move(self):
        self.rect.x += self.direction.x * self.speed
        
        if not self.on_ground:
            self.image = pg.image.load("assets/player/jump.png")
            self.image = pg.transform.flip(self.image, self.flip, False)
        
    def gravity_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def y_collision(self):
        for sprite in self.collision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.direction.y = 0
                    self.rect.bottom = sprite.rect.top
                    self.on_ground = True
                
                if self.direction.y < 0:
                    self.direction.y = 0
                    self.rect.top = sprite.rect.bottom
    
    def x_collision(self):
        for sprite in self.collision_group:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    
    def animation(self, speed=8, frames=3, path=""):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.image = pg.image.load(path+ str(self.frame) + ".png")
            self.image = pg.transform.flip(self.image, self.flip, False)
        
    def update(self):
        self.input()
        self.move()
        self.x_collision()
        self.gravity_force()
        self.y_collision()