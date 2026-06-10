from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for x in ingredients.split(" "):
        for y in dark_spell_allowed_ingredients():
            x = str(x).replace(",", "")
            if (x.lower() == y.lower()):
                return (str(ingredients) + "- VALID")
    return (str(ingredients) + "- INVALID")
