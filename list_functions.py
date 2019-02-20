
def main():

    names = get_5_names()
    print(names)

    longest = longest_string(names)
    print(longest)

    trees = ["elm", "maple", "oak"]
    longest_tree = longest_string(trees)

def get_5_names():
    """Asks the user for 5 names, and returns them in a list"""

    names_list = []
    for _ in range(5):
        name = input("Give me a name: ")
        names_list.append(name)

    return names_list


def longest_string(strings):
    """Returns the longest string in strings"""

    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s

    return longest



main()
