import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===\n")
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("Accessing file:", sys.argv[1], "\n")
        fd = open(sys.argv[1], "r")
        print("---")
        read = fd.read()
        print(read)
        print("---")
        fd.close()
        print(f"\nFile {sys.argv[1]} closed.")
    except FileNotFoundError:
        sys.stderr.write(f"[STDERR] ERROR: No such file as {sys.argv[1]}.\n")
        return
    except PermissionError:
        sys.stderr.write(f"[STDERR] ERROR: \
Permission denied for {sys.argv[1]}.\n")
        return
    read = read.replace("\n", "#\n")
    read = read + "#"
    print("\nTransform data:\n")
    print("---")
    print(read)
    print("---")
    print("\nEnter new file name \
(Leave this empty if you do not intend to save the transformed file): ")
    new_file = sys.stdin.readline().strip()
    if (new_file != ""):
        try:
            print(f"Saving data to {new_file}")
            fd = open(new_file, "w")
            fd.write(read)
            print(f"Data saved in file {new_file}.")
        except Exception as obj:
            sys.stderr.write(f"[STDERR] ERROR: {obj}.\n")
        finally:
            fd.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
