import random as rnd  # import random library and name it "rnd" for short


def main():
    # Get user's full name
    full_name = input("""Welcome to the DMV (estimated wait time is 3 hours)
Please enter your first, middle, and last name:\n""")
    # Get user's birthday
    birthday = input("Enter date of birth (MM/DD/YY):\n")

    # Get an random 7-digit integer as driver licence number
    driver_licence_number = str(rnd.randint(0, 9999999))
    driver_licence_number = ((7 - len(driver_licence_number))*'0'
                             + driver_licence_number)
    # Find position of space between first name and middle name
    name_break1 = full_name.find(" ")
    # Find position of space between middle name and last name
    name_break2 = full_name.rfind(" ")
    # Slice first name out of full name
    first_name = full_name[0].upper() + full_name[1:name_break1].lower()
    # Check whether there is middle name in full name
    if (name_break1 != name_break2):
        # Slice middle name out of full name
        middle_name = (full_name[name_break1 + 1].upper()
                       + full_name[name_break1 + 2:name_break2].lower())
    else:
        # Set middle name as empty string
        middle_name = ""
    # Slice last name out of full name
    last_name = (full_name[name_break2 + 1].upper()
                 + full_name[name_break2 + 2:].lower())
    # Get expiration date from birthday
    expiration_date = birthday[:6] + "21"

    # Print out driver license's basic information
    print("-------------------------------------")
    print("Washington Driver License")
    print("DL", driver_licence_number)
    print("LN", last_name)
    print("FN", first_name, middle_name)
    print("DOB", birthday)
    print("EXP", expiration_date)
    print("-------------------------------------")


main()
