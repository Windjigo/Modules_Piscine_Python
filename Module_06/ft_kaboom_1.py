import alchemy.grimoire.dark_spellbook


def main():
    print("=== Kaboom 1 ===")
    print("Using grimoire module directly")
    print("Trying to record a dark spell with the right ingredients:",
          alchemy.grimoire.dark_spellbook.dark_spell_record
          ("GOOD", "Earth, wind and fire"))
    print("Trying to record a dark spell with the wrong ingredients:",
          alchemy.grimoire.dark_spellbook.dark_spell_record
          ("EVIL", "bats, frogs and sulphur"))


if __name__ == "__main__":
    main()
