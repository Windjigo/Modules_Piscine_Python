class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name + ":", self.height, "cm,", self.age, "days old")

    def grow(self, time: int) -> None:
        self.height = int(self.height) + 0.1 * int(self.height) * time

    def get_older(self, time: int) -> None:
        self.age += time


def ft_garden_grow() -> None:
    plant1 = Plant("Rose", 25, 30)
    i = 1
    print("=== Garden Plant Growth ===")
    origin = plant1.height
    while (i < 7):
        print("=== Day", i, "===")
        plant1.show()
        i += 1
        plant1.grow(1)
        plant1.get_older(1)
    print("=== Day", i, "===")
    plant1.show()
    print("Growth this week:", int(plant1.height) - origin, "cm")


if __name__ == "__main__":
    ft_garden_grow()
