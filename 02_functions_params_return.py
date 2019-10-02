import sys


def main():
    hello_function("World!")

    string1 = '&' * double_num(6)
    string2 = '%' * add_nums(5, 7)
    string2 = '*' * add_nums(double_num(5), 7)

    print(string1)
    print(string2)

    x, y, z = multi_value_return()
    print("x is", x)
    print("y is", y)
    print("z is", z)

    no_value_return()


def hello_function(argument):
    """Prints a hello message with a value
    String -> None"""
    print("Hello,", argument)


def double_num(number):
    """Doubles a number
    Number -> Number"""
    return 2 * number


def add_nums(x, y):
    """Adds x and y
    Number Number -> Number"""
    return x + y


def multi_value_return():
    """Returns three characters
    None -> Character Character Character"""
    return 'a', 'b', 'c'


def no_value_return():
    """Prints a string
    None -> None"""
    print("Just printing this and not returning anything")

main()
