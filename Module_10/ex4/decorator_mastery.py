import functools
import time
import random
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def timed(*args, **kwargs) -> None:
        start = time.time()
        print(f"Casting {func.__name__}")
        func(*args, **kwargs)
        execution_time = time.time() - start
        print(f"Spell completed in {round(execution_time, 3)} seconds")
    return timed


def power_validator(min_power: int) -> Callable:
    def power_validator(func: Callable) -> Callable:
        @functools.wraps(func)
        def validated(*args, **kwargs) -> str:
            try:
                if (int(args[0]) >= min_power):
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
            except Exception:
                if (int(args[2]) >= min_power):
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
        return validated
    return power_validator


def retry_spell(max_attempts: int) -> Callable:
    def retry_spell(func: Callable) -> Callable:
        @functools.wraps(func)
        def retry(*args, **kwargs) -> str:
            i = 0
            while i < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    i += 1
                    print(f"Spell failed, \
retrying... (attempt {i}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts")
        return retry
    return retry_spell


class MageGuild:
    def __init__(self):
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for i in name:
            if (i.isalpha() is not True and i.isspace() is not True):
                return (False)
        if (len(name) < 3):
            return (False)
        return (True)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with <{power}> power")


@power_validator(5)
def fireball(power: int, target: str) -> str:
    return f"Fireball deals {power} damage to the {target}"


@spell_timer
def waiter() -> None:
    time.sleep(2)
    print("Done !")


@retry_spell(10)
def unstable_spell() -> str:
    if random.randint(1, 10) > 9:
        return ("Done")
    else:
        raise Exception("Spell destabilized")


def main() -> None:
    print("\nTesting Wrappers")
    print("\nTest 1 : Spell timer")
    waiter()
    if (waiter.__name__ == "waiter"):
        print("Functools.wraps fonctionnel")
    else:
        print("Failed Functools.wraps")
    print("\nTest 2 : Power validator")
    print(fireball(2, "Dragon"))
    print(fireball(6, "Dragon"))
    if (fireball.__name__ == "fireball"):
        print("Functools.wraps fonctionnel")
    else:
        print("Failed Functools.wraps")
    print("\nTest 3 : Retry spell")
    print(unstable_spell())
    print(unstable_spell())
    if (unstable_spell.__name__ == "unstable_spell"):
        print("Functools.wraps fonctionnel")
    else:
        print("Failed Functools.wraps")
    print("\nTest 4 : Mage Guild")
    a = MageGuild()
    print("Testin casting a spell with 20 power:")
    print(" ", a.cast_spell("Heal", 20))
    if (a.cast_spell.__name__ == "cast_spell"):
        print("  Functools.wraps fonctionnel")
    else:
        print("  Failed Functools.wraps")
    print("Testin casting a spell with 5 power:")
    print(" ", a.cast_spell("Heal", 5))
    if (a.cast_spell.__name__ == "cast_spell"):
        print("  Functools.wraps fonctionnel")
    else:
        print("  Failed Functools.wraps")
    print("Testing mage names")
    mage_names = ['Zara', 'Riley', 'Jo', 'Alex123']
    for i in mage_names:
        print(f"  Mage {i} name is valid:", MageGuild.validate_mage_name(i))


if __name__ == "__main__":
    main()
