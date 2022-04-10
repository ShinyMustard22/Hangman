import console_printing
import random
import word_functions
from man import Man


def main():
    man = Man()
    letters = random.randint(4, 7)

    guessed_word = ['_'] * letters
    actual_word = word_functions.generateWord(letters)

    console_printing.drawGallows()


if __name__ == "__main__":
    main()
