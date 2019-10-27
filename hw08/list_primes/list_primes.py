from prime_generator import PrimeGenerator


def main():
    # Initialize an object of PrimeGeneraotr class
    pg = PrimeGenerator()
    # Prompts the user for a maximum integer
    max = int(input("Enter an integer you want to count primes to (>= 2):\n"))
    # Counts the primes up to the maximum integer
    primes_list = pg.primes_to_max(max)
    # Prints the result
    print(primes_list)


main()
