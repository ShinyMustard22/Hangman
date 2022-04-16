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

        word_string = word_file.readlines()[random.randint(0, utility.file_len(word_file.name) - 1)]
        word_file.close()

        word = list(word_string)
        word = word[:-1]

        self.__word = word
        self.__guessed_word = ["_"] * letters
        self.__guessed_letters = set([])

    def check_letter(self, letter):
        contains_letter = False

        for i in range(len(self.__word)):
            if self.__word[i] == letter:
                contains_letter = True
                self.__guessed_word[i] = letter
        
        if contains_letter == False:
            self.__missed_letters.append(letter)

        self.__guessed_letters.add(letter)
        return contains_letter

    def if_won(self):
        return self.__guessed_word == self.__word

    def get_guessed_word(self):
        return self.__guessed_word

    def get_word(self):
        return self.__word

    def get_guessed_letters(self):
        return self.__guessed_letters
