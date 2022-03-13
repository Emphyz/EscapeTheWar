from typing import Dict
from ursina import *

Ursina()


class Scene():
    def __init__(self, entities: Dict[str, Entity]):
        self.__entities = entities

    def get_entity(self, key):
        return self.__entities.get(key)

    def get_entities(self):
        return self.__entities

    def keys_entities(self):
        return self.__entities.keys()

    def values_entities(self):
        return self.__entities.values()

    def set_entities(self, new_entities: Dict[str, Entity]):
        self.__entities = new_entities

    def add_entity(self, nom: str, new_entity: Entity):
        self.__entities[nom] = new_entity