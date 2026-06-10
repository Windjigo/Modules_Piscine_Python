from .light_spellbook import light_spell_record
from .light_spellbook import light_spell_allowed_ingredients


def fix_flake8():
    light_spell_allowed_ingredients()
    light_spell_record()
