import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.tick = 0
        self.enemy_colision = pygame.sprite.Group()
        self.all_colision = pygame.sprite.Group()

        #self.music = pygame.mixer.Sound("file")
        #self.music.play(-1)

    def colision(self):
        pass

    def gameover(self):
        pass
                
    def update(self):
        self.colision()
        self.gameover()
        return super().update()
