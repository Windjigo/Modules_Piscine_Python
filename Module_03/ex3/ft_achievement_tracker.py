import random


def get_player_achievement() -> set:
    total_achievements = set(['Crafting Genius', 'Strategist',
                              'World Savior', 'Speed Runner',
                              'Survivor', 'Master Explorer',
                              'Treasure Hunter', 'Unstoppable',
                              'First Steps', 'Collector Supreme',
                              'Untouchable', 'Sharp Mind',
                              'Boss Slayer'])
    player_achievement: set[str] = set()
    for i in total_achievements:
        x = random.randint(0, 4)
        if (player_achievement.intersection(i) == set() and x < 3):
            player_achievement.add(i)
    return (player_achievement)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    Alice = get_player_achievement()
    Bob = get_player_achievement()
    Charlie = get_player_achievement()
    Dylan = get_player_achievement()
    all = Alice.union(Bob.union(Charlie.union(Dylan)))
    print("Player Alice:", Alice)
    print("Player Bob:", Bob)
    print("Player Charlie:", Charlie)
    print("Player Dylan:", Dylan)
    print("\nAll distinct achievement :", all)
    print("\nCommon achievements :", Alice.intersection(
        Bob.intersection(Charlie.intersection(Dylan))))
    print("\nOnly Alice has:", Alice.difference(
        Bob.union(Charlie.union(Dylan))))
    print("Only Bob has:", Bob.difference(Alice.union(Charlie.union(Dylan))))
    print("Only Charlie has:", Charlie.difference(
        Alice.union(Bob.union(Dylan))))
    print("Only Dylan has:", Dylan.difference(Alice.union(Charlie.union(Bob))))
    print("\nAlice is missing:", all.difference(Alice))
    print("Bob is missing:", all.difference(Bob))
    print("Charlie is missing:", all.difference(Charlie))
    print("Dylan is missing:", all.difference(Dylan))


if __name__ == "__main__":
    main()
