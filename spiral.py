import turtle

def main():
    m = turtle.Turtle()

    m.screen.bgcolor("black")
    m.pencolor("white")

    m.speed(0)

    #turtle.tracer(False)

    draw_spiral(m)

    #turtle.update()

    turtle.mainloop()

def draw_spiral(t):
    """Draws a hexagonal spiral"""

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for x in range(400):
        c = colors[x % 6]
        t.pencolor(c)

        t.forward(x)
        t.left(59)


main()
