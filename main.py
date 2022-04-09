import random
from man import Man


def drawGallows():
    print("  -----")
    print("  |   |")
    print("  |")
    print("  |")
    print("  |")
    print("-----")


def main():
    man = Man()
    rand = random.randint(4, 7)

    word = ['_'] * rand


if __name__ == "__main__":
    main()
