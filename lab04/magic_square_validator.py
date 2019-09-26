# This programs, given a square, determines if it is a magic square.


def main():
    # Asks user for a potential magic square.
    print("Enter a magic number")
    square = []
    for i in range(3):
        square.append(list(input()))
        for j in range(3):
            square[i][j] = int(square[i][j])
    is_magic = True  # sets is_magic to True

    for i in range(3):
        sum_of_row = 0
        sum_of_column = 0
        sum_of_diagonal1 = 0
        sum_of_diagonal2 = 0
        for j in range(3):
            sum_of_row += square[i][j]  # sums all the numbers in a row
            sum_of_column += square[j][i]  # sums all the numbers in a column
            sum_of_diagonal1 += square[j][j]  # sums all the numbers
            # in diagonal1
            sum_of_diagonal2 += square[2 - j][j]  # sums all the numbers
            # in diagonal2
        # Checks if the given square is not a magic square
        if (sum_of_row != 15 or sum_of_column != 15 or
                sum_of_diagonal1 != 15 or sum_of_diagonal2 != 15):
            is_magic = False
            break

    if is_magic:
        print("This is a magic square!")  # shows the given square is
        # a magic square
    else:
        print("Not a magic square!")  # shows the given square is not
        # a magic sqaure

main()
