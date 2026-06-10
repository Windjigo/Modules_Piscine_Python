from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if (validate_ingredients(ingredients).split("-")[1] == " VALID"):
        return (f"{spell_name} RECORDED")
    return (f"{spell_name} REJECTED")
