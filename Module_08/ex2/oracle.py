from dotenv import load_dotenv
import os


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    load_dotenv()
    liste = ["MATRIX_MODE", "DATABASE_URL",
             "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    liste2 = []
    listLoglevel = ["Trace", "Debug", "Information",
                    "Warning", "Error", "Critical", "None"]
    test = 0
    try:
        for i in liste:
            liste2 += [os.getenv(f'{i}')]
    except Exception:
        print("Error while getting the environmental \
variable. Please retry or change their values")
        return
    for i in range(len(liste2)):
        if (liste2[i] is None):
            liste2[i] = "Missing"
    if (liste2[0] == 'development'):
        for i in range(len(liste)):
            if (i != 3):
                print(f"{liste[i]} : {liste2[i]}")
            else:
                for i in range(len(listLoglevel)):
                    if (str(i) == liste2[3]):
                        test += 1
                        print(f"Log Level : {listLoglevel[i]}")
                if (test == 0):
                    print("Log Level : Invalid")
    elif (liste2[0] == 'production'):
        print(f"{liste[0]} : production")
        if (liste2[1] != "Missing"):
            print(f"{liste[1]} : Connected to local instance")
        else:
            print(f"{liste[1]} : Not found")
        if (liste2[2] == 'test123'):
            print("API Access : Authenticated")
        else:
            print("API Access : Access refused")
        test = 0
        for i in range(len(listLoglevel)):
            if (str(i) == liste2[3]):
                test += 1
                if (i == 0):
                    print("Log Level : Trace forbidden in production mode")
                else:
                    print(f"Log Level : {listLoglevel[i]}")
        if (test == 0):
            print("Log Level : Invalid")
        if (liste2[4] != "Missing"):
            print("Zion Network: Online")
        else:
            print("Zion Network: Not found")
    else:
        print("Invalid Mode given.\nStopping the program")


if __name__ == "__main__":
    main()
