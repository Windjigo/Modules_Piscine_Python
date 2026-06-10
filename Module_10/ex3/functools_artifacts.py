import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int | Exception:
    try:
        if (spells == []):
            return (0)
        if (operation == "add"):
            return functools.reduce(lambda x, y: operator.add(x, y), spells)
        if (operation == "multiply"):
            return functools.reduce(lambda x, y: operator.mul(x, y), spells)
        if (operation == "max"):
            return functools.reduce(lambda x, y: max(x, y), spells)
        if (operation == "min"):
            return functools.reduce(lambda x, y: min(x, y), spells)
        else:
            raise Exception("Unknown operation")
    except Exception as obj:
        return (obj)


def partial_enchanter(base_enchantment: Callable) \
        -> dict[str, functools.partial]:
    dico = {"fire":
            functools.partial(base_enchantment, power=50, element="flaming"),
            "ice":
            functools.partial(base_enchantment, power=50, element="Frozen"),
            "lightning":
            functools.partial(base_enchantment, power=50, element="Shocking")}
    return dico


@functools.lru_cache(3)
def memoized_fibonacci(n: int) -> int:
    if (n < 2):
        return (n)
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def normal_fibonacci(n: int) -> int:
    if (n < 2):
        return (n)
    return (normal_fibonacci(n-1) + normal_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return (f"{spell} is from an unknown spell type")

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return (f"Damage spell: {spell} damage")

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return (f"Enchantment: {spell}")

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return (f"Multi-cast: {len(spell)} spells")

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> None:
    print(f"Enchant {target} with {element}, lvl {power}")


def main() -> None:
    print("=== Functools artifacts ===\n")
    print("Testing spell reducer with [16, 21, 33, 34, 37, 33] ...")
    print("Sum =", spell_reducer([16, 21, 33, 34, 37, 33], "add"),
          "\nProduct =", spell_reducer([16, 21, 33, 34, 37, 33], "multiply"),
          "\nMax =", spell_reducer([16, 21, 33, 34, 37, 33], "max"),
          "\nMin =", spell_reducer([16, 21, 33, 34, 37, 33], "min"),
          "\nUnknown =", spell_reducer([16, 21, 33, 34, 37, 33], "test"),)
    print("\nTesting partial enchanter ...")
    print(partial_enchanter(base_enchantment))
    print("\nTesting memoized fibonacci ...")
    print(f"Fib(0) = {memoized_fibonacci(0)}\nFib(1) = \
{memoized_fibonacci(1)}\nFib(10) = {memoized_fibonacci(10)} \
\nFib(35) = {memoized_fibonacci(35)}")
    print("Testing ordinary fibonacci ...")
    print(f"Fib(0) = {normal_fibonacci(0)}\nFib(1) = \
{normal_fibonacci(1)}\nFib(10) = {normal_fibonacci(10)} \
\nFib(35) = {normal_fibonacci(35)}")
    print("\nTesting spell dispatcher with 4 differents types...")
    dispatch = spell_dispatcher()
    dico = {"x": "y", 1: 2}
    enchant = "Healing"
    print(f"{dispatch(dico)}\n{dispatch(10)}\n{dispatch(enchant)} \
\n{dispatch([1, 2, 3])}")


if __name__ == "__main__":
    main()
