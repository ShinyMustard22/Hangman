# import os


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


def print_letter_count(guessed_word):
    print("There are", len(guessed_word), "letters in this word.")


def refresh(guessed_word):
    # clear the screen
    draw_Board(guessed_word)
    print_letter_count(guessed_word)
