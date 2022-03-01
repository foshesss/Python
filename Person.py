from abc import (
  ABC,
  abstractmethod,
)

class Entity(ABC): # cannot instantiate
    def __init__(self, name, level = 1):
        self.name = name
        self._level = level

    @abstractmethod
    def attack(self): # can call this if needed
        ...

class Goblin(Entity):
    def attack(self):
        print("AYYE")

g = Goblin("David")
g.attack()

print(10 % 10)


