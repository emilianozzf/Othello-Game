def main():
    # takes a user's age and resting heart rate
    age = int(input("Please enter your age: "))
    rest_heart_rate = int(input("Please enter your resting heart rate: "))

    # compute the maximum heart rate and heart rate reserve
    max_heart_rate = 208 - 0.7 * age
    reserve = max_heart_rate - rest_heart_rate

    print("=======================================")

    # print the heart rate reserve
    print("Your heart rate reserve is:", round(reserve, 2), "bpm")
    # compute the range of each training zone and print it out
    print("Here is a breakdown of your training zones:")
    print("Zone 1:", round(rest_heart_rate + reserve * 0.5, 2), "to",
          round(rest_heart_rate + reserve * 0.6, 2), "bpm")
    print("Zone 2:", round(rest_heart_rate + reserve * 0.6 + 0.01, 2), "to",
          round(rest_heart_rate + reserve * 0.7, 2), "bpm")
    print("Zone 3:", round(rest_heart_rate + reserve * 0.7 + 0.01, 2), "to",
          round(rest_heart_rate + reserve * 0.8, 2), "bpm")
    print("Zone 4:", round(rest_heart_rate + reserve * 0.8 + 0.01, 2), "to",
          round(rest_heart_rate + reserve * 0.93, 2), "bpm")
    print("Zone 5:", round(rest_heart_rate + reserve * 0.93 + 0.01, 2), "to",
          round(rest_heart_rate + reserve * 1, 2), "bpm")

    print("=======================================")


main()
