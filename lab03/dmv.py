import random as rnd  # import random library and name it "rnd" for short

def main():
    full_name = input("""Welcome to the DMV (estimated wait time is 3 hours)
Please enter your first, middle, and last name:\n""")  # get user's full name
    birthday = input("Enter date of birth (MM/DD/YY):\n")  # get user's birthday

    driver_licence_number = rnd.randint(1000000, 9999999)  # get an random 7-digit integer as driver licence number
    name_break1 = full_name.find(" ")  # find position of space between first name and middle name
    name_break2 = full_name.rfind(" ")  # find position of space between middle name and last name
    first_name = full_name[0].upper() + full_name[1:name_break1].lower()  # slice first name out of full name
    if (name_break1 != name_break2):  # check whether there is middle name in full name
        middle_name = full_name[name_break1 + 1].upper() + full_name[name_break1 + 2:name_break2].lower()  # slice middle name out of full name
    else:
        middle_name = ""  # set middle name as empty string
    last_name = full_name[name_break2 + 1].upper() + full_name[name_break2 + 2:].lower()  # slice last name out of full name
    expiration_date = birthday[:6] + "21"  # get expiration date from birthday

    # print out driver license's basic information
    print("-------------------------------------")
    print("Washington Driver License")
    print("DL", driver_licence_number)
    print("LN", last_name)
    print("FN", first_name, middle_name)
    print("DOB", birthday)
    print("EXP", expiration_date)
    print("-------------------------------------")


main()
