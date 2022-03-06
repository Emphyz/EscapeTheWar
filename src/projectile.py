from ursina import *
from ursina.curve import *

class Vodka(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.model = 'cube'
        self.scale = (0.1, 0.2)
        self.origin = (8, -1.5)
        self.texture = 'vodka'
        self.color = color.white
        self.texture_scale = (1,1)
        self.nb_vodka=kwargs.get("nb_vodka")
        self.visible=False
        self.obstacle=kwargs.get("obstacle")
        self.position_lancer=kwargs.get("position_lancer")

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        if self.nb_vodka==0:
            self.visible=False

        if self.nb_vodka==1:
            self.visible=True

        if self.nb_vodka==2:
            self.texture_scale = (2,1)
            self.scale = (0.2, 0.2)
            self.origin = (2, 1)

        if self.nb_vodka==3:
            self.texture_scale = (3,1)
            self.scale = (0.3, 0.2)
            self.origin = (3, 1)

        if self.nb_vodka==4:
            self.texture_scale = (4,1)
            self.scale = (0.4, 0.2)
            self.origin = (4, 1)

        if self.nb_vodka==5:
            self.texture_scale = (5,1)
            self.scale = (0.5, 0.2)
            self.origin = (5, 1)

    def lancer(self, liste):
        self.nb_vodka-=1
        bouteille=Entity(model='cube', scale=(2,4), position=self.position_lancer,texture='vodka', visible=True)
        b=-11
        a=0
        for i in liste:
            if bouteille.intersects(i).hit:
                a+=1
        if a==0:
            b+=1
            bouteille.rotation(0,10,0)
            if b<0:
                bouteille.x+=0.5
                bouteille.y+=0.5
            elif b==0:
                bouteille.x+=1
            elif b>0:
                bouteille.x-=0.5
                bouteille.y-=0.5
        if a==1:
            bouteille.explosion = Entity(model=Circle(), scale=.5, color=color.white33, collider='cube',position=bouteille.position)
            bouteille.explosion.animate_scale(3, duration=.3, curve=linear)
            bouteille.explosion.fade_out(duration=.2)
            destroy(bouteille.explosion, 2.1)
            destroy(bouteille, 3)

    def input(self, key):
        if key == 'a':
            self.lancer(self.obstacle)