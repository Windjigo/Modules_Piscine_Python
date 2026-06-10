from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def count_up_by_1() -> int:
        nonlocal count
        count += 1
        return count

    return count_up_by_1


def spell_accumulator(initial_power: int) -> Callable:
    count = 0

    def count_up_by_x() -> int:
        nonlocal count
        count += initial_power
        return count

    return count_up_by_x


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchanter(item_name: str) -> str:
        return (f"{enchantment_type} {item_name}")

    return (enchanter)


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: str) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        try:
            return (vault[key])
        except KeyError:
            return ("Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("\n=== Scope mysteries ===")
    print("\nTesting mage counter :")
    counter = mage_counter()
    counter2 = mage_counter()
    for i in range(5):
        print(f"After {i} iteration, counter 1 = {counter()}")
    print("At the end, counter 2=", counter2())
    print("\nTesting spell accumulator :")
    counter = spell_accumulator(5)
    counter2 = spell_accumulator(3)
    for i in range(5):
        print(f"After {i} iteration, counter 1 = {counter()}")
    print("At the end, counter 2=", counter2())
    print("\nTesting enchantment factory :")
    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    print(f"Testing the flaming enchantment \
factory on two items :\n{fire_factory('Sword')}\
, {fire_factory('Barbecue')}")
    print(f"Testing the frozen enchantment \
factory on two items :\n{ice_factory('Sword')}\
, {ice_factory('Candy Cane')}")
    print("\nTesting memory vault :")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Trying to recall the \
secret entry previously stored:", vault["recall"]("secret"))
    print("Trying to recall the \
test entry not found in the vault:", vault["recall"]("test"))


if __name__ == "__main__":
    main()
