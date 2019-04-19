from cs110graphics import *
import random

WIDTH_AND_HEIGHT = 800

class Space(EventHandler):
    def __init__(self, win):
        EventHandler.__init__(self)
        self._win = win

        self._clicks = 0

        self._space = Rectangle(self._win, WIDTH_AND_HEIGHT, WIDTH_AND_HEIGHT,
                                (WIDTH_AND_HEIGHT // 2, WIDTH_AND_HEIGHT // 2))

        self._space.set_fill_color("lightyellow")
        self._space.add_handler(self)
        self._space.set_depth(100)
        self._win.add(self._space)

    # Fill in the handle_mouse_press method so that each time the user clicks
    # on the Space object, a new circle with radius of 10 appears where the user clicked.
    def handle_mouse_press(self, event):

        self._clicks += 1
        if self._clicks <= 5:
            loc = event.get_mouse_location()
            c = Circle(self._win, 10, loc)
            self._win.add(c)

            RunWithYieldDelay(self._win, self.make_circle_bigger(c))

    def make_circle_bigger(self, circle):

        radius = 10

        max_radius = random.randint(20, 100)

        while radius < max_radius:
            radius += 1
            circle.set_radius(radius)

            yield 1



def main(window):
    window.set_width(WIDTH_AND_HEIGHT)
    window.set_height(WIDTH_AND_HEIGHT)

    Space(window)


if __name__ == "__main__":
    StartGraphicsSystem(main)
