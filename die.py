"""
die.py
Implements the Die class
"""

import random

class Die():
    """This class represents a 6-sided die."""

    def __init__(self, sides):
        """constructor for die. "the init method"
        The role of the constructor is to initialize the data of an object,
        "self" is the object itself (that is being initialized).
        """

        # Attribute for the value of the die. _ indicates that it shouldn't
        # be accessed outside of the class
        self._value = None
        self._sides = sides

        self.roll()

    def roll(self):
        """Reset the die's value to a random number"""
        self._value = random.randint(1, self._sides)

    def get_value(self):
        return self._value


def main():

    d1 = Die(1000)
    d2 = Die(20)

    doubles = False
    rolls = 0

    while not doubles:
        rolls += 1
        d1.roll()
        d2.roll()
        print(d1.get_value(), d2.get_value())

        doubles = d1.get_value() == d2.get_value()

    print("It took", rolls, "rolls to get doubles")





main()
