class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name + ":", self.height, "cm,", self.age, "days old")


def ft_garden_data() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant1.show()
    plant2 = Plant("Sunflower", 80, 45)
    plant2.show()
    plant3 = Plant("Cactus", 15, 120)
    plant3.show()


if __name__ == "__main__":
    ft_garden_data()
