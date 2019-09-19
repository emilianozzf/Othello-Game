import random as rnd  # import random library and name it "rnd" for short

def main():
    RANDOM_NUMBER = rnd.randint(1, 50)  # pick a random integer from 1 to 50 inclusively
    guess = int(input("""Welcome to the Guessing Game!
I picked a number between 1 and 50. Try and guess!\n"""))  # get user's first guess
    print("You guessed", guess)  # print user's first guess
    count = 1  # set number of user's guesses as 1

    while True:
        # let player know he succeeds
        if (guess == RANDOM_NUMBER):
            if (count == 1):
                print("Congratilations. You figured it out in", count, "try.")
            else:
                print("Congratulations. You figured it out in", count, "tries.")
            # mock or compliment player depending on number of guesses it took
            if (count == 1):
                print("That was lucky!")
            elif (count >= 2 and count <=4):
                print("That was amazing!")
            elif (count >=5 and count <= 6):
                print("That was okay.")
            elif (count == 7):
                print("Meh.")
            elif (count >= 8 and count <=9):
                print("This is not your game.")
            else:
                print("You are the worst guesser I've ever seen.")
            break  # break out of loop if player succeeds
        # let player know how close their guess is
        else:
            if (guess >= RANDOM_NUMBER - 1 and guess <= RANDOM_NUMBER + 1):
                guess = int(input("Your guess is scalding hot\n"))
            elif (guess >= RANDOM_NUMBER - 2 and guess <= RANDOM_NUMBER + 2):
                guess = int(input("Your guess is warm\n"))
            elif (guess >= RANDOM_NUMBER - 3 and guess <= RANDOM_NUMBER + 3):
                guess = int(input("Your guess is very warm\n"))
            elif (guess >= RANDOM_NUMBER - 5 and guess <= RANDOM_NUMBER + 5):
                guess = int(input("Your guess is warm\n"))
            elif (guess >= RANDOM_NUMBER - 8 and guess <= RANDOM_NUMBER + 8):
                guess = int(input("Your guess is cold\n"))
            elif (guess >= RANDOM_NUMBER - 13 and guess <= RANDOM_NUMBER + 13):
                guess = int(input("Your guess is very cold\n"))
            elif (guess >= RANDOM_NUMBER - 20 and guess <= RANDOM_NUMBER + 20):
                guess = int(input("Your guess is extremely cold\n"))
            else:
                guess = int(input("Your guess is icy freezing miserably cold\n"))
            count += 1  # keep track of number of user's guesses


main()
