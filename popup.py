
from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

class Counter(EventHandler):

    def __init__(self, win, center, message):
        EventHandler.__init__(self)

        self._win = win
        self._center = center
        self._message = message

        self._count = 0
        self._clickable = True

        self._circ = Circle(self._win, 75, center)
        self._circ.set_fill_color("gold")
        self._circ.set_depth(50)
        self._circ.add_handler(self)
        self._win.add(self._circ)

        self._text = Text(self._win, str(self._count), 20, center)
        self._text.set_depth(20)
        self._text.add_handler(self)
        self._win.add(self._text)


    def handle_mouse_press(self, event):

        if self._clickable:
            self._count += 1
            self._text.set_text(str(self._count))

            if self._count % 5 == 0:
                self.toggle_clickable()
                Popup(self._win, self, (WIN_WIDTH // 2, WIN_HEIGHT // 2), self._message)

    def toggle_clickable(self):
        self._clickable = not self._clickable


class Popup(EventHandler):
    """Makes a popup window that let's you click an "ok" button."""

    # This is a class variable: variable that is accessible to every instance
    # of the class. You use it within the class using: Popup.top_depth
    top_depth = 10

    def __init__(self, win, counter, center, message):
        EventHandler.__init__(self)

        self._win = win
        self._counter = counter

        (x, y) = center

        self._popup_window = Rectangle(self._win, 140, 100, center)
        self._popup_window.set_fill_color("tomato")

        self._message = Text(self._win, message, 14, (x, y - 25))

        self._ok_button = Rectangle(self._win, 40, 30, (x, y + 25))
        self._ok_button.set_fill_color("turquoise")
        self._ok_button.add_handler(self)

        self._ok_text = Text(self._win, "ok", 16, (x, y + 25))
        self._ok_text.add_handler(self)

        self._components = [self._popup_window, self._message, self._ok_button,
                            self._ok_text]

        for component in self._components:
            component.set_depth(Popup.top_depth)
            Popup.top_depth -= 1 # changing top_depth to be closer to us

            self._win.add(component)

    def handle_mouse_press(self, event):

        self._counter.toggle_clickable()
        # Remove the popup window
        for component in self._components:
            self._win.remove(component)



def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    Counter(win, (200, 200), "This is the\nfirst counter!")
    Counter(win, (400, 200), "This is the\nsecond counter!")


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
