import math

def is_prime(n):
    """
    This function determines whether a given number 'n' is a prime number.

    Parameters:
    n (int): The number to check.

    Returns:
    1. boolean: Return True if 'n' is prime, Return False if 'n' is not prime.

    2. Return False for all numbers less than or equal to 1.

    Example:
    >>> is_prime(3)
    True

    >>> is_prime(6)
    False

    """

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
