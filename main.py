import random
from man import Man


def drawGallows():
    print("  -----")
    print("  |   |")
    print("  |")
    print("  |")
    print("  |")
    print("-----")


def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def generateWord(letters):
    if letters == 4:
        word_file = open("words/fourLetterWords.txt", "r")

    elif letters == 5:
        word_file = open("words/fiveLetterWords.txt", "r")

    elif letters == 6:
        word_file = open("words/sixLetterWords.txt", "r")

    else:
        word_file = open("words/sevenLetterWords.txt", "r")

    word = word_file.readlines()[random.randint(0, file_len(word_file.name) - 1)]
    word_file.close()

    word_list = list(word)
    word_list.pop(len(word_list) - 1)

    return word_list


def main():
    man = Man()
    letters = random.randint(4, 7)

    guessed_word = ['_'] * letters
    actual_word = generateWord(letters)

    print(guessed_word)
    print(actual_word)


if __name__ == "__main__":
    main()
