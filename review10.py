
def main():
    name = "My name is SteveMORE CAPS."
    index = last_index_of_capital(name)
    print("The last index of a capital is", index, ", which is a", name[index])

    print(last_index_of_capital("no capitals here"))

    # In the examples above, name and "no capitals here" are the arguments
    # to the last_index_of_capital function.


def last_index_of_capital(string):
    """Returns the index of the last capital letter in string.
    If no capitals, return -1.
    string is the only parameter to this function."""

    for index in range(len(string) - 1, -1, -1):
        if string[index] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            return index

    return -1



main()
