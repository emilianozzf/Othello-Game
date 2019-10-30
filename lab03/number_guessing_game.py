import random as rnd


def main():
    # Pick a random integer from 1 to 50 inclusively
    random_number = rnd.randint(1, 50)
    # Get user's first guess
    guess = int(input("""Welcome to the Guessing Game!
I picked a number between 1 and 50. Try and guess!\n"""))
    # Print user's first guess
    print("You guessed", guess)
    # Set number of user's guesses as 1
    count = 1

    while True:
        # Let player know he succeeds
        if (guess == random_number):
            if (count == 1):
                print("Congratilations. You figured it out in", count, "try.")
            else:
                print("Congratulations. You figured it out in", count,
                      "tries.")
            # Mock or compliment player depending on number of guesses it took
            if (count == 1):
                print("That was lucky!")
            elif (count >= 2 and count <= 4):
                print("That was amazing!")
            elif (count >= 5 and count <= 6):
                print("That was okay.")
            elif (count == 7):
                print("Meh.")
            elif (count >= 8 and count <= 9):
                print("This is not your game.")
            else:
                print("You are the worst guesser I've ever seen.")
            # Break out of loop if player succeeds
            break
        # Let player know how close their guess is
        else:
            if (guess >= random_number - 1 and guess <= random_number + 1):
                guess = int(input("Your guess is scalding hot\n"))
            elif (guess >= random_number - 2 and guess <= random_number + 2):
                guess = int(input("Your guess is warm\n"))
            elif (guess >= random_number - 3 and guess <= random_number + 3):
                guess = int(input("Your guess is very warm\n"))
            elif (guess >= random_number - 5 and guess <= random_number + 5):
                guess = int(input("Your guess is warm\n"))
            elif (guess >= random_number - 8 and guess <= random_number + 8):
                guess = int(input("Your guess is cold\n"))
            elif (guess >= random_number - 13 and guess <= random_number + 13):
                guess = int(input("Your guess is very cold\n"))
            elif (guess >= random_number - 20 and guess <= random_number + 20):
                guess = int(input("Your guess is extremely cold\n"))
            else:
                guess = int(input("Your guess is icy freezing miserably "
                                  + "cold\n"))
            # Keep track of number of user's guesses
            count += 1


main()
