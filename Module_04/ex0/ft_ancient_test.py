import sys


def main() -> None:
    print("=== CYBER ARCHIVES RECOVERY\n")
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("Accessing file:", sys.argv[1], "\n")
        fd = open(sys.argv[1], "r")
        print("---")
        print(fd.read())
        print("---")
        fd.close()
        print(f"\nFile {sys.argv[1]} closed.")
    except FileNotFoundError:
        print(f"ERROR: No such file as {sys.argv[1]}.")
    except PermissionError:
        print(f"ERROR: Permission denied for {sys.argv[1]}.\n")


if __name__ == "__main__":
    main()
