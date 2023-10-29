from prime_rf2877 import prime_rf2877
from prime import is_prime

def test_is_prime():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in prime_numbers:
        assert is_prime(prime) == True, f'Error: {prime} is not prime.'
        print(f"{prime} is prime.")

    composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for composite in composite_numbers:
        assert is_prime(composite) == False, f'Error: {composite} is not composite.'
        print(f"{composite} is composite.")
