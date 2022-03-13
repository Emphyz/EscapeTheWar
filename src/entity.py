from ursina import *
from projectile import *
from creation_personnage import *
from coeur import *
from scene import Scene
from functools import partial

asset_folder = '../asset/'

hub_scene = Scene(None)

tutorial_scene = Scene(None)

egout_scene = Scene(None)

foret_scene = Scene(None)

plaine_scene = Scene(None)

frontiere_scene = Scene(None)

# tuto scene

tutorial_scene.add_entity("ground", Entity(add_to_scene_entities=False, model='cube', collider='box', color=color.black, position=(
    0, 0), scale=(20, 4)))

# scene egout

egout_scene.add_entity("projectile", Vodka(add_to_scene_entities=False, model='cube', collider='box', color=color.white, position=(
    10, 0), texture=asset_folder + 'vodka', scale=(2, 4)))

egout_scene.add_entity("scie", Entity(add_to_scene_entities=False, model='cube', collider='box', color=color.white, position=(
    70, -25), texture=asset_folder + "scie", scale_x=2, scale_y=2))

egout_scene.add_entity("background_city", Entity(add_to_scene_entities=False, model='quad', collider=False, scale=(
    120, 60), position=(0, 23.5, 5), texture=asset_folder + 'city'))

egout_scene.add_entity("ground_s1", Entity(add_to_scene_entities=False, model='cube', scale=(70, 25), position=(
    0, -14.5), collider='box', color=color.black))

egout_scene.add_entity("ground_s2", Entity(add_to_scene_entities=False, model='cube', scale=(300, 14), position=(
    197.5, -8), collider='box', color=color.black))

egout_scene.add_entity("wallstart", Entity(add_to_scene_entities=False, model='cube', collider='box', scale=(
    5, 12), position=(-10, 4), color=color.black))

egout_scene.add_entity("wallstart2", Entity(add_to_scene_entities=False, model='cube', collider='box', scale=(
    5, 25), position=(50, -2), color=color.black))

egout_scene.add_entity("plaque_e1", Entity(add_to_scene_entities=False, model='cube', scale=(12.5, 1), position=(
    41.25, -3, -2), collider='box', color=color.gray))

egout_scene.add_entity("ground_e1", Entity(add_to_scene_entities=False, model='cube', scale=(100, 20), position=(
    50, -37), collider='box', color=color.black))

egout_scene.add_entity("ground_e_back1", Entity(add_to_scene_entities=False, model='cube', scale=(16, 49), position=(
    41.5, -22.5, 4), texture=asset_folder + 'mur_egout', color=color.gray))

# scene 3

foret_scene.add_entity("bacground_foret", Entity(model='cube', scale=(
    70, 25), position=(0, -1), collider='box', color=color.black))

foret_scene.add_entity("ground_1_foret", Entity(model='cube', scale=(
    70, 25), position=(0, -1), collider='box', color=color.white))
