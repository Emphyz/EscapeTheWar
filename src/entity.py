from ursina import *
from projectile import *
from creation_personnage import *
from coeur import *
from functools import partial

from scene import Scene

asset_folder = '../asset/'

hub_scene = Scene(None)

tutorial_scene = Scene(None)

egout_scene = Scene(None)

foret_scene = Scene(None)

plaine_scene = Scene(None)

frontiere_scene = Scene(None)

# scene egout

projectile = Entity(add_to_scene_entities=False, model='cube', collider='box', color=color.white, position=(
    10, 0), texture=asset_folder + 'vodka', scale=(2, 4))

scie = Entity(add_to_scene_entities=False, model='cube', collider='box', color=color.white, position=(
    70, -25), texture=asset_folder + "scie", scale_x=2, scale_y=2)

background_city = Entity(add_to_scene_entities=False, model='quad', collider=False, scale=(
    120, 60), position=(0, 23.5, 5), texture=asset_folder + 'city')

ground_s1 = Entity(add_to_scene_entities=False, model='cube', scale=(70, 25), position=(
    0, -14.5), collider='box', color=color.black)

ground_s2 = Entity(add_to_scene_entities=False, model='cube', scale=(300, 14), position=(
    197.5, -8), collider='box', color=color.black)

wallstart = Entity(add_to_scene_entities=False, model='cube', collider='box', scale=(
    5, 12), position=(-10, 4), color=color.black)

wallstart2 = Entity(add_to_scene_entities=False, model='cube', collider='box', scale=(
    5, 25), position=(50, -2), color=color.black)

plaque_e1 = Entity(add_to_scene_entities=False, model='cube', scale=(12.5, 1), position=(
    41.25, -3, -2), collider='box', color=color.gray)

ground_e1 = Entity(add_to_scene_entities=False, model='cube', scale=(100, 20), position=(
    50, -37), collider='box', color=color.black)

ground_e_back1 = Entity(add_to_scene_entities=False, model='cube', scale=(16, 49), position=(
    41.5, -22.5, 4), texture=asset_folder + 'mur_egout', color=color.gray)

obstacle = [ground_s1, ground_s2, wallstart, wallstart2,
            plaque_e1, ground_e1, ground_e_back1, scie]

all_entity = [background_city, projectile, scie,
              ground_s1, ground_s2, wallstart, wallstart2, plaque_e1, ground_e1, ground_e_back1]

player = Personnage(add_to_scene_entities=False, max_jumps=2, color=color.white, texture=asset_folder +
                    "poutine", scale_x=2, scale_y=4, spawnpoint=(0, 1, 0), all_entity=all_entity)
camera.add_script(SmoothFollow(target=player, offset=[0, 1, -30], speed=10))
player.collider = BoxCollider(player, center=Vec3(0, 2, 1), size=Vec3(2, 4, 2))

projectile = Entity(add_to_scene_entities=False, model='cube', collider='box', position=(10, 0), texture=asset_folder +
                    'vodka', scale=(2, 4), obstacle=obstacle, position_lancer=player.position)

Mortal = [scie]
vodka_a = [projectile]


egout_scene.add_entity("projectile", Entity(add_to_scene_entities=False, model='cube', collider='box', color=color.white, position=(
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

egout_scene.add_entity("player", Personnage(add_to_scene_entities=False, max_jumps=2, color=color.white, texture=asset_folder +
                                            "poutine", scale_x=2, scale_y=4, spawnpoint=(0, 1, 0), all_entity=all_entity))

egout_scene.add_entity("projectile", Entity(add_to_scene_entities=False, model='cube', collider='box', position=(10, 0), texture=asset_folder +
                                            'vodka', scale=(2, 4), obstacle=obstacle, position_lancer=player.position))


def test(item: Button):
    app.restart()


item = Button(add_to_scene_entities=False, parent=window, color=color.black, position=(
    0, -0.3), text="RETRY", scale=(0.25, 0.1))
item._on_click = partial(test, item)
item.visible = False

coeur = Coeur(add_to_scene_entities=False,
              texture=asset_folder + 'coeur', vie=3)
affichage_vodka = Vodka(add_to_scene_entities=False,
                        texture=asset_folder + 'vodka', nb_vodka=0)

scene2 = [player, scie, projectile, coeur, affichage_vodka, item, background_city,
          ground_s1, ground_s2, wallstart, wallstart2, plaque_e1, ground_e1, ground_e_back1]

# scene 2

s2_ground_s1 = Entity(model='cube', scale=(70, 25), position=(
    0, -1), collider='box', color=color.black)

s2_background_foret = Entity(model='cube', scale=(100, 50), position=(
    0, 0, -5), collider='box', color=color.white)

scene3 = [player, s2_ground_s1, s2_background_foret]

foret_scene.add_entity("bacground_foret", Entity(model='cube', scale=(70, 25), position=(0, -1), collider='box', color=color.black))

foret_scene.add_entity("ground_1_foret", Entity(model='cube', scale=(70, 25), position=(0, -1), collider='box', color=color.white))