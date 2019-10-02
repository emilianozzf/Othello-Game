import sys


def main(files):
    try:
        out = open("results.txt", "w")

    except:
        print("Can't open results.txt for writing")
        return

    for filename in files:
        try:
            f = open(filename, "r")
        except:
            print("Can't open", filename)
            return

        title = f.readline().strip()  # readline method returns
        # always the next line and strip method strip off "\n"

        author = str.join(' ', f.readline().strip.split(' ')[1:])

        line_count = 0
        for line in f:
            line_count += 1

        out.write("Processed poem:\n")
        out.write("Titile:" + titile + "\n")
        out.write("Author:" + author + "\n")
        out.write("Lines:" + str(line_count) + "\n")
        out.write("\n")


main(sys.argv[1:])

# pass
# python3 06_file_IO Poems/*
