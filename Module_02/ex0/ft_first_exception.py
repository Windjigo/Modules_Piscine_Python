def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature(temp_str: str) -> None:
    print("\nInput data is", temp_str)
    try:
        print("Temperature is now", input_temperature(temp_str), "°C")
    except ValueError as obj:
        print("Caught ValueError:", obj)


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
