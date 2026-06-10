import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    lst1 = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
            'Gregory', 'john', 'kevin', 'Liam']
    lst_capitalized = [x.capitalize() for x in lst1]
    lst_filtered = [x for x in lst1 if x[0].isupper()]
    print("Initial list of players:", lst1)
    print("New list with all names capitalized:", lst_capitalized)
    print("New list of capitalized names only:", lst_filtered)
    dico = {x: random.randint(50, 1000) for x in lst_capitalized}
    dico_high_score = {x: dico[x] for x in lst_capitalized if dico[x] > 500}
    print("Score dict:", dico)
    print("Score average is", sum(dico.values())/len(dico))
    print("High scores:", dico_high_score)


if __name__ == "__main__":
    main()
