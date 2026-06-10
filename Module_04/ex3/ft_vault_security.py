from typing import Optional


def secure_archive(file_name: str, op: Optional[str] = None,
                   to_write: Optional[str] = None) -> tuple[bool, str]:
    if (op == "read" or op is None):
        try:
            with open(file_name, "r") as fd:
                read = fd.read()
            return (True, read)
        except Exception as obj:
            return (False, str(obj))
    elif (op == "write"):
        try:
            with open(file_name, "w") as fd:
                fd.write(str(to_write))
            return (True, 'Content successfully written to file')
        except Exception as obj:
            return (False, str(obj))
    else:
        return (False, "The operation to perform doesn't exist")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    file_read = secure_archive("ancient_fragment.txt", "read")
    print(file_read)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("test2", "write", file_read[1]))


if __name__ == "__main__":
    main()
