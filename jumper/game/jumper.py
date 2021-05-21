class Jumper:
    """A code template for a jumper hanging a guy. The responsibility of 
    this class of objects is to organize the display text.
    
    Stereotype:
        Text organizer

    Attributes:
        lives (int): The number of mistakes the player has left before they lose.
        drawing (list): List of strings that displays the output.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.lives = 5
        self.drawing = [
            r" ___  ",
            r"/___\ ",
            r"\   / ",
            r" \ /  ",
            r"  0   ",
            r" /|\  ",
            r" / \  "
        ]

    def get_output(self):
        """Organizes drawing list into an output string.
        
        Args:
            self (Jumper): an instance of Jumper.

        Returns:
            output_string (string): String that displays the output.
        """
        output_string = f""
        for line in self.drawing:
            output_string += f"{line}\n"
        output_string += "^^^^^^^\n"
        return output_string

    def deduct_life(self):
        """Decreases the lives count and removes a part of the drawing list.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.drawing.pop(0)
        self.lives -= 1

        if self.lives == 0:
            self.drawing.insert(0, "  X   ")

    def is_alive(self):
        """Checks to see if the player is still alive and able to play.
        
        Args:
            self (Jumper): an instance of Jumper.

        Returns:
            True (boolean): if the player is alive.
            False (boolean): if the player is dead.
        """
        if self.lives > 0:
            return True
        else:
            return False
