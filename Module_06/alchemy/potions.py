import elements
import alchemy.elements as elements2


def healing_potion():
    return f"Healing potion brewed with '{elements2.create_earth()}' \
and '{elements2.create_air()}'"


def strength_potion():
    return f"Strength potion brewed with '{elements.create_fire()}' \
and '{elements.create_water()}'"
