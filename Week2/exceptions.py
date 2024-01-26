import sys


def main():
    try:
        x = int(input("X: "))
        y = int(input("Y: "))

        try:
            result = x / y
            print(f"{x} divided by {y} is {result}.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")
            sys.exit(1)

    except ValueError:
        print("Please provide an integer input.")
        sys.exit(1)


if __name__ == "__main__":
    main()
