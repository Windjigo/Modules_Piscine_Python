import sys


def main() -> None:
    if (sys.prefix == sys.base_prefix):
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python: /usr/bin/python3.11\nVirtual \
Environment: None detected")
        print("\nWARNING: You're in the global environment!\nThe \
machines can see everything you install")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env\nsource matrix_env/bin/activate \
# On Unix\nmatrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python:", sys.executable)
        data = str(sys.prefix).split("/")
        print("Virtual environment:", data[len(data) - 1])
        print("Environment path:", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!\nSafe \
to install packages without affecting the global system.")
        print("\nPackage installation path:", sys.path[len(sys.path) - 1])


if __name__ == "__main__":
    main()
