import ex1
import ex0


def test_factory_with_capa(factory: ex0.CreatureFactory) -> None:
    try:
        print(type(factory))
        print(" Base:")
        base = factory.create_base()
        base.describe()
        base.attack()
        if (type(factory) is ex1.factories.HealingCreatureFactory):
            base.heal(base.name)
        else:
            base.transform()
            base.attack()
            base.revert()
        print(" Evolved:")
        evolved = factory.create_evolved()
        evolved.describe()
        evolved.attack()
        if (type(factory) is ex1.factories.HealingCreatureFactory):
            evolved.heal(evolved.name)
        else:
            evolved.transform()
            evolved.attack()
            evolved.revert()
    except Exception as obj:
        print(obj)


def main() -> None:
    Heal = ex1.HealingCreatureFactory()
    Trans = ex1.TransformingCreatureFactory()
    print("Testing creature with healing capabilities")
    test_factory_with_capa(Heal)
    print("\nTesting creature with transform capabilities")
    test_factory_with_capa(Trans)


if __name__ == "__main__":
    main()
