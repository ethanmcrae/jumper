from game.console import Console
from game.jumper import Jumper
from game.word import Word

from playsound import playsound

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        keep_playing (boolean): Whether or not the game can continue.
        word (Word): An instance of the class of objects known as Word.
        current_guess (string): The last guess made by the player.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
        self.current_guess = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play. When the game
        is over, it plays a corresponding sound and displays the correct word.
        
        Args:
            self (Director): an instance of Director.
        """

        self.do_outputs()

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        self.console.write("The word was: " + self.word.cur_word)

        if self.word.is_win():
            playsound('./assets/win.wav')
        else:
            playsound('./assets/death.mp3')



    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        gets a letter from the player to match the word. Only allows players to
        input letters they haven't guessed yet.

        Args:
            self (Director): An instance of Director.
        """
        self.current_guess = self.console.read_letters("Guess a letter [a-z]: ")

        while self.current_guess in self.word.all_guesses:
            self.current_guess = self.console.read_letters("You already guessed that. Please guess a new letter [a-z]: ")
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, the jumper hangs the man some more, or the new correct letter
        gets displayed.

        Args:
            self (Director): An instance of Director.
        """
        if not self.word.check_letter(self.current_guess):
            self.jumper.deduct_life()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means it displays if the guy is alive or not still 
        along with the word.

        Args:
            self (Director): An instance of Director.
        """
        self.keep_playing = self.jumper.is_alive()
        jumper_drawing = f"{self.word.hidden_word}\n\n" + self.jumper.get_output()
        self.console.write(jumper_drawing)

        if self.word.is_win():
            self.keep_playing = False