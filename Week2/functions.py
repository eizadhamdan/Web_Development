def main():
    num = 10

    for i in range(num):
        print(f"The square of {i} is {square(i)}.")


def square(x):
    return pow(x, 2)


if __name__ == "__main__":
    main()
