# This program repeatedly prompts the user for numbers (until the user inputs
# 'done' and prints out a list of corresponding triangluar numbers)


def main():
    # Ensures the tri_nums has well-defined minimum value
    tri_nums = []
    # Repeatedly prompts the user for numbers
    while True:
        # Prompts the user for a number or 'done'
        user_input = input("Enter a number, or enter 'done': ")
        # Checks if the user input is 'done'
        if user_input == "done":
            # Prints out the list of triangluar numbers and break out
            print(tri_nums)
            break
        # Otherwise, computes the coresponding triangular number
        else:
            # Casts the input string to an integer
            in_num = int(user_input)
            # Computes the triangluar number of the input number
            tri_num = get_tri_num(in_num)
            # Prints out the result
            print("The triangular number for", in_num, "is", tri_num)
            # Adds the triangular number to the tri_num list
            tri_nums.append(tri_num)


def get_tri_num(num):
    """
    Given a number, returns its triangular number
    Number -> Number
    """
    # Ensures the tri_num variable has well-defined minimum value
    tri_num = 0
    # Computes num's triangular number
    for _ in range(1, num + 1):
        tri_num += _
    # Returns num's triangular number
    return tri_num


main()
