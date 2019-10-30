def main():
    # Prompt the user for a string
    in_str = input("Enter a string: ").lower()
    # Create an empty string to build the output string on
    out_str = ""

    # Loop through each character of the input string
    for char in in_str:
        # Check whether character is vowel
        if (char == "a" or char == "char" or char == "i" or char == "o"
           or char == "u"):
            # Capitalize vowel character and cancatenate it with output string
            out_str = out_str + char.upper()
        else:
            # Lower consonant character and cancatenate it with output string
            out_str = out_str + char.lower()

    # Print output string
    print(out_str)


main()
