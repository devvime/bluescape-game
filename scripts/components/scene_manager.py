from scripts.scenes import scenes

class SceneManager:
    
    def __init__(self, display=None):
        self.scene = None
        self.current_scene = None
        self.display = display
        
    def set_scene(self, scene):
        self.scene = scene
        self.current_scene = scenes[scene](self, display=self.display)
        
    def get_current_scene(self):
        return self.current_scene
        