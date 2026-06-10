from ex0.creatures import Creature
from abc import ABC, abstractmethod


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> None:
        self.transformation = True

    @abstractmethod
    def revert(self) -> None:
        self.transformation = False


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformation = False

    def attack(self) -> None:
        if (self.transformation is False):
            print(f"{self.name} used Bash")
        else:
            print(f"{self.name} used Slash")

    def transform(self) -> None:
        print(f"{self.name} is transforming into a sharper form!")
        super().transform()

    def revert(self) -> None:
        print(f"{self.name} is going back to his base form")
        super().revert()


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal")
        self.transformation = False

    def attack(self) -> None:
        if (self.transformation is False):
            print(f"{self.name} used Double-Edge")
        else:
            print(f"{self.name} used Draco Meteor")

    def transform(self) -> None:
        print(f"{self.name} is transforming into a dragonic batle form!")
        super().transform()

    def revert(self) -> None:
        print(f"{self.name} is too tired to maintain its form")
        super().revert()
