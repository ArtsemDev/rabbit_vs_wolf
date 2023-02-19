class Berry(object):
    instances: list = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.instances.append(instance)
        return instance

    def __init__(self):
        self.life: int = 20
        self.hungry: int = 2
        self.icon: str = '🌿'
        self.pos_x = None
        self.pos_y = None

    def grow(self) -> None:
        self.icon = '🍓'
        self.hungry *= 2

    def step(self) -> None:
        self.life -= 1
        if self.life == 10:
            self.grow()
        if self.life == 0:
            self.instances.remove(self)

    def __repr__(self) -> str:
        return self.icon

    def __str__(self) -> str:
        return self.__repr__()
