# This program prompts the user for a file name, then prints out
# counts of words, non-whitespace characters (including punctuation), and
# alphanumeric characters (letters and numbers, excluding punctuation).


def main():
    filename = input("Enter the file name: ")
    try:
        f = open(filename, "r")
    except:
        print("Can't open", filename)
        return
    num_words = 0
    num_nonwhite_chrs = 0
    num_alphanumeric_chrs = 0

    for line in f:
        words = line.strip().split(' ')
        if words[0] != '':
            num_words += len(words)
        nonwhite_chrs = str.join('', words)
        num_nonwhite_chrs += len(nonwhite_chrs)
        for c in nonwhite_chrs:
            if (ord(c.lower()) >= ord('a') and ord(c.lower()) <= ord('z')) \
               or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                num_alphanumeric_chrs += 1

    print("Words:", num_words)
    print("Characters: ", num_nonwhite_chrs)
    print("Letters & numbers:", num_alphanumeric_chrs)

main()
