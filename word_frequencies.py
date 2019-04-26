
def main():

    filename = input("Enter a filename: ")

    file_to_read = open(filename, "r")

    file_contents = file_to_read.read()
    words = file_contents.split()

    word_frequencies = {}

    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

    for key in word_frequencies:
        print(word_frequencies[key], " - ", key)

if __name__ == "__main__":
    main()
