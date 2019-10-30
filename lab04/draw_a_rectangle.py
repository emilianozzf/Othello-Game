# This program, given a symbol, width and height of a rectangle,
# prints the expected rectangle.
WHITESPACE = ' '


def main():
    symbol = input("Enter a symbol: ")  # asks user for a symbol
    width = int(input("Enter the width: "))  # asks user for a width
    height = int(input("Enter the height: "))  # asks user for a length
    if width < 2:  # checks if the value of width is two small
        print("The value of width is too small!")
        return
    if height < 2:  # checks if the value of width is two small
        print("The value of height is too small!")
        return

    for h in range(height):  # loops through height
        if h == 0 or h == height - 1:
            print(symbol * width)  # prints the first and the last line
        else:
            print(symbol + WHITESPACE * (width - 2) + symbol)  # prints
            # the lines left


main()
