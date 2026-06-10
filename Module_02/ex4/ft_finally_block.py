class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


def water_plant(plant_name: str) -> int:
    try:
        for i in plant_name:
            if (i == plant_name[0] and i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                raise PlantError("Invalid plant name to water:")
            if (i != plant_name[0] and i not in "abcdefghijklmnopqrstuvwxyz"):
                raise PlantError("Invalid plant name to water:")
        print("Watering", plant_name, ": [OK]")
        return (0)
    except PlantError as obj:
        print("Caught PlantError :", obj, plant_name)
        return (1)


def test_watering_system(plant1: str, plant2: str, plant3: str) -> None:
    print("Opening watering system")
    try:
        if (water_plant(plant1) == 1):
            raise Exception(".. ending tests and returning to main")
        if (water_plant(plant2) == 1):
            raise Exception(".. ending tests and returning to main")
        if (water_plant(plant3) == 1):
            raise Exception(".. ending tests and returning to main")
    except Exception as obj:
        print(obj)
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system("Tomato", "Potato", "Lettuce")
    print("\nTesting invalid plants...")
    test_watering_system("Tomato", "potato", "Lettuce")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
