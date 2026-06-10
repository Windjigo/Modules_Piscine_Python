from abc import ABC, abstractmethod
from .creatures import Torragon, Aquabub, Flameling, Pyrodon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class WaterFactory(CreatureFactory):
    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()
