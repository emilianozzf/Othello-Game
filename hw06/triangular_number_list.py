# This program repeatedly prompts the user for numbers (until the user inputs
# 'done' and prints out a list of corresponding triangluar numbers)


def main():
    # Ensures the triangular numbers' list has well-defined minimum value
    tri_nums = []
    # Repeatedly executes until the user inputs 'done'
    while True:
        # Prompts the user for a number or 'done'
        user_input = input("Enter a number, or enter 'done': ")
        # Checks if the user input is 'done'
        if user_input == "done":
            # Prints out the list of triangluar numbers
            print(tri_nums)
            # Breaks out of the loop
            break
        # Otherwise, the user inputs a number
        else:
            # Casts the input string to an integer
            in_num = int(user_input)
            # Computes the triangluar number of the input number
            tri_num = triangular_number(in_num)
            # Prints out the result
            print("The triangular number for", in_num, "is", tri_num)
            # Adds the triangular number to the triangular numbers' list
            tri_nums.append(tri_num)


def triangular_number(num):
    """
    Given a number, returns its triangular number
    Number -> Number
    """
    # Ensures the tri_num variable has well-defined minimum value
    tri_num = 0
    # Computes the triangular number
    for _ in range(1, num + 1):
        tri_num += _
    # Returns the triangular number
    return tri_num


main()
