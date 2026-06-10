from abc import ABC, abstractmethod
from ex0.creatures import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        creature.attack()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (hasattr(creature, "heal"))

    def act(self, creature: Creature) -> None:
        try:
            creature.attack()
            creature.heal(creature.name)
        except Exception as obj:
            print(obj)


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return (hasattr(creature, "revert") and hasattr(creature, "transform"))

    def act(self, creature: Creature) -> None:
        try:
            creature.transform()
            creature.attack()
            creature.revert()
        except Exception as obj:
            print(obj)
