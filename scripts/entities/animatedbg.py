import pygame

from scripts.components.entity import Entity
from scripts.settings import HEIGHT

class AnimatedBg:

    def __init__(self, img, pos1, pos2, group):
        self.bg = Entity(img, pos1, group)
        self.bg2 = Entity(img, pos2, group)
    
    def update(self):

        self.bg.rect.y += 1
        self.bg2.rect.y += 1

        if self.bg.rect.y > HEIGHT:
            self.bg.rect.y = 0
        elif self.bg2.rect.y == 0:
            self.bg2.rect.y = -HEIGHT