from cs110graphics import *
import random

WIDTH_AND_HEIGHT = 800

class Cheese(EventHandler):
    def __init__(self, win):
        EventHandler.__init__(self)
        self._win = win

        self._space = Rectangle(self._win, WIDTH_AND_HEIGHT, WIDTH_AND_HEIGHT,
                                (WIDTH_AND_HEIGHT // 2, WIDTH_AND_HEIGHT // 2))

        self._space.set_fill_color("lightyellow")
        self._space.add_handler(self)
        self._space.set_depth(100)
        self._win.add(self._space)

        self._circles = 0
        self._list_of_circles = []

    # Fill in the handle_mouse_press method so that each time the user clicks
    # on the Space object, a new circle with radius of 10 appears where the user clicked.
    def handle_mouse_press(self, event):

        self._circles += 1

        center = event.get_mouse_location()
        c = Circle(self._win, 10, center)
        self._win.add(c)

        RunWithYieldDelay(self._win, self.animate_circle(c))
        self._list_of_circles.append(c)

        if self._circles > 5:
            self._win.remove(self._list_of_circles.pop(0))

    def animate_circle(self, circle):

        max_radius = random.randint(20, 100)

        for radius in range(10, max_radius):
            circle.set_radius(radius)

            yield 1


def main(window):
    window.set_width(WIDTH_AND_HEIGHT)
    window.set_height(WIDTH_AND_HEIGHT)

    Cheese(window)


if __name__ == "__main__":
    StartGraphicsSystem(main)
