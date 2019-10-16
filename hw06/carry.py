# This program prompts the user for two integers of any length and adds them
# together. In addition to adding them, it also counts the number of times
# the "carry" operation needs to be carried out.


def main():
    # Prompts the user for the first integer
    in_num1 = int(input("Enter the first number: "))
    # Prompts the user for the second integer
    in_num2 = int(input("Enter the second number: "))
    # Represents digits of the first integer in a list
    digits_of_num1 = list(str(in_num1))
    # Represents digits of the second integer in a list
    digits_of_num2 = list(str(in_num2))
    # Reverses the digits in the list1
    digits_of_num1.reverse()
    # Reverses the digits in the list1
    digits_of_num2.reverse()
    # Appends '0' to one of the two digits lists to make them of same length
    get_same_length_lists(digits_of_num1, digits_of_num2)
    # Computes the length of two same-length lists
    length = len(digits_of_num1)
    # Counts carry operations that need to be carried out
    carries = count_carries(digits_of_num1, digits_of_num2, length)
    # Computes the number of carry operations that need to be carried out
    num_of_carries = carries.count(1)
    # Prints the result
    print(in_num1, '+', in_num2, '=', in_num1 + in_num2)
    print("Number of carries:", num_of_carries)


def get_same_length_lists(digits_list1, digits_list2):
    """
    Appends '0' to one of the two digits lists to make them of same length
    List List -> None
    """
    # Computes the length of the input list1
    length_of_digits_list1 = len(digits_list1)
    # Computes the length of the input list2
    length_of_digits_list2 = len(digits_list2)
    # Checks which one of the two input lists is longer, and appends '0' to the
    # other one
    if length_of_digits_list1 <= length_of_digits_list2:
        for _ in range(length_of_digits_list2 - length_of_digits_list1):
            digits_list1.append('0')
    else:
        for _ in range(length_of_digits_list1 - length_of_digits_list2):
            digits_list2.append('0')


def count_carries(digits_list1, digits_list2, length):
    """
    Counts carry operations that need to be carried out
    List List Number -> List
    """
    # Ensures the list recording the carry operations has a well-defined
    # minimum value
    carries = [0]
    # Loops through each digit of the input lists
    for _ in range(length):
        # Computs the sum for the column
        sub_sum = int(digits_list1[_]) + int(digits_list2[_]) + carries[_]
        # Checks if the sum is larger than 9
        if sub_sum > 9:
            # Records there is a carry operation
            carries.append(1)
        # Otherwise
        else:
            # Records there is no carry operation
            carries.append(0)
    # Return the list recording the carry operations
    return carries


main()
