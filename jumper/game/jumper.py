import random
#from game.word import Word

class Jumper:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        hunter (Hunter): An instance of the class of objects known as Hunter.
        rabbit (Rabbit): An instance of the class of objects known as Rabbit.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.lives = 5
        self.word = Word()
        self.drawing = [
            r" ___  ",  # 0
            r"/___\ ",  # 1
            r"\   / ",  # 2
            r" \ /  ",  # 3
            r"  0   ",  # 4
            r" /|\  ",  # 5
            r" / \  "  #  6
        ]

    def get_output(self):
        output_string = f"{self.word.cur_word}\n"
        for line in self.drawing:
            output_string += f"{line}\n"
        output_string += "^^^^^^^\n"
        return output_string

    def deduct_life(self):
        self.drawing.remove(0)
        self.lives -= 1

        if self.lives == 0:
            self.drawing.insert(0, "  X   ")

        if len(self.drawing) == 3:
            self.drawing.insert("  X   ")
