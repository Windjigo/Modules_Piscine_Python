import alchemy


def main():
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", alchemy.create_air())
    print("Testing the hidden create_earth: ")
    print(alchemy.create_earth())


if __name__ == "__main__":
    main()
