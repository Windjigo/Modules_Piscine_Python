def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        print(int("abc"))
    elif (operation_number == 1):
        print(10/0)
    elif (operation_number == 2):
        open("/non/existent/file")
    elif (operation_number == 3):
        print(3 + "str")
    else:
        x = 3 * 4
        print(x)


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
        print("Operation completed successfully")
    except Exception as obj:
        if (operation_number == 0):
            print("Caught ValueError:", obj)
        elif (operation_number == 1):
            print("Caught ZeroDivisionError:", obj)
        elif (operation_number == 2):
            print("Caught FileNotFoundError:", obj)
        else:
            print("Caught TypeError:", obj)


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_types(0)
    print("Testing operation 1...")
    test_error_types(1)
    print("Testing operation 2...")
    test_error_types(2)
    print("Testing operation 3...")
    test_error_types(3)
    print("Testing operation 4...")
    test_error_types(4)
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
