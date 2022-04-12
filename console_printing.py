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
    # clear the screen
    draw_Board(word.get_guessed_word())
    print_letter_count(len(word.get_guessed_word()))


def get_guess(word):
    guess = input("Guess the next letter: ")

    while len(guess) != 1 or not guess.isalpha() or set(word.get_guessed_letters()).__contains__(guess):
        refresh(word)

        if len(guess) != 1:
            print("That is not a character...")
        elif not guess.isalpha():
            print("That is not a letter...")
        else:
            print("You already guessed that...")

        guess = input("Guess the next letter: ")

    return guess
