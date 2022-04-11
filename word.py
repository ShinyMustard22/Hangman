import random
import utility


class Word:
    def __init__(self, letters):
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

        self.__word_list = word_list

    def check_letter(self, letter, guessed_word):
        contains_letter = False

        for i in range(len(self.__word_list)):
            if self.__word_list[i] == letter:
                contains_letter = True
                guessed_word[i] = letter

        return contains_letter

    @property
    def _word_list(self):
        return self.__word_list

    word_list = property(get_age())
