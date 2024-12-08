import pygame, sys
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.button import Button

class GameOver(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = AnimatedBg("assets/menu/bg.png", [0, 0], [0, -HEIGHT], [self.all_sprites])
        self.title = Obj("assets/menu/gameover.png", [436, 166], [self.all_sprites])
        self.btn_play = Button(color="white", pos=(64, 520), text="Return", font_color=[51, 51, 51], call_back=self.play)
        self.btn_quit = Button(color="white", pos=(64, 600), text="Quit", font_color=[51, 51, 51], call_back=self.quit_game)
        
    def play(self):
        self.active = False
        
    def quit_game(self):
        pygame.quit()
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




