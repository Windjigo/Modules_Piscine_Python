import typing
import random


def event_generator() -> typing.Generator[tuple, None, None]:
    players = ["Bob", "Alice", "Charlie", "Dylan"]
    action = ["climb", "swim", "fly", "fight", "sleep", "eat"]
    while True:
        yield ((players[random.randint(0, len(players)-1)],
               action[random.randint(0, len(action)-1)]))


def consume_event(lst: list) -> typing.Generator[list, None, None]:
    while lst:
        to_yield = lst[random.randint(0, len(lst)-1)]
        lst.remove(to_yield)
        yield (to_yield)


def main() -> None:
    gen = event_generator()
    lst = []
    print("=== Game Data Stream Processor ===")
    for i in range(1, 1001):
        print("Event", i, ":", "Player", next(gen)[0], "did action", )
    for i in range(10):
        lst += [next(gen)]
    print("\nBuilt list of 10 events:", lst, "\n")
    for event in consume_event(lst):
        print("Got event from list:", event)
        print("Remains in list:", lst)
        print("")


if __name__ == "__main__":
    main()
