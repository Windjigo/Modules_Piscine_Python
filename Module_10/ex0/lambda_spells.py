def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"*{x}*", spells))


def mages_stats(mages: list[dict]) -> dict:
    return {"max_power":
            max(list(map(lambda x: x["power"], mages))),
            "min_power":
            min(list(map(lambda x: x["power"], mages))),
            "avg_power":
            round(sum(list(map(lambda x: x["power"], mages)))
                  / len(mages), 2)}


def main() -> None:
    print("\n======== Lambda spells =======\n\n")
    print("Testing artefact_sorter:\n")
    artifacts = [{'name': 'Ice Wand', 'power': 97, 'type': 'armor'},
                 {'name': 'Water Chalice', 'power': 95, 'type': 'accessory'},
                 {'name': 'Fire Staff', 'power': 70, 'type': 'weapon'},
                 {'name': 'Water Chalice', 'power': 119, 'type': 'accessory'},
                 {'name': 'Shadow Blade', 'power': 63, 'type': 'weapon'}]
    print(f"Original artifact list:\n{artifacts}\n")
    print(f"Sorted artifact list:\n{artifact_sorter(artifacts)}\n")
    print("======================================\n")
    print("Testing power_filter:\n")
    mages = [{'name': 'Casey', 'power': 69, 'element': 'wind'},
             {'name': 'River', 'power': 53, 'element': 'earth'},
             {'name': 'River', 'power': 56, 'element': 'earth'},
             {'name': 'Sage', 'power': 85, 'element': 'lightning'},
             {'name': 'Jordan', 'power': 50, 'element': 'fire'},
             {'name': 'Alex', 'power': 53, 'element': 'shadow'},
             {'name': 'Jordan', 'power': 97, 'element': 'wind'}]
    print(f"Original mage list:\n{mages}\n")
    print(f"Filtered mage list:\n{power_filter(mages, 70)}\n")
    print("======================================\n")
    print("Testing spell_transformer:\n")
    spells = ['lightning', 'tsunami', 'shield', 'meteor', 'fireball', 'heal']
    print(f"Original spell list:\n{spells}\n")
    print(f"Transformed spell list:\n{spell_transformer(spells)}\n")
    print("======================================\n")
    print("Testing mages_stats:\n")
    print(f"Mage list:\n{mages}\n")
    print(f"Statistics for the list:\n{mages_stats(mages)}")


if __name__ == "__main__":
    main()
