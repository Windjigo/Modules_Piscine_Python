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

    def show(self) -> None:
        print(self._name + ":", self._height, "cm,", self._age, "days old")

    def grow(self, time: int) -> None:
        self._height = int(self._height) + 0.1 * int(self._height) * time

    def age(self, time: int) -> None:
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


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        self._trunk = trunk
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", self._trunk, "cm")

    def shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", self._height,
              "cm long and", self._trunk, "cm wide")


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


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Tree")
    plant1 = Tree("Oak", 200.0, 300, 8)
    plant1.show()
    print("[asking the oak to produce shade]")
    plant1.shade()
    print("\n=== Flower")
    plant2 = Flower("Rose", 20.0, 30, "red", 0)
    plant2.show()
    print("[asking the rose to bloom]")
    plant2.bloom()
    print("[asking the rose to bloom]")
    plant2.bloom()
    print("\n=== Vegetable")
    plant3 = Vegetable("Tomato", 2.0, 3, "April", 0)
    plant3.show()
    print("[make tomato grow and age for 20 days]")
    plant3.age(20)
    plant3.grow(20)
    plant3.show()


if __name__ == "__main__":
    ft_plant_types()
