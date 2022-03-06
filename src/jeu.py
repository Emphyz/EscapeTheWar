from ursina import *
from entity import *
from bob_le_chef_dorchestre import *
from scene import *

app = Ursina()

scene_afficher=Scene(scene2)

scene.entities=scene_afficher.get_entities()

def update():
    for i in Mortal:
        if player.intersects(i).hit or player.y <= -150:
            player.vivant = False
            coeur.vivant = False
            player.position = player.spawnpoint
    for i in vodka_a:
        if player.intersects(i).hit:
            i.visible = False
            i.collider = False
            affichage_vodka.nb_vodka += 1
    if player.vie == 0:
        item.visible = True


def input(key):
    if key == 'escape':
        mouse.visible = True
        mouse.locked = False
    if key == 'escape up':
        mouse.visible = False
        mouse.locked = True
    if key == 'a':
       bob(scene_afficher, scene3)

window.fullscreen = True
camera.orthographic = True
camera.position = (0, 0)
camera.fov = 30

player.position = player.spawnpoint

mouse.visible = False
mouse.locked = True

app.run()
