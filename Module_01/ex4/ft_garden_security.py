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


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 25.0, 30)
    print(plant1.get_age(), plant1.get_height())
    plant1 = Plant("Rose", -25.0, 30)
    print(plant1.get_age(), plant1.get_height())
    plant1 = Plant("Rose", 25.0, -30)
    print(plant1.get_age(), plant1.get_height())
    plant1.set_age(25)
    plant1.set_height(5)
    plant1.set_age(-25)
    plant1.set_height(-5)


if __name__ == "__main__":
    ft_garden_security()
