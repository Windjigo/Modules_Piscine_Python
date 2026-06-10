import elements
from .. import create_air
from .. import potions


def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' \
and '{potions.strength_potion()}' mixed with \
'{elements.create_fire()}'"
