import turtle

DISTANCE = 30

def main():
    m = turtle.Turtle()

    advanced_turtle_drawing(m)



def turtle_drawing(t):

    while True:

        user_input = input("Enter a direction using wasd: ")

        if user_input == "w":
            t.setheading(90)
            t.forward(DISTANCE)
        elif user_input == "a":
            t.setheading(180)
            t.forward(DISTANCE)
        elif user_input == "s":
            t.setheading(270)
            t.forward(DISTANCE)
        elif user_input == "d":
            t.setheading(0)
            t.forward(DISTANCE)
        elif user_input == "quit":
            break

def advanced_turtle_drawing(t):

    while True:

        user_input = input("Enter a direction using wasd: ")

        if user_input == "quit":
            break

        angle_sum = 0
        for char in user_input:
            if char == "d":
                angle_sum += 0
            if char == "w":
                angle_sum += 90
            if char == "a":
                angle_sum += 180
            if char == "s":
                angle_sum += 270

        angle = angle_sum / len(user_input)
        t.setheading(angle)
        t.forward(DISTANCE * len(user_input))



main()
