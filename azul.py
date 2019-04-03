"""
azul.py
This will implement the board game Azul
"""

import random

TILE_COLORS = ["blue", "yellow", "red", "black", "white"]


class Azul:
    """Represent the entire game of Azul"""

    def __init__(self):

        # For now, assume a 2-player game
        self._number_of_players = 2
        NUMBER_OF_FACTORIES = 5

        # Store the player names in a list
        self._player_names = []
        for x in range(self._number_of_players):
            player = input("Enter name of player {}: ".format(x + 1))
            self._player_names.append(player)

        self._current_player = 0

        self._bag = Bag()

        # Create the factories
        self._factories = []
        for _ in range(NUMBER_OF_FACTORIES):
            self._factories.append(Factory())


    def __str__(self):
        """ We want this to look like:
        ----- Azul -----
        0. Factory with tiles: [<white>, <red>, <black>]
        1. Factory with tiles: []
        2. Factory ...
        """

        result = "----- Azul -----\n"
        for index in range(len(self._factories)):
            result += str(index) + ". " + str(self._factories[index]) + "\n"

        return result

    def play_game(self):
        """Controls the entire game of Azul, from beginning to end."""

        self.begin_round()

        # NOTE: We'll later change this condition to stop when the round ends
        while True:

            self.take_turn()


    def take_turn(self):
        """Let's current player take one turn."""
        
        print(self)

        # For now, let's just have one player take one turn
        factory_number = int(input("{}, which factory do you want to pick from: ".format(self._player_names[self._current_player])))
        color = input("What color tiles do you want to take: ")

        taken_tiles = self._factories[factory_number].take_all_one_color(color)

        print()
        print("You now have the tiles {}, and the game looks like:".format(taken_tiles))

        self._current_player = (self._current_player + 1) % self._number_of_players

    def begin_round(self):
        """Called at the start of each round to add tiles to the factories."""

        for fact in self._factories:
            for _ in range(4):
                t = self._bag.random_tile()
                fact.add_tile(t)



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


class Factory:
    """Represents the factories in Azul"""

    def __init__(self):
        self._my_tiles = []

    def add_tile(self, tile):
        """Adds a tile to the factory"""
        self._my_tiles.append(tile)

    def __str__(self):
        return "Factory with tiles: " + str(self._my_tiles)

    def take_all_one_color(self, color):
        """Remove and return all tiles of specified color from factory."""
        return_list = []
        retain_list = []

        for tile in self._my_tiles:
            if tile.get_color() == color:
                return_list.append(tile)
            else:
                retain_list.append(tile)

        # print(return_list)
        # print(retain_list)

        self._my_tiles = retain_list

        return return_list


def main():

    game = Azul()

    game.play_game()


    # tile_bag = Bag()
    #
    # factory1 = Factory()
    #
    # for _ in range(4):
    #     tile = tile_bag.random_tile()
    #     factory1.add_tile(tile)
    #
    # print(factory1)
    #
    # color = input("Enter a color you want take from this factory: ")
    #
    # users_tiles = factory1.take_all_one_color(color)
    # print()
    # print("User's tiles: ", users_tiles)
    # print(factory1)









if __name__ == "__main__":
    main()
