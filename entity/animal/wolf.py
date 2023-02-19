from .base import Animal


class Wolf(Animal):
    icon: str = '🐺'
    is_predator: bool = True
    property = {
        'max_hp': 10,
        'velocity': 3,
        'power': 5,
        'hunger': 10,
        'life': 50
    }

    def __init__(self):
        super().__init__(**self.property)
