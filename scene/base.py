from itertools import product
from random import randint, choices

from entity.animal import Rabbit, Wolf
from entity.animal.base import Animal
from entity.plant import Berry


class Frame(object):

    def __init__(
            self,
            width: int,
            height: int,
            berries_count: int,
            animal_count: int
    ) -> None:
        coords = choices([*product(range(width), range(height))], k=berries_count + animal_count)
        for _ in range(berries_count):
            obj = Berry()
            obj.pos_x, obj.pos_y = coords[0]
            del coords[0]
        for _ in range(animal_count // 2):
            obj = Rabbit()
            obj.pos_x, obj.pos_y = coords[0]
            del coords[0]
            obj = Wolf()
            obj.pos_x, obj.pos_y = coords[0]
            del coords[0]

        self.width = width
        self.height = height

    def render(self):
        frame = [
            ['🟩' for _ in range(self.width)]
            for _ in range(self.height)
        ]
        for berry in Berry.instances:
            frame[berry.pos_x][berry.pos_y] = f'{berry}'

        for animal in Animal.instances:
            frame[animal.pos_x][animal.pos_y] = f'{animal}'

        return '\n'.join(''.join(line) for line in frame)
