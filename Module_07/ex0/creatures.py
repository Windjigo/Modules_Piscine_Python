from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> None:
        print(f"{self.name} is a {self.type} type creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> None:
        print(f"{self.name} used Ember")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> None:
        print(f"{self.name} used Flamethrower")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> None:
        print(f"{self.name} used Bubble")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> None:
        print(f"{self.name} used Hydro Pump")
