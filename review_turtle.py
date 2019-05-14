
import turtle, math

def main():
    t = turtle.Turtle()

    t.fillcolor("coral")
    t.begin_fill()

    t.up()
    t.backward(150)
    t.down()

    height = math.sqrt(60 ** 2 - 30 ** 2)

    for _ in range(2):
        t.forward(300)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()

    t.left(60)
    t.fillcolor("blue")
    t.begin_fill()

    for _ in range(5):
        t.forward(60)
        t.right(120)
        t.forward(60)
        t.left(120)

    t.end_fill()

    turtle.mainloop()

main()
