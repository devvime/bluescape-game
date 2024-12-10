import pygame as pg
import sys

from scripts.settings import *
from scripts.entities.animatedbg import AnimatedBg
from scripts.components.entity import Entity
from scripts.components.scene import Scene
from scripts.components.text import Text
from scripts.components.button import Button

class GameOver(Scene):

    def __init__(self, scene_manager, display=None):
        super().__init__(display)
        
        self.scene_manager = scene_manager
        self.bg = AnimatedBg("assets/menu/bg.png", [0, 0], [0, -HEIGHT], [self.all_sprites])
        self.title = Entity("assets/menu/gameover.png", [436, 166], [self.all_sprites])
        self.btn_play = Button(color="white", pos=(64, 520), text="Return", font_color=[51, 51, 51], call_back=self.play, display=self.display)
        self.btn_quit = Button(color="white", pos=(64, 600), text="Quit", font_color=[51, 51, 51], call_back=self.quit_game, display=self.display)
        
    def play(self):
        self.scene_manager.set_scene("menu")
        
    def quit_game(self):
        pg.quit()
        sys.exit()
    
    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()




