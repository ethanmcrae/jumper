from random import choice

class Word:

    """
        Handles generating the secret word, and checking if inputs
        are in that word.

        Stereotype:
            Service Provider, information holder

        Attributes:
            cur_word: The secret word to guess
            hidden_word: Holds the current guessed letters in order,
                         seperated by underscores. To begin, it is just underscores.
            all_guesses: A list of all letters that have been guessed
            hidden_word_list: An array of all hidden_word characters
            cur_word_list: An array of all cur_word characters


    """

    def __init__(self):

        """
            The class constructor
        """

        with open('./assets/Dicitonary', 'r') as f:
            all_words = f.read().split("\n")

        self.cur_word = choice(all_words).lower() # "foo".lower()
        self.hidden_word = ""

        self.all_guesses = []
        self.hidden_word_list = []
        self.cur_word_list = []

        for underscore in range(len(self.cur_word)):
            self.hidden_word += "_"
            self.hidden_word_list.append("_")


        for letter in self.cur_word:
            self.cur_word_list.append(letter)



    def check_letter(self, letter):

        """
            Checks if an inputted letter is in the word. If
            it takes hidden_word_list, then it replaces
            the underscores at those indexes with the letters.

            It also updates hidden_word and all_guesses

            Finally, it returns True if the letter was correct,
            and false if it was incorrect.

            Args:
                The letter to guess

        """

        letter = letter.lower()

        self.all_guesses.append(letter)

        if letter in self.cur_word:

            indexes = [index for index, element in enumerate(self.cur_word_list) if element == letter]

            for index in indexes:
                self.hidden_word_list[index] = letter

            # updates self.hidden_word
            self.hidden_word = ""

            for letter in self.hidden_word_list:
                self.hidden_word += letter

            return True

        else:
            return False


    def get_output(self):
        """
            Returns the current status of hidden word
        """
        return self.hidden_word

    def is_win(self):

        """
            Checks if the user was won or not, based
            on it all characters have been guessed.
        :return:
            True if all letters have been guessed
            False if there are still letters to be guessed.
        """

        if "_" in self.hidden_word_list:
            return False
        else:
            return True

