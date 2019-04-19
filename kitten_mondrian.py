
from cs110graphics import *
import random

class KittenMondrian(EventHandler):
    "Makes paintings like Piet Mondrian."

    def __init__(self, window, x_left, x_right, y_top, y_bottom, depth, images):
        EventHandler.__init__(self)

        self._win = window
        self._x_left = x_left
        self._x_right = x_right
        self._y_top = y_top
        self._y_bottom = y_bottom
        self._depth = depth
        self._images = images

        center = ((x_left + x_right) // 2, (y_top + y_bottom) // 2)
        width = x_right - x_left
        height = y_bottom - y_top

        filename = random.choice(images)
        self._rect = Image(self._win, filename, width, height, center)
        self._rect.set_depth(depth)

        self._rect.add_handler(self)

        self._win.add(self._rect)

    def handle_mouse_press(self, event):

        # This gets the location where the mouse was clicked
        (x_split, y_split) = event.get_mouse_location()

        # If left button clicked, split vertically; if right button, horizontally
        if event.get_button() == "Left Mouse Button":

            KittenMondrian(self._win, self._x_left, x_split, self._y_top, self._y_bottom, self._depth - 1, self._images)
            KittenMondrian(self._win, x_split, self._x_right, self._y_top, self._y_bottom, self._depth - 1, self._images)

        if event.get_button() == "Right Mouse Button":

            KittenMondrian(self._win, self._x_left, self._x_right, self._y_top, y_split, self._depth - 1, self._images)
            KittenMondrian(self._win, self._x_left, self._x_right, y_split, self._y_bottom, self._depth - 1, self._images)

def main(window):

    window.set_width(600)
    window.set_height(600)


    images = []
    for x in range(16):
        filename = "./images/kitten{}.jpg".format(x)
        images.append(filename)

    KittenMondrian(window, 10, 590, 10, 590, 100, images)

if __name__ == "__main__":
    # When using cs110graphics, replace the usual call to main() with this:
    StartGraphicsSystem(main)
