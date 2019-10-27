class PrimeGenerator:
    """A class representing a prime generator"""
    def __init__(self):
        """Creates a list to store primes and a set to store composites"""
        self.primes_list = []
        self.composites_set = set()

    def primes_to_max(self, max):
        """Takes an integer argument and returns a list of all primes from 2
        to the argument value"""
        for n in range(2, max+1):
            if n not in self.composites_set:
                prime = n
                self.primes_list.append(prime)
                for composite in range(prime**2, max+1, prime):
                    self.composites_set.add(composite)
        return self.primes_list
