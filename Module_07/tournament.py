import ex0
import ex1
import ex2


def battle(list: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]]) -> None:
    print(f"*** Tournament ***\n{len(list)} opponents involved")
    for i in list:
        opp1 = i[0].create_base()
        for j in list:
            try:
                if (j != i):
                    print("\n   *Battle*")
                    opp2 = j[0].create_base()
                    opp1.describe()
                    print(" vs.")
                    opp2.describe()
                    print(" now fight!")
                    if (i[1].is_valid(opp1) is True):
                        i[1].act(opp1)
                    else:
                        list.remove(i)
                        raise Exception(f"{opp1.name} is \
disqualified for its illegal moveset")
                    if (j[1].is_valid(opp2) is True):
                        j[1].act(opp2)
                    else:
                        list.remove(j)
                        raise Exception(f"{opp2.name} is \
disqualified for its illegal moveset")
            except Exception as obj:
                print(obj)
        list.pop(0)


def main() -> None:
    fire = ex0.FlameFactory()
    water = ex0.WaterFactory()
    heal = ex1.HealingCreatureFactory()
    trans = ex1.TransformingCreatureFactory()
    defense = ex2.DefensiveStrategy()
    aggr = ex2.AggressiveStrategy()
    normal = ex2.NormalStrategy()
    print("Tournament 0 (basic)")
    print("List of opponents: [(Flameling+Normal), (Sproutling+Defensive)])")
    battle([(fire, normal), (heal, defense)])
    print("\nTournament 1 (error)")
    print("List of opponents: [(Flameling+Aggressive), \
(Sproutling+Defensive)])")
    battle([(fire, aggr), (heal, defense)])
    print("\nTournament 2 (multiples)")
    print("List of opponents: [(Aquabub+Normal), \
(Sproutling+Defensive), (Shiftling+Aggressive)]")
    battle([(water, normal), (heal, defense), (trans, aggr)])


if __name__ == "__main__":
    main()
