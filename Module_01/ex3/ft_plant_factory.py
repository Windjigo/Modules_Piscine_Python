class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name + ":", self.height, "cm,", self.age, "days old")

    def grow(self, time: int) -> None:
        self.height = int(self.height) + 0.1 * int(self.height) * time

    def get_older(self, time: int) -> None:
        self.age += time


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25.0, 30)
    print("Created:", end=" ")
    plant1.show()
    plant2 = Plant("Oak", 200.0, 365)
    print("Created:", end=" ")
    plant2.show()
    plant3 = Plant("Cactus", 5.0, 90)
    print("Created:", end=" ")
    plant3.show()
    plant4 = Plant("Sunflower", 80.0, 45)
    print("Created:", end=" ")
    plant4.show()
    plant5 = Plant("Fern", 15.0, 120)
    print("Created:", end=" ")
    plant5.show()


if __name__ == "__main__":
    ft_plant_factory()
