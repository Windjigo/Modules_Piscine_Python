import alchemy.grimoire


def validate_ingredients(ingredients: str) -> str:
    for x in ingredients.split(" "):
        for y in alchemy.grimoire.light_spell_allowed_ingredients():
            x = str(x).replace(",", "")
            if (x.lower() == y.lower()):
                return (str(ingredients) + "- VALID")
    return (str(ingredients) + "- INVALID")
