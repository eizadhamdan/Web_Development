def main():
    name = "Harry"

    print(name[0], name[1])

    names = ["Harry", "Ron", "Hermione"]

    print(*names, sep=", ")
    print(names[1])

    coordinateX = 10.0
    coordinateY = 20.0
    # tuple can be used here
    coordinate = 10.0, 20.0
    print(coordinate)


if __name__ == "__main__":
    main()
