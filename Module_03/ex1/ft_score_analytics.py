import sys


def create_list_params(argv: list[str]) -> list:
    new_list = []
    if (len(argv) == 1):
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
    else:
        for i in range(1, len(argv)):
            try:
                new_list += [int(argv[i])]
            except Exception:
                print("Invalid parameter:", argv[i])
    return new_list


def list_treatment(scores: list) -> None:
    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores)/len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))
    print("")


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = create_list_params(sys.argv)
    if scores == []:
        return
    list_treatment(scores)


if __name__ == "__main__":
    main()
