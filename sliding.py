
from cs110graphics import *
import random

class Tile(EventHandler):

    def __init__(self, win, width, center):
        EventHandler.__init__(self)

        self._win = win

        self._square = Square(self._win, width, center)
        self._square.set_depth(10)

        self._text = Text(self._win, str(center), 14, center)
        self._text.set_depth(5)

        self._components = [self._square, self._text]

        for component in self._components:
            component.add_handler(self)
            self._win.add(component)

    def handle_mouse_press(self, event):
        # RunWithYieldDelay always takes a wuindow and a method call that
        # will hanble the movement
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        RunWithYieldDelay(self._win, self.slide_tile(random.choice(DIRECTIONS)))

    def slide_tile(self, direction):

        (dx, dy) = direction

        self._square.set_fill_color("white")

        for _ in range(100):
            for component in self._components:
                component.move(dx, dy)

            center = self._square.get_center()
            self._text.set_text(str(center))

            yield 1

        self._square.set_fill_color("yellow")



def main(window):

    window.set_width(600)
    window.set_height(600)
    window.set_background("midnightblue")

    Tile(window, 100, (300, 300))

if __name__ == "__main__":
    # When using cs110graphics, replace the usual call to main() with this:
    StartGraphicsSystem(main)
