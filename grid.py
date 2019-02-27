
import random

# word_grid = [["one", "two", "three"],
#              ["a", "b", "c"],
#              ["hat", "cat", "bat"],
#              ["apple", "banana", "cherry"]]
#
# print(word_grid)
# print(word_grid[2])
# print(word_grid[2][1])
#
# for row in word_grid:
#     print(row)

WIDTH = 12
DIRECTIONS = ["right", "left", "up", "down"]

def main():

    # BAD: Doesn't make copies of rows
    # row = ["empty"] * WIDTH
    # room = [row] * WIDTH

    room = []
    for _ in range(WIDTH):
        row = ["dirt"] * WIDTH
        room.append(row)

    # print(room)

    # for row in room:
    #     print(row)
    # print()

    room[3][6] = "robot"

    for col in range(WIDTH):
        room[0][col] = "obstacle"
        room[WIDTH - 1][col] = "obstacle"

    for row in range(WIDTH):
        room[row][0] = "obstacle"
        room[row][WIDTH - 1] = "obstacle"

    # for row in room:
    #     print(row)
    # print()

    print_room(room)

    # for _ in range(6):
    #     direct = input("Enter which direction the robot should move: ")
    #     room = move_robot(room, direct)
    #     print_room(room)


    # visits = random_walk(room, 10000)

    visits = clean_room(room)

    for row in visits:
        for num in row:
            print("{:5d}".format(num), end="")
        print()



    # for i in range(5):
    #     print(i, "woo", i *i, end="CAT", sep="?")
    # print("DONE")


def print_room(room):
    """Prints a nice representation of the robot's room"""

    for row in room:
        for cell in row:
            if cell == "obstacle":
                print("O", end="")
            elif cell == "robot":
                print("R", end="")
            elif cell == "empty":
                print(" ", end="")
            elif cell == "dirt":
                print("*", end="")

        print()

def robot_location(room):
    """Find the robot's row and column in the room"""

    for r in range(WIDTH):
        for c in range(WIDTH):
            if room[r][c] == "robot":
                return (r, c)


def move_robot(room, direction):
    """Moves robot one cell in specified direction"""

    robot_row, robot_col = robot_location(room)

    intended_row = robot_row
    intended_col = robot_col

    if direction == "right":
        intended_col = robot_col + 1
    elif direction == "left":
        intended_col = robot_col - 1
    elif direction == "up":
        intended_row = robot_row - 1
    elif direction == "down":
        intended_row = robot_row + 1

    if room[intended_row][intended_col] != "obstacle":
        room[intended_row][intended_col] = "robot"
        room[robot_row][robot_col] = "empty"

    return room

def random_walk(room, steps):
    """Randomly moves robot around room for steps steps"""

    # Track the robot location
    visits = []
    for _ in range(WIDTH):
        row = [0] * WIDTH
        visits.append(row)

    for i in range(steps):
        direction = random.choice(DIRECTIONS)
        room = move_robot(room, direction)

        print("After {} steps, robot moved {}, and the room looks like:".format(i, direction))
        print_room(room)

        r, c = robot_location(room)
        visits[r][c] += 1

    return visits

def all_clean(room):
    """Return True if the room has no dirt, False otherwise"""

    for row in room:
        for cell in row:
            if cell == "dirt":
                return False

    return True

def clean_room(room):

    # Track the robot location
    visits = []
    for _ in range(WIDTH):
        row = [0] * WIDTH
        visits.append(row)

    i = 0
    while not all_clean(room):
        i += 1
        direction = random.choice(DIRECTIONS)
        room = move_robot(room, direction)

        print("After {} steps, robot moved {}, and the room looks like:".format(i, direction))
        print_room(room)

        r, c = robot_location(room)
        visits[r][c] += 1

    return visits

if __name__ == "__main__":
    main()
