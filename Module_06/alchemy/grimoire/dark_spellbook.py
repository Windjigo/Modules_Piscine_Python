from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if (validate_ingredients(ingredients).split("-")[1] == " VALID"):
        return (f"{spell_name} RECORDED")
    return (f"{spell_name} REJECTED")
