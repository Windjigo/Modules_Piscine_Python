from ex0.creatures import Creature
from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> None:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> None:
        print(f"{self.name} used Vine whip")

    def heal(self, target: str) -> None:
        print(f"{self.name} used heal. {target} is slightly healed")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass")

    def attack(self) -> None:
        print(f"{self.name} used Solar Beam")

    def heal(self, target: str) -> None:
        print(f"{self.name} used Megaheal. {target} is fully healed")
