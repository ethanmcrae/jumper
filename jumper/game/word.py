class Word:

    def __init__(self):

        self.cur_word = "foo".lower()
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
        return self.hidden_word

    def is_win(self):

        if "_" in self.hidden_word_list:
            return False
        else:
            return True


if __name__ == "__main__":
    wd = Word()
    wd.check_letter("o")
    wd.check_letter('F')
