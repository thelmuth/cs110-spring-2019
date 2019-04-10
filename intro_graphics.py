
from cs110graphics import *


class Light(EventHandler):
    """ A light is a circle graphic that can change color."""

    def __init__(self, win, rad, cen):
        EventHandler.__init__(self)

        self._win = win
        self._radius = rad
        self._center = cen

        self._colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self._color_index = 0
        self._color = self._colors[self._color_index]

        self._circle = Circle(self._win, self._radius, self._center)
        self._circle.set_fill_color(self._color)
        self._circle.set_border_color(self._color)
        self._circle.set_depth(10)

        self._circle.add_handler(self)

        self._win.add(self._circle)

    def handle_mouse_press(self, event):
        """This method is called when the circle is clicked on."""

        self._color_index = (self._color_index + 1) % len(self._colors)
        self._color = self._colors[self._color_index]
        self._circle.set_fill_color(self._color)
        self._circle.set_border_color(self._color)

class Light2(Light):

    def __init__(self, win, rad, cen):
        Light.__init__(self, win, rad, cen)

        self._colors = ["brown", "black", "grey", "white", "tan", "pink", "beige"]
        self._color = self._colors[self._color_index]
        self._circle.set_fill_color(self._color)
        self._circle.set_border_color(self._color)

        self._circle.set_depth(2)

def main(window):

    window.set_width(600)
    window.set_height(600)

    first_circle = Circle(window, 30, (300, 200))
    first_circle.set_fill_color("cyan")
    first_circle.set_depth(15)
    window.add(first_circle)

    light1 = Light(window, 50, (100, 100))
    light2 = Light(window, 90, (400, 200))
    light3 = Light(window, 75, (600, 600))

    new_light = Light2(window, 35, (60, 60))











if __name__ == "__main__":
    # When using cs110graphics, replace the usual line with this one:
    StartGraphicsSystem(main)
