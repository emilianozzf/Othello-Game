v = "This v is a global variable"


def main():
    print("Calling f1")
    f1()
    print("Calling f2")
    f2()


def f1():
    global v
    v = "This global v has been monkeyed with by f1"
    x = "A variable in f1"
    print(v)


def f2():
    x = "A variable in f2"
    print(x)
    print(v)


main()
