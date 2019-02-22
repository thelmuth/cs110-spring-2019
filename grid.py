
# word_grid = [["one", "two", "three"],
#              ["a", "b", "c"],
#              ["hat", "cat", "bat"],
#              ["apple", "banana", "cherry"]]
#
# print(word_grid[2][1])
#
# for bag in word_grid:
#     print(bag)


WIDTH = 12

def main():

    # # Bad idea, makes aliases for every row
    # row = ["empty"] * WIDTH
    # room = [row] * WIDTH

    room = []
    for _ in range(WIDTH):
        row = ["empty"] * WIDTH
        room.append(row)

    #print(room)
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

    room = move_robot(room, "right")
    print_room(room)


    # for i in range(5):
    #     print(i, "hi", "yay", end="$$")


def print_room(room):
    """Prints a robot's room"""
    for row in room:
        for element in row:
            if element == "empty":
                print(" ", end="")
            elif element == "robot":
                print("R", end="")
            elif element == "obstacle":
                print("O", end="")
        print()
    print()

def robot_location(room):
    """Find's the robot's location in a room"""

    for r in range(WIDTH):
        for c in range(WIDTH):
            if room[r][c] == "robot":
                return (r, c)

def move_robot(room, direction):
    """Moves the robot in given direction, if it doesn't hit an obstacle"""

    robot_row, robot_col = robot_location(room)

    print(robot_row, robot_col)

if __name__ == "__main__":
    main()
