# This program reads data from a file, does some analysis on it, and finally
# prints the report.

# Sets all the conversion factors as constants
BTM_CRITICAL = 10
TOP_CRITICAL = 900
GALLONS_PER_MIN = 2
GOAL_GALLONS1 = 5
GOAL_GALLONS2 = 100
MINS_PER_HOUR = 60
HOURS_PER_DAY = 24
W_PER_KW = 1000


def main():
    # Opens a file and handles exceptions
    filename = input("Please enter the file name: ")
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("Unable to open", filename)
        return

    # Ensures the following variabls have well-defined minimum values
    critical_point = (BTM_CRITICAL + TOP_CRITICAL) / 2
    dur_in_mins = 0
    tot_run_mins = 0
    tot_gallons = 0
    tot_wmins = 0
    mins_to_reach1 = -1
    mins_to_reach2 = -1

    # Reads data line by line
    for line in f:
        # Updates the duration of the data file in minutes
        dur_in_mins += 1
        # Reads the number of watts by pump during the corresponding minute
        wmins_per_minute = int(line.strip())
        # Checks if the pump is running during the corresponding minute
        if wmins_per_minute > critical_point:
            # Updates the total running time in minutes
            tot_run_mins += 1
            # Updates the total number of gallons produced
            tot_gallons += GALLONS_PER_MIN
            # Updates the starting point
        # Updates the total power used by the pump in Watt minutes
        tot_wmins += wmins_per_minute
        # Computes how long it took to consume a certain quantity of water
        if tot_gallons == GOAL_GALLONS1 + 1:
            mins_to_reach1 = dur_in_mins
        if tot_gallons == GOAL_GALLONS2:
            mins_to_reach2 = dur_in_mins
        # Dynamically modifies the critical point
        if wmins_per_minute > BTM_CRITICAL and wmins_per_minute < TOP_CRITICAL:
            critical_point = (critical_point + wmins_per_minute) / 2
    # Computes the duration of the data file in hours
    dur_in_hs = dur_in_mins / MINS_PER_HOUR
    # Computes the duration of the data file in days
    dur_in_ds = dur_in_hs / HOURS_PER_DAY
    # Computes the average daily consumption
    ave_daily_consumption = tot_gallons / dur_in_ds
    # Computes the total power used by the pump in Kilowatt Hours
    tot_kwhs = tot_wmins / W_PER_KW / MINS_PER_HOUR

    # Prints the report respectively
    print("Data covers a total of", dur_in_hs, "hours")
    print("(That's", dur_in_ds, "days)\n")
    print("Pump was running for", tot_run_mins, "minutes, producing",
          tot_gallons, "gallons")
    print("(That's", ave_daily_consumption, "gallons per day)\n")
    print("Pump required a total of", tot_wmins, "watt minutes of power")
    print("(That's", tot_kwhs, "kWh)\n")
    print("It took", mins_to_reach1, "minutes of data to reach",
          GOAL_GALLONS1, "gallons.")
    print("It took", mins_to_reach2, "minutes of data to reach",
          GOAL_GALLONS2, "gallons.")


main()
