def main():
    function_caller_args(f1, "Hi there!")
    function_caller(f2)
    function_caller(f3())


def function_caller(foobar):
    print("I call a function")
    foobar()


def function_caller_args(foobar, argument):
    print("I call the function I got passed")
    foobar(argument)


def f1(some_string):
    print("I'm function f1, here's my argument:", some_string)


def f2():
    print("I'm function f2")


def f3():
    def f4():
        print("I'm function f4")
    return f4


main()
