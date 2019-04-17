
from cs110graphics import *

class Car:
    """A car that the user can control around the screen."""

    def __init__(self, window, center, color):

        self._window = window
        self._center = center

        self._width = 20
        self._length = 60
        self._distance = 25

        self._heading_x = 0
        self._heading_y = -1

        self._body = Rectangle(self._window, self._width, self._length, center)
        self._body.set_fill_color(color)
        self._body.set_depth(10)

        self._window.add(self._body)

        self._light1_center = (center[0] - 4, center[1] - 26)
        self._light2_center = (center[0] + 4, center[1] - 26)

        self._light1 = Circle(self._window, 3, self._light1_center)
        self._light2 = Circle(self._window, 3, self._light2_center)
        self._light1.set_depth(5)
        self._light2.set_depth(5)

        self._window.add(self._light1)
        self._window.add(self._light2)

        self._components = [self._body, self._light1, self._light2]

        self._left_button = Button(self._window, self, (25, 50), "left")
        self._right_button = Button(self._window, self, (75, 50), "right")
        self._forward_button = Button(self._window, self, (50, 25), "forward")
        self._backward_button = Button(self._window, self, (50, 75), "backward")

    def move_car(self, direction):
        """Moves the car in the given direction."""

        if direction == "forward":
            change_x = self._heading_x * self._distance
            change_y = self._heading_y * self._distance

            for component in self._components:
                component.move(change_x, change_y)

        elif direction == "backward":
            change_x = self._heading_x * self._distance * -1
            change_y = self._heading_y * self._distance * -1

            for component in self._components:
                component.move(change_x, change_y)

        elif direction == "right":
            old_heading_x = self._heading_x
            self._heading_x = self._heading_y * -1
            self._heading_y = old_heading_x

            pivot = self._body.get_pivot()

            for component in self._components:
                component.set_pivot(pivot)
                component.rotate(-90)

        elif direction == "left":
            old_heading_x = self._heading_x
            self._heading_x = self._heading_y
            self._heading_y = old_heading_x * -1

            pivot = self._body.get_pivot()

            for component in self._components:
                component.set_pivot(pivot)
                component.rotate(90)

class Button(EventHandler):
    """Represents buttons to tell car which way to go."""

    def __init__(self, window, car, center, direction):
        EventHandler.__init__(self)

        BUTTON_RADIUS = 15

        self._win = window
        self._car = car
        self._color = "red"
        self._direction = direction

        self._circle = Circle(self._win, BUTTON_RADIUS, center)
        self._circle.set_fill_color(self._color)

        self._circle.add_handler(self)

        self._win.add(self._circle)


    def handle_mouse_press(self, event):
        """If clicked, tell the car which button was clicked."""

        self._car.move_car(self._direction)



def main(window):

    window.set_width(600)
    window.set_height(600)

    r = Car(window, (300, 300), "yellow")


if __name__ == "__main__":
    # When using cs110graphics, replace the usual call to main() with this:
    StartGraphicsSystem(main)
