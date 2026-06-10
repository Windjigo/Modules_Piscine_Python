from ex0.factories import CreatureFactory
from .heal_creature import Sproutling, Bloomelle
from .transform_creature import Morphagon, Shiftling
from ex0.creatures import Creature


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
