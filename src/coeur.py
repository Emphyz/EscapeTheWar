from ursina import *


class Coeur(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.model = 'quad'
        self.scale = (0.3, 0.1)
        self.origin = (2.4, -4.5)
        self.color = color.white
        self.texture_scale = (3, 1)
        self.s = kwargs.get("vie")
        self.vivant = True
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.mort()
        if self.s == 2:
            self.texture_scale = (2, 1)
            self.scale = (0.2, 0.1)
            self.origin = (3.85, -4.5)
        if self.s == 1:
            self.texture_scale = (1, 1)
            self.scale = (0.1, 0.1)
            self.origin = (8.2, -4.5)
        if self.s == 0:
            self.visible = False

    def mort(self):
        if self.vivant == False:
            self.s -= 1
            self.vivant = True
