from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
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
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
        self.current_guess = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the hunter to a new location.

        Args:
            self (Director): An instance of Director.
        """
        # message = self.hunter.get_message()
        # self.console.write(message)
        # location = self.console.read_number("Enter a location [1-1000]: ")
        # if location: self.hunter.move(location)
        self.current_guess = self.console.read_letters("Guess a letter [a-z]: ")
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the rabbit watches the hunter.

        Args:
            self (Director): An instance of Director.
        """
        # self.rabbit.watch(self.hunter.location)
        if not self.word.check_letter(self.current_guess):
            self.jumper.deduct_life()
        
        # self.jumper.update()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the rabbit provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        # hint = self.rabbit.get_hint()
        # self.console.write(hint)
        # self.keep_playing = (self.rabbit.distance[-1] != 0)
        self.keep_playing = self.jumper.is_alive()
        jumper_drawing = self.jumper.get_output()
        self.console.write(jumper_drawing)