def main():
    try:
        n = int(input("Number: "))

        if n > 0:
            print("The number is positive.")
        elif n == 0:
            print("The number is zero.")
        else:
            print("The number is negative.")

    except ValueError:
        print("Please enter an integer.")


if __name__ == "__main__":
    main()
