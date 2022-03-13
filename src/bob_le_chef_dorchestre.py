from ursina import *
from scene import *


def bob(entity1: Dict[str, Entity], entity2: Dict[str, Entity]):
    return {**entity1, **entity2}
