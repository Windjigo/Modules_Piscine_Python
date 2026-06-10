def recursive(x: int, count: int) -> None:
    if (x == count):
        print("Day ", x, "\nHarvest time!")
    else:
        print("Day ", x)
        x += 1
        recursive(x, count)


def ft_count_harvest_recursive() -> None:
    count = int(input("Days until harvest: "))
    recursive(1, count)
