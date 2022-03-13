from ursina import *
from projectile import *
from creation_personnage import *
from coeur import *
from functools import partial
from scene import Scene
from entity import *
from bob_le_chef_dorchestre import bob
from jeu import actual_scene

asset_folder = '../asset/'

add_to_all_scene = Scene(None)

death_scene = Scene(None)


# add to all scene

add_to_all_scene.add_entity("player", Personnage(add_to_scene_entities=False, max_jumps=2, color=color.white, texture=asset_folder +
                                                 "poutine", scale_x=2, scale_y=4, spawnpoint=(0, 1, 0)))


coeur = Coeur(add_to_scene_entities=False,
              texture=asset_folder + 'coeur', vie=3)

affichage_vodka = Vodka(add_to_scene_entities=False,
                        texture=asset_folder + 'vodka', nb_vodka=0)


# death scene

def test(item: Button):
    scene_afficher = Scene(bob(add_to_all_scene, actual_scene))
    scene.entities = scene_afficher.get_entities()


death_scene.add_entity("bouton", Button(add_to_scene_entities=False, parent=window, color=color.black, position=(
    0, -0.3), text="RETRY", scale=(0.25, 0.1)))
item._on_click = partial(test, item)
item.visible = False
