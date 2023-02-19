from .base import Animal


class Rabbit(Animal):
    icon: str = '🐰'
    is_predator: bool = False
    property = {
        'max_hp': 7,
        'velocity': 4,
        'power': 2,
        'hunger': 7,
        'life': 25
    }

    def __init__(self):
        super().__init__(**self.property)
