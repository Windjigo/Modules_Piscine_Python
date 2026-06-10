import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    try:
        print(" Base:")
        base = factory.create_base()
        base.describe()
        base.attack()
        print(" Evolved:")
        evolved = factory.create_evolved()
        evolved.describe()
        evolved.attack()
    except Exception as obj:
        print(obj)


def battle_base(factory1: ex0.CreatureFactory, factory2: ex0.CreatureFactory) \
        -> None:
    try:
        base1 = factory1.create_base()
        base2 = factory2.create_base()
        base1.describe()
        print(" vs.")
        base2.describe()
        print(" fight!")
        base1.attack()
        if (base1.type == "Water"):
            print(f"{base2.name} has been KOed")
            return
        base2.attack()
        if (base2.type == "Water"):
            print(f"{base1.name} has been KOed")
            return
    except Exception as obj:
        print(obj)


def main() -> None:
    fire = ex0.FlameFactory()
    water = ex0.WaterFactory()
    print("Testing factory")
    test_factory(fire)
    print("\nTesting factory")
    test_factory(water)
    print("\nTesting battle")
    battle_base(fire, water)
    print("")
    battle_base(water, fire)


if __name__ == "__main__":
    main()
