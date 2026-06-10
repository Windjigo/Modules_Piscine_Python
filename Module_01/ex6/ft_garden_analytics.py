class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        if (age < 0):
            print(self._name + ":", "Error, age can't be negative. \
Default age used")
            self._age = 1
        else:
            self._age = age
        if (height < 0):
            print(self._name + ":", "Error, height can't be negative. \
Default height used")
            self._height = 1
        else:
            self._height = height
        self.stats = Plant.Statistics(self)

    def show(self) -> None:
        self.stats.upgrade("show")
        print(self._name + ":", self._height, "cm,", self._age, "days old")

    def grow(self, time: int) -> None:
        self.stats.upgrade("grow")
        self._height = int(self._height) + 0.1 * int(self._height) * time

    def age(self, time: int) -> None:
        self.stats.upgrade("age")
        self._age += time

    def set_height(self, new_height: int) -> None:
        if (new_height < 0):
            print(self._name + ":", "Error, height can't be negative. \
\nHeight update rejected")
            return
        else:
            print(self._name + ":", "Height updated")
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(self._name + ":", "Error, age can't be negative. \
\nAge update rejected")
            return
        else:
            print(self._name + ":", "Age updated")
            self._height = new_age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    @staticmethod
    def verif_age(self) -> int:
        if (self._age >= 365):
            return (True)
        else:
            return (False)

    @classmethod
    def unknown(cls):
        return cls("Unknown plant", 0.0, 0)

    class Statistics:
        def __init__(self, owner: str) -> None:
            self._owner = owner
            self._numb_grow = 0
            self._numb_age = 0
            self._numb_show = 0

        def upgrade(self, pointer: str) -> None:
            if (pointer == "grow"):
                self._numb_grow += 1
            elif (pointer == "age"):
                self._numb_age += 1
            else:
                self._numb_show += 1

        def show_stat(self) -> None:
            print("Stats:", self._numb_grow, "grow,",
                  self._numb_age, "age,", self._numb_show, "show")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        self._trunk = trunk
        super().__init__(name, height, age)
        self.stats = Tree.Statistics(self)

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._trunk, "cm")

    def shade(self) -> None:
        self.stats.upgrade("shade")
        print(f"Tree {self._name} now produces a shade of", self._height,
              "cm long and", self._trunk, "cm wide")

    class Statistics(Plant.Statistics):
        def __init__(self, owner: str) -> None:
            super().__init__(owner)
            self.numb_shade = 0

        def upgrade(self, pointer: str) -> None:
            if (pointer != "shade"):
                super().upgrade(pointer)
            else:
                self.numb_shade += 1

        def show_stat(self) -> None:
            super().show_stat()
            print(self.numb_shade, "shade")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, bloom: int) -> None:
        self._color = color
        self._bloom = bloom
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print("Color:", self._color)
        if (self._bloom == 0):
            print(self._name, "has not bloomed yet.")
        else:
            print(self._name, "has already bloomed")

    def bloom(self) -> None:
        if (self._bloom == 0):
            print(self._name, "has bloomed beautifully!")
            self._bloom = 1
        else:
            print(self._name, "has already bloomed")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest: str, nutrition: int) -> None:
        self._harvest = harvest
        self._nutrition = nutrition
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print("Harvest season:", self._harvest)
        print("Nutritional value =", self._nutrition)

    def grow(self, time: int) -> None:
        tmp = self._height
        super().grow(time)
        self._nutrition += (self._height - tmp)*2

    def age(self, time: int) -> None:
        tmp = self._age
        super().age(time)
        self._nutrition += (self._age - tmp)*0.5


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int,
                 color: str, bloom: int, seed: int) -> None:
        super().__init__(name, height, age, color, bloom)
        if (bloom == 0 & seed != 0):
            self._seed = 0
            print(self._name + ":", "Number of seeds invalid, defaulting to 0")
        else:
            self._seed = seed

    def bloom(self) -> None:
        if (self._bloom == 0):
            self._seed = round(self._height / 10)
        super().bloom()

    def show(self) -> None:
        super().show()
        print("Seeds:", self._seed)


def access_stats(plant: Plant) -> None:
    plant.stats.show_stat()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    plant1 = Plant("test1", 1, 200)
    print("Is 200 days more than a year? ->", Plant.verif_age(plant1))
    plant1 = Plant("test1", 1, 400)
    print("Is 400 days more than a year? ->", Plant.verif_age(plant1))
    print("\n=== Flower")
    plant1 = Flower("Rose", 15.0, 10, "red", 0)
    plant1.show()
    print("[statistics for Rose]")
    access_stats(plant1)
    print("[asking the rose to grow and bloom]")
    plant1.bloom()
    plant1.grow(5)
    plant1.show()
    print("[statistics for Rose]")
    access_stats(plant1)
    print("\n=== Tree")
    plant1 = Tree("Oak", 200.0, 365, 5.0)
    plant1.show()
    print("[statistics for Oak]")
    access_stats(plant1)
    print("[asking the tree to produce shade]")
    plant1.shade()
    print("[statistics for Rose]")
    access_stats(plant1)
    print("\n=== Seed")
    plant1 = Seed("Sunflower", 80.0, 45, "yellow", 0, 0)
    plant1.show()
    print("[statistics for Sunflower]")
    access_stats(plant1)
    print("[make sunflower grow, age and bloom]")
    plant1.grow(5)
    plant1.age(5)
    plant1.bloom()
    plant1.show()
    print("[statistics for Sunflower]")
    access_stats(plant1)
    print("\n=== Anonymous")
    plant1 = Plant.unknown()
    plant1.show()
    print("[statistics for Unknown plant]")
    access_stats(plant1)


if __name__ == "__main__":
    ft_garden_analytics()
