# This program, given a user's first name, last name, and favorite word,
# returns a unique user name as well as three suggested passwords,
# each constructed using different rules.
import random as rnd


def main():
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    favorite_word = input("Please enter your favorite word: ")

    user_name = generate_user_name(first_name, last_name)
    password1 = generate_password1(first_name, last_name)
    password2 = generate_password2(first_name, last_name, favorite_word)
    password3 = generate_password3(first_name, last_name, favorite_word)

    print("\nThanks " + first_name + ", your user name is: " + user_name)
    print("\nHere are three suggested passwords for you to consider:\n")
    print("Password1:", password1)
    print("Password2:", password2)
    print("Password3:", password3)


def generate_user_name(first_name, last_name):
    """Given a user's first name and last name, returns a unique user name,
    using the specific rule."""
    first_letter = first_name[0]
    last_name_extra = last_name
    for _ in range(7):
        last_name_extra += chr(rnd.randint(ord('a'), ord('z')))
    rnd_num = str(rnd.randint(0, 99))

    user_name = (first_letter + last_name_extra[:7] + rnd_num).lower()

    return user_name


def generate_password1(first_name, last_name):
    """Given a user's first name and last name, returns a unique password1,
    using the specific rule."""
    first_name_replaced = replace_chrs(first_name)
    rnd_num = str(rnd.randint(0, 99))
    last_name_replaced = replace_chrs(last_name)
    password1 = first_name_replaced + rnd_num + last_name_replaced

    return password1


def replace_chrs(name):
    """Given a name, returns a replaced name, using a specific rule."""
    name_replaced = ""

    for c in name:
        if c.lower() == 'a':
            name_replaced += '@'
        elif c.lower() == 'o':
            name_replaced += '0'
        elif c.lower() == 'l':
            name_replaced += '1'
        elif c.lower() == 's':
            name_replaced += '$'
        else:
            name_replaced += c.lower()

    return name_replaced


def generate_password2(first_name, last_name, favorite_word):
    """Given a user's first name, last name, and favorite word, returns a
    unique password2, using the specific rule."""
    words_list = [first_name, last_name, favorite_word]
    password2 = ""

    for e in words_list:
        password2 += abbreviate_words(e)

    return password2


def abbreviate_words(word):
    """Given a word, returns an "acronym", using the specific rule."""
    return word[0].lower() + word[-1].upper()


def generate_password3(first_name, last_name, favorite_word):
    """Given a user's first name, last name, and favorite word, returns a
    unique password3, using the specific rule."""
    rnd_words_list = generate_random_order_list(first_name,
                                                last_name,
                                                favorite_word)
    password3 = ""

    for e in rnd_words_list:
        password3 += generate_portion(e)

    return password3


def generate_portion(word):
    """Given a word, returns a portion of the word, using the specific rule."""
    portion = word[:rnd.randint(1, len(word))]
    return portion


def generate_random_order_list(word1, word2, word3):
    """Given a list of words, returns a random-ordered list of words."""
    original_words_list = [word1, word2, word3]
    rnd_words_list = []

    while len(rnd_words_list) < 3:
        word_pick = original_words_list[rnd.randint(0, 2)]
        if word_pick not in rnd_words_list:
            rnd_words_list.append(word_pick)

    return rnd_words_list

main()
