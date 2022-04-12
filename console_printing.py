import colorama
import time
from colorama import Fore


def draw_Board(guessed_word):
    print("   - - - -")
    print("   |     |")
    print("   |")
    print("   |")
    print("   |")
    print(" _ _ _", '\t\t', draw_guessed_word(guessed_word))


def draw_guessed_word(guessed_word):
    guessed_word_str = ""
    for letter in guessed_word:
        guessed_word_str += letter + " "

    if " " in guessed_word_str:
        guessed_word_str = guessed_word_str[:-1]

    return guessed_word_str


def print_letter_count(letters):
    print("There are", letters, "letters in this word.")


def refresh(word):
    colorama.init()
    print(Fore.WHITE + "\n" * 50)
    draw_Board(word.get_guessed_word())
    print_letter_count(len(word.get_guessed_word()))


def get_guess(word):
    guess = input("Guess the next letter: ")

    while len(guess) != 1 or not guess.isalpha() or set(word.get_guessed_letters()).__contains__(guess):
        refresh(word)

        if len(guess) != 1:
            print(Fore.RED + "That is not a character...")
        elif not guess.isalpha():
            print(Fore.YELLOW + "That is not a letter...")
        else:
            print(Fore.YELLOW + "You already guessed that...")

        guess = input(Fore.WHITE + "Guess the next letter: ")

    return guess


def correct_guess():
    print(Fore.GREEN + "Congratulations! That letter is in the word!")
    time.sleep(1.5)


def incorrect_guess():
    print(Fore.RED + "Sorry! That guess was incorrect...")
    time.sleep(1.5)


def winning_message():
    print(Fore.GREEN + "\n" * 50)
    print("Amazing! You won!!!")


def losing_message():
    print(Fore.RED + "\n" * 50)
    print("Unfortunate! You lost...\nBetter luck next time!")
