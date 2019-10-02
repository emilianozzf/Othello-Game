def hello_function(argument):
    """Prints a hello message with a value
    String -> None"""
    print("Hello,", argument)

print(dir(str))  # returns a list of methods that can be called
print(help(hello_function))  # returns a document of a function
eval(input("Tell me what to do: "))
