def main():
    interview()


def interview():
    """Conducts an interview
    None -> None"""
    questions()
    print("We're done here.")


def questions():
    """Poses questions to the user
    None -> None"""
    answer = "yes"
    while answer == "yes":
        answer = input("Do you really want to work here?\n")


main()
