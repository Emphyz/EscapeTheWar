from ursina import *
from entity import *
from bob_le_chef_dorchestre import *
from scene import *
from entity_2 import *

app = Ursina()

actual_scene = tutorial_scene

scene_afficher = Scene(bob(add_to_all_scene, tutorial_scene))
scene.entities = scene_afficher.get_entities()


def update():
    for i in Mortal:
        if add_to_all_scene.get("player").intersects(i).hit or add_to_all_scene.get("player").y <= -150:
            add_to_all_scene.get("player").vivant = False
            coeur.vivant = False
            add_to_all_scene.get("player").position = add_to_all_scene.get(
                "player").spawnpoint
    for i in vodka_a:
        if add_to_all_scene.get("player").intersects(i).hit:
            i.visible = False
            i.collider = False
            affichage_vodka.nb_vodka += 1
    if add_to_all_scene.get("player").vie == 0:
        scene_afficher = Scene(bob(add_to_all_scene, death_scene))
        scene.entities = scene_afficher.get_entities()


def input(key):
    if key == 'escape':
        mouse.visible = True
        mouse.locked = False
    if key == 'escape up':
        mouse.visible = False
        mouse.locked = True
    if key == 'a':
        scene.afficher = Scene(bob(add_to_all_scene, egout_scene))
        scene.entities = scene_afficher.get_entities()


camera.add_script(SmoothFollow(target=add_to_all_scene.get(
    "player"), offset=[0, 1, -30], speed=10))

window.fullscreen = True
camera.orthographic = True
camera.position = (0, 0)
camera.fov = 30

add_to_all_scene.get("player").position = add_to_all_scene.get(
    "player").spawnpoint

mouse.visible = False
mouse.locked = True

app.run()
