import colorama
import time
import utility
from colorama import Fore


def draw_Board(word, guessed_word, man):
    print("   - - - -                   ", end='')
    
    #print out each missed letter
    i = 0;
    while (i < word.missed_letters.length):
        print(word.missed_letters[i])
         
    print("   |     |")
    print("   |     " + Fore.CYAN + man.head())
    print(Fore.WHITE + "   |    " + Fore.CYAN + man.leftArm() + man.abdomen() + man.rightArm())
    print(Fore.WHITE + "   |    " + Fore.CYAN + man.leftLeg() + " " + man.rightLeg())
    print(Fore.WHITE + " _ _ _", '\t\t', draw_guessed_word(guessed_word))


def draw_guessed_word(guessed_word):
    guessed_word_str = ""
    for letter in guessed_word:
        guessed_word_str += letter + " "

    if " " in guessed_word_str:
        guessed_word_str = guessed_word_str[:-1]

    return guessed_word_str


def print_letter_count(letters):
    print("There are", letters, "letters in this word.")


def refresh(word, man):
    colorama.init()
    print(Fore.WHITE + "\n" * 50)
    draw_Board(word, word.get_guessed_word(), man)
    print_letter_count(len(word.get_guessed_word()))


def get_guess(word, man):
    guess = input("Guess the next letter: ")

    while len(guess) != 1 or not guess.isalpha() or set(word.get_guessed_letters()).__contains__(guess):
        refresh(word, man)

        if len(guess) != 1:
            print(Fore.YELLOW + "That is not a character...")
        elif not guess.isalpha():
            print(Fore.YELLOW + "That is not a letter...")
        else:
            print(Fore.YELLOW + "You already guessed that...")

        guess = input(Fore.WHITE + "Guess the next letter: ")

    return guess


def correct_guess():

    print(Fore.GREEN + "Good Job! That letter is in the word!")
    time.sleep(1.5)


def incorrect_guess():
    print(Fore.RED + "Sorry! letter is not in the word...")
    time.sleep(1.5)


def winning_message(word):
    print(Fore.GREEN + "\n" * 50)
    print("Amazing! You won!!!")
    print("The word was", utility.list_to_string(word.get_word()) + "!")


def losing_message(word):
    print(Fore.RED + "\n" * 50)
    print("Unfortunate! You lost...\nBetter luck next time!")
    print("The word was", utility.list_to_string(word.get_word()) + ".")
