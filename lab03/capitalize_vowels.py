def main():
    in_str = input("Enter a string: ")  # get input string from user
    out_str = ""  # set output string as empty string

    for e in in_str:  # loop through each character of input string
        if (e == "a" or e == "e" or e == "i" or e == "o" or e == "u"):  # check whether character is vowel
            out_str = out_str + e.upper()  # capitalize vowel character and cancatenate it with output string
        else:
            out_str = out_str + e.lower()  # lower consonant character and cancatenate it with output string

    print(out_str)  # print output string


main()
