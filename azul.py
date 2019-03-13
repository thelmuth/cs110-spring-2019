"""
azul.py
This will implement the board game Azul
"""

import random

TILE_COLORS = ["blue", "yellow", "red", "black", "white"]

class Tile:
    """Represents tiles of 5 colors"""

    def __init__(self, color):
        assert color in TILE_COLORS
        self._color = color

    def get_color(self):
        return self._color

    def __str__(self):
        """Returns a human-readable string version of an object.
        This is automatically called when you print an object!"""
        return "<" + self._color + ">"

    def __repr__(self):
        """Like __str__, but is called when Python needs an "unambiguous"
        version of an object"""
        return "<" + self._color + ">"


class Bag:
    """Represents the bag of tiles"""

    def __init__(self):
        """Create a new bag with 100 tiles in it"""
        # Need 100 tiles, 20 of each color, and add them to the bag
        self._bag = []

        for color in TILE_COLORS:
            for _ in range(20):
                tile = Tile(color)
                self._bag.append(tile)

    def __str__(self):
        return "Bag: " + str(self._bag)

    def __len__(self):
        return len(self._bag)

    def random_tile(self):
        """Gets a random tile from the bag and removes it from the bag.
        Can't use random.choice, since it doesn't remove tile from bag."""
        index = random.randint(0, len(self._bag) - 1)

        return self._bag.pop(index)

    def empty(self):
        """Returns true if the bag is empty"""
        return len(self._bag) == 0




def main():

    tile_bag = Bag()

    while not tile_bag.empty():
        print(len(tile_bag))
        t = tile_bag.random_tile()

        print(t)














if __name__ == "__main__":
    main()
