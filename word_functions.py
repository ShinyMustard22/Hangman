import random
import utility


def generateWord(letters):
    if letters == 4:
        word_file = open("words/fourLetterWords.txt", "r")

    elif letters == 5:
        word_file = open("words/fiveLetterWords.txt", "r")

    elif letters == 6:
        word_file = open("words/sixLetterWords.txt", "r")

    else:
        word_file = open("words/sevenLetterWords.txt", "r")

    word = word_file.readlines()[random.randint(0, utility.file_len(word_file.name) - 1)]
    word_file.close()

    word_list = list(word)
    word_list.pop(len(word_list) - 1)

    return word_list
