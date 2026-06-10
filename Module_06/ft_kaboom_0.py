import alchemy.grimoire


def main():
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Trying to record light spell with the right ingredients:",
          alchemy.grimoire.light_spell_record("GOOD SPELL",
                                              "Earth, wind and fire"))
    print("Trying to record light spell with the wrong ingredients:",
          alchemy.grimoire.light_spell_record("EVIL SPELL",
                                              "bats, frogs and sulphur"))


if __name__ == "__main__":
    main()
