
def main():

    filename = input("Enter a filename: ")

    file_to_read = open(filename, "r")

    words = []
    for line in file_to_read:
        words.append(line[:-1])

    print(words)

if __name__ == "__main__":
    main()
