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
'''
    def add_entities(self, new_entities: Dict[str, Entity]):
        for i in new_entities:
            self.__entities.append(i)

    def change_entity(self, entity_change, new_entity: Entity):  #utiliser Del
        for i in range(len(self.__entities)):
            if self.__entities[i] == entity_change:
                self.__entities[i] = new_entity

    def change_entities(self, entities_change: Dict[str, Entity], new_entities: Dict[str, Entity]):
        a = 0
        for i in entities_change:
            self.change_entity(self, i, new_entities[a])
            a += 1
'''