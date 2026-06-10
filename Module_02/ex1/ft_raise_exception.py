def input_temperature(temp_str: str) -> int | None:
    try:
        if (int(temp_str) < 0):
            raise ValueError("°C is too cold for plants (min 0°C)")
        elif (int(temp_str) > 40):
            raise ValueError("°C is too hot for plants (max 40°C)")
        return (int(temp_str))
    except ValueError as obj:
        print(int(temp_str), obj)
        return (None)


def test_temperature(temp_str: str) -> None:
    print("\nInput data is", temp_str)
    try:
        if (input_temperature(temp_str) is not None):
            print("Temperature is now", input_temperature(temp_str), "°C")
    except ValueError as obj:
        print("Caught ValueError:", obj)


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature('25')
    test_temperature('abc')
    test_temperature('100')
    test_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
