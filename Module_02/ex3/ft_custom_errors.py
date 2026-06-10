class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.message = message


def test_plant_error(plant_state: str, water_state: str) -> None:
    try:
        if (plant_state == "wilting"):
            raise PlantError("The tomato plant is wilting!")
        else:
            print("No plant error")
    except PlantError as obj:
        print("Caught PlantError:", obj)


def test_water_error(plant_state: str, water_state: str) -> None:
    try:
        if (water_state == "drought"):
            raise WaterError("Not enough water in the tank!")
        else:
            print("No water error")
    except WaterError as obj:
        print("Caught WaterError:", obj)


def test_garden_error(plant_state: str, water_state: str) -> None:
    try:
        if (plant_state == "wilting" and water_state == "drought"):
            raise GardenError("Problems with the water and the plant!")
        elif (plant_state == "wilting"):
            raise PlantError("The tomato plant is wilting!")
        elif (water_state == "drought"):
            raise WaterError("Not enough water in the tank!")
        else:
            print("No garden error")
    except GardenError as obj:
        print("Caught GardenError:", obj)


def main():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    test_plant_error("wilting", "drought")
    test_plant_error("flowering", "drought")
    print("\nTesting WaterError...")
    test_water_error("wilting", "drought")
    test_water_error("wilting", "watered")
    print("\nTesting catching all garden errors...")
    test_garden_error("wilting", "drought")
    test_garden_error("flowering", "drought")
    test_garden_error("wilting", "watered")
    test_garden_error("flowering", "watered")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
