from prime_generator import PrimeGenerator


def test_primes_to_max():
    """Tests the primes_to_max method"""
    pg1 = PrimeGenerator()
    pg2 = PrimeGenerator()
    assert pg1.primes_to_max(100)[0] == 2
    assert pg1.primes_to_max(100)[8] == 23
    assert pg1.primes_to_max(100)[16] == 59
    assert pg2.primes_to_max(1000)[40] == 179
    assert pg2.primes_to_max(1000)[120] == 661
    assert pg2.primes_to_max(1000)[160] == 947
