from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return (base_spell(target, power*multiplier))
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if (condition(target, power) is True):
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def launch_spells(target: str, power: int) -> Any:
        res = []
        for i in spells:
            res += [i(target, power)]
        return res
    return launch_spells


def heal(target: str, power: int) -> str:
    return f"Heal restores {power} HP to the {target}"


def fireball(target: str, power: int) -> str:
    return f"Fireball deals {power} damage to the {target}"


def condition(target: str, power: int) -> bool:
    return power >= 5


def main() -> None:
    print("\n=== Higher Magic ===")
    print("\nTesting spell combiner :")
    combiner = spell_combiner(heal, fireball)
    print("Combined heal and fireball =", combiner("Dragon", 10))
    print("\nTesting power amplifier:")
    amplified = power_amplifier(fireball, 3)
    print("Normal =", fireball("Dragon", 10),
          "\nAmplified by 3 =", amplified("Dragon", 10))
    print("\nTesting Conditional caster:")
    conditional = conditional_caster(condition, fireball)
    print("Testing with condition respected =", conditional("Dragon", 10))
    print("Testing with condition unfulfilled =", conditional("Dragon", 4))
    print("\nTesting spell sequence:")
    sequence = spell_sequence([fireball, heal])
    print("Testing the sequencer with fireball and heal =",
          sequence("Dragon", 10))


if __name__ == "__main__":
    main()
