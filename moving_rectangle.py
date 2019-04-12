
from cs110graphics import *

class MovingRectangle(EventHandler):
    """A rectangle that moves to the right when you click it."""

    def __init__(self, window, width, length, center):
        EventHandler.__init__(self)

        self._window = window
        self._center = center

        self._rect = Rectangle(self._window, width, length, self._center)
        self._rect.set_fill_color("teal")

        self._rect.add_handler(self)

        self._window.add(self._rect)

    def handle_mouse_press(self, event):

        ### This is one way to do it
        # (x, y) = self._center
        # self._center = (x + 20, y)
        #
        # self._rect.move_to(self._center)

        self._rect.move(20, 5)

def main(window):

    window.set_width(600)
    window.set_height(600)

    r = MovingRectangle(window, 100, 40, (100, 300))


if __name__ == "__main__":
    # When using cs110graphics, replace the usual call to main() with this:
    StartGraphicsSystem(main)
