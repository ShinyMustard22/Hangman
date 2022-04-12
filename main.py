import random
from word import Word
from man import Man
import console_printing


def main():
    letters = random.randint(4, 7)

    word = Word(letters)
    man = Man()

    while not man.isHanged() and not word.if_won():
        console_printing.refresh(word)
        guess = console_printing.get_guess(word)
        word.check_letter(guess)

if __name__ == "__main__":
    main()
