
# What does this program draw?
import turtle

t = turtle.Turtle()

for x in range(20, 100, 20):
    t.circle(x)

t.right(45)

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.mainloop()
