# This program prompts the user for a numerical value that is a multiple of 2
# and prints out a cube.

# Stores some useful characters as constants
SPACE = ' '
EMPTY = ''
# Horizontal lines consist of '-' characters
HORIZONTAL_CHAR = '-'
# Vertical lines consist of '|' characters
VERITICAL_CHAR = '|'
# Diagonals consist of '/' characters
DIAGONAL_CHAR = '/'
# Cube corners cosist of '+' characters
CONER_CHAR = '+'


def main():
    # Prompts the user for cube size
    num = int(input("Input cube size (multiple of 2): "))
    # Computes the length of the cube
    length = 2*num
    # Computes the number of rows
    num_rows = 3*num//2 + 3
    # Computes the lines
    lines = get_lines(length, num_rows)
    # Complements each line and prints it out
    for _ in range(num_rows):
        if _ == 0 or _ == num_rows - 1:
            print(lines[_])
        elif 0 < _ < 2*num_rows//3 - 1:
            print(lines[_] + VERITICAL_CHAR)
        elif _ == 2*num_rows//3 - 1:
            print(lines[_] + CONER_CHAR)
        else:
            print(lines[_] + DIAGONAL_CHAR)


def get_lines(length, num_rows):
    """
    Given the length of lines and the number of rows, returns a list of lines
    Number Number -> List
    """
    # Ensures the list has well-defined minimum value
    lines = []
    # Computes the horizontal edge
    horizontal_edge = get_horizontal_edge(length)
    # Computes the horizontal line1
    horizontal_line1 = get_horizontal_line(length, DIAGONAL_CHAR)
    # Computes the horizontal line2
    horizontal_line2 = get_horizontal_line(length, VERITICAL_CHAR)
    # Computes the left spaces lines
    left_spaces_lines = get_left_spaces_lines(num_rows)
    # Computes the right spaces lines
    right_spaces_lines = get_right_spaces_lines(num_rows)
    # Concatenates each line
    for _ in range(num_rows):
        if _ == 0 or _ == num_rows//3 or _ == num_rows - 1:
            lines.append(left_spaces_lines[_] + horizontal_edge +
                         right_spaces_lines[_])
        elif _ < num_rows//3:
            lines.append(left_spaces_lines[_] + horizontal_line1 +
                         right_spaces_lines[_])
        else:
            lines.append(left_spaces_lines[_] + horizontal_line2 +
                         right_spaces_lines[_])
    # Returns the concatenated lines
    return lines


def get_horizontal_edge(length):
    """Given the length of the horizontal edge, returns the horizontal edge
    Numebr -> String
    """
    # Computs and returns the horizontal edge
    return CONER_CHAR + HORIZONTAL_CHAR*length + CONER_CHAR


def get_horizontal_line(length, char):
    """Given the length of the horizontal line and the character, returns
    the horizontal line
    Numebr Character -> String
    """
    # Computes and returns the horizontal line
    return char + SPACE*length + char


def get_left_spaces_lines(num_rows):
    """
    Given the number of rows, returns the left spaces-lines
    Number -> List
    """
    # Ensures the list has well-defined minimum value
    left_spaces_lines = []
    # Computes the left spaces-lines
    for _ in range(num_rows//3):
        left_spaces_lines.append(SPACE*(num_rows//3 - _))
    for _ in range(num_rows//3, num_rows):
        left_spaces_lines.append(EMPTY)
    # Returns the left spaces-lines
    return left_spaces_lines


def get_right_spaces_lines(num_rows):
    """
    Given the number of rows, returns the right spaces-lines
    Number -> List
    """
    # Ensures the list has well-defined minimum value
    right_spaces_lines = []
    # Computes the right spaces-lines
    for _ in range(1):
        right_spaces_lines.append(EMPTY)
    for _ in range(1, num_rows//3):
        right_spaces_lines.append(SPACE*(_ - 1))
    for _ in range(num_rows//3, 2*num_rows//3):
        right_spaces_lines.append(SPACE*(num_rows//3 - 1))
    for _ in range(2*num_rows//3, num_rows - 1):
        right_spaces_lines.append(SPACE*(num_rows - 2 - _))
    for _ in range(num_rows - 1, num_rows):
        right_spaces_lines.append(EMPTY)
    # Returns the left spaces-lines
    return right_spaces_lines


main()
