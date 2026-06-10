import sys


def print_params(argv: list) -> None:
    print("Program name:", argv[0])
    if (len(argv) == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", len(argv)-1)
        for i in range(1, len(argv)):
            print("Argument", i, ":", argv[i])
    print("Total arguments:", len(argv), "\n")


def main() -> None:
    print("=== Command Quest ===")
    print_params(sys.argv)


if __name__ == "__main__":
    main()
