import sys


def get_inventory(argv: list[str]) -> dict[str, int]:
    created_dict: dict[str, int] = {}
    for i in range(1, len(argv)):
        try:
            temp_list = argv[i].split(":")
            if (len(temp_list) == 2):
                if (temp_list[0] in created_dict.keys()):
                    print(f"Redundant item '{temp_list[0]}' - discarding")
                else:
                    created_dict[temp_list[0]] = int(temp_list[1])
            else:
                print("Invalid syntax for", argv[i])
        except ValueError as obj:
            print("Quantity error for 'key':", obj)
    return (created_dict)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = get_inventory(sys.argv)
    if (inventory == {}):
        print("The inventory is empty.")
    else:
        print("Got inventory:", inventory)
        print("Item list:", list(inventory.keys()))
        print("Total quantity of the", len(inventory.keys()),
              "items:", sum(inventory.values()))
        for i in inventory.keys():
            print("Item", i, "represents",
                  round((inventory[i]/sum(inventory.values())*100), 1), "%")
        for i in inventory.keys():
            if (inventory[i] == max(inventory.values())):
                print("Item most abundant:", i, "with quantity", inventory[i])
        for i in inventory.keys():
            if (inventory[i] == min(inventory.values())):
                print("Item least abundant:", i, "with quantity", inventory[i])
    print("Let's add two laser guns")
    inventory["laser pistol"] = 2
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
