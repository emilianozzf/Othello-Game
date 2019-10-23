# This program asks for an account number and determines whether or not the
# number is valid using Luhn’s algorithm.


def main():
    # Prompts the user for an account number and casts it into a list
    account_number = list(input("Enter your account number:\n"))
    # Computes the length of the account number
    length_of_account_number = len(account_number)
    # Ensures the sum variable has well-defined minimum value
    sum = 0

    # Loops through the account number
    for i in range(length_of_account_number):
        # Casts the digit from a string to an integer
        account_number[i] = int(account_number[i])
        # Beginning with the second to right-most digit, loops through every
        # other digit from right to left
        if i in range(length_of_account_number - 2, -1, -2):
            # Doubles the digit's value
            doubled = 2*account_number[i]
            # If the resulting number is a two digit number, adds the first
            # digit of that value to the second digit, yielding a single
            # digit number
            account_number[i] = (doubled % 10) + (doubled // 10)
        # Updates the sum variable
        sum += account_number[i]

    # Checks if the input account number is not empty and the resulting sum is
    # evenly divisible by 10
    if (account_number) and (sum % 10 == 0):
        # The input account number is valid
        print("The account number is valid!")
    # Otherwise
    else:
        # The input account number is not valid
        print("The account number is not valid.")


main()
