from random import randint

from entity.plant import Berry


class Animal(object):
    icon: str = ' '
    is_predator: bool = False
    instances: list = []

    property = {
        'max_hp': None,
        'velocity': None,
        'power': None,
        'hunger': None,
        'life': None
    }

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.instances.append(instance)
        return instance

    def __init__(
            self,
            max_hp: int,
            velocity: int,
            power: int,
            hunger: int,
            life: int
    ) -> None:
        self.max_hp = max_hp
        self.hp = max_hp
        self.velocity = velocity
        self.is_man = randint(0, 1)
        self.power = power
        self.hunger = hunger
        self.life = life
        self.pos_x = None
        self.pos_y = None

    def __repr__(self) -> str:
        return self.icon

    def __str__(self) -> str:
        return self.__repr__()

    def step(self) -> None:
        self.life -= 1
        self.hunger -= 1
        self.power -= 1
        self.velocity -= 1
        if self.life == 0 or self.hunger == 0:
            self.instances.remove(self)

    def eat(self, other) -> None:
        delta = 0
        if isinstance(other, Berry):
            self.hp += (other.hungry // 2) if self.is_predator else other.hungry
            Berry.instances.remove(other)
            delta = (other.hungry // 2) if self.is_predator else other.hungry
        elif self.power > other.hp:
            self.hp += other.hp
            self.instances.remove(other)
            delta = other.hp
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
        self.hunger += delta
        self.power += delta
        self.velocity += delta

    def reproduction(self, other: "Animal") -> None:
        if self.__class__ == other.__class__:
            if self.hp * 0.7 > self.max_hp and other.hp * 0.7 > other.max_hp:
                self.__class__(**self.property)
