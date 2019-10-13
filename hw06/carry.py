# This program prompts the user for two integers of any length, adds them
# together, counts the number of times the "carry" operation needs
# to be carried out, and prints out the result


def main():
    # Prompts the user for the first number and cast it to an integer
    num1 = int(input("Enter the first number: "))
    # Prompts the user for the first number and cast it to an integer
    num2 = int(input("Enter the second number: "))
    # Adds two input numbers
    sum = num1 + num2
    # Computes the number of places of the first input number
    num_places1 = get_num_places(num1)
    # Computes the number of places of the second input number
    num_places2 = get_num_places(num2)
    # Get the list of digits of the first input number
    splitted1 = split_num(num1, num_places1)
    # Get the list of digits of the second input number
    splitted2 = split_num(num2, num_places2)
    # Get two same-length lists of digits of
    splitted1, splitted2 = get_same_len_splitted(splitted1, splitted2)
    # Computes the number of carries needed
    num_carries = count_carries(splitted1, splitted2)
    # Prints out the result
    print(num1, "+", num2, "=", sum)
    print("Number of carries:", num_carries)


def get_num_places(num):
    """
    Given a number, returns its number of places
    Number -> Number
    """
    # Returns the number of places of the input number
    return len(str(num))


def split_num(num, num_of_places):
    """
    Given a number, returns a list of its digits
    Number Number -> List
    """
    # Ensures the splitted list has well-defined minimum value
    splitted = []
    # Loops through digits of the input number
    for i in range(num_of_places):
        # Computes the digit and adds it to the list
        splitted.append(num % 10)
        # Updates the num variable
        num //= 10
    # Returns the result list of digits
    return splitted


def get_same_len_splitted(splitted1, splitted2):
    """
    Given two lists of digits, returns two same-length lists of digits
    List List -> List List
    """
    # Computes the length of list1
    length1 = len(splitted1)
    # Computes the length of list2
    length2 = len(splitted2)
    # Mutated the lists to be of same length
    if length1 <= length2:
        for i in range(length2 - length1):
            splitted1.append(0)
    else:
        for i in range(length1 - length2):
            splitted2.append(0)
    # Returns the modified lists
    return splitted1, splitted2


def count_carries(splitted1, splitted2):
    """
    Given two same-length lists of digits, returns their number of carries
    List List -> Number
    """
    # Ensures the variables have well-defined minimum values
    num_carries = 0
    is_carried = []
    # Computes the number of carries
    for i in range(len(splitted1)):
        if splitted1[i] + splitted2[i] >= 10:
            is_carried.append(True)
            num_carries += 1
        elif splitted1[i] + splitted2[i] == 9 and i >= 1 and is_carried[i-1]:
            is_carried.append(True)
            num_carries += 1
        else:
            is_carried.append(False)
    # Returns the number of carries
    return num_carries


main()
