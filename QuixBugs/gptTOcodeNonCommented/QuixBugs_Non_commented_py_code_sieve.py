#sieve.py
#
#The code provided is missing a check for the square root of the number being tested. This optimization can significantly improve the performance of the sieve algorithm. Additionally, the code should handle cases where the input is less than 2.
#
#Here is the corrected code:
#
import math
#
def sieve(max):
    if max < 2:
        return []
    
    primes = []
    for n in range(2, max + 1):
        if all(n % p != 0 for p in primes if p <= math.isqrt(n)):
            primes.append(n)
    return primes
#
#
#