import math


def get_player_pos() -> tuple:
    pre_coords = input("Enter new coordinates as floats in format 'x,y,z': ")
    coords = pre_coords.split(",")
    i = 1
    try:
        if (len(coords) > 3):
            raise TypeError("Too many parameters (Need 3)")
        if (len(coords) < 3):
            raise TypeError("Not enough parameters (Need 3)")
        x = float(coords[0])
        i += 1
        y = float(coords[1])
        i += 1
        z = float(coords[2])
        final_coords = (x, y, z)
        return final_coords
    except Exception as obj:
        if (len(coords) != 3):
            print(obj)
        else:
            print("Error on parameter", i, ": could not convert \
                  string to float")
        return (get_player_pos())


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coords1 = get_player_pos()
    print("Got a first tuple:", coords1)
    print("It includes: X=", coords1[0], ", Y=",
          coords1[1], ", Z=", coords1[2])
    print("Distance to center:",
          round(math.sqrt(coords1[0]**2 + coords1[1]**2 + coords1[2]**2), 4))
    print("\nGet a second set of coordinates")
    coords2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          round(math.sqrt(
              (coords2[0] - coords1[0])**2 +
              (coords2[1] - coords1[1])**2 +
              (coords2[2] - coords1[2])**2), 4))


if __name__ == "__main__":
    main()
