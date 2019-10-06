# This program prompts the user for a file name, then prints out
# counts of words, non-whitespace characters (including punctuation), and
# alphanumeric characters (letters and numbers, excluding punctuation).


def main():
    # Gets the file name from the user
    filename = input("Enter the file name: ")
    # Opens the file and handle exceptions
    try:
        f = open(filename, "r")
    except:
        print("Can't open", filename)
        return

    # Makes sure each variable has reasonable minimum value
    num_words = 0
    num_nonwhite_chrs = 0
    num_alphanumeric_chrs = 0

    # Reads the file line by line
    for line in f:
        # Splits the line into words
        words = line.strip().split(' ')
        # Makes sure this is not a empty line
        if words != ['']:
            # Updates the number of words
            num_words += len(words)
            # Joins the words into nonwhite characters (including punctuation)
            nonwhite_chrs = str.join('', words)
            # Updates the number of nonwhite characters (including punctuation)
            num_nonwhite_chrs += len(nonwhite_chrs)
            # Loops through characters in the nonwhite characters
            # (including punctuation)
            for c in nonwhite_chrs:
                # Checks if the character is an alphanumeric character
                if ((ord('a') <= ord(c.lower()) <= ord('z')) or
                   (ord('0') <= ord(c) <= ord('9'))):
                    # Updates the number of alphanumeric characters
                    num_alphanumeric_chrs += 1

    # Prints the results
    print("Words:", num_words)
    print("Characters: ", num_nonwhite_chrs)
    print("Letters & numbers:", num_alphanumeric_chrs)

main()
