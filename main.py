# This program is a solution for
# Project Euler Problem 60
# https://projecteuler.net/problem=60

# Find the lowest sum for a set of five primes
# for which any two primes concatenate to produce another prime.


from sympy import isprime, primerange
from itertools import permutations


def takeAndConcatenate(array):
    array = list(permutations(array, 2))
    for x, y in array:
        number = int(str(x) + str(y))
        if not isprime(number):
            return False
    return True


def main():
    primes = list(primerange(3, 10_000))
    lenPrimes = len(primes)
    for first in range(0, lenPrimes):
        for second in range(first + 1, lenPrimes):
            firstPrime = primes[first]
            secondPrime = primes[second]
            array = [firstPrime, secondPrime]
            if takeAndConcatenate(array):
                for third in range(second + 1, lenPrimes):
                    thirdPrime = primes[third]
                    array = [firstPrime, secondPrime, thirdPrime]
                    if takeAndConcatenate(array):
                        for forth in range(third + 1, lenPrimes):
                            forthPrime = primes[forth]
                            array = [firstPrime, secondPrime, thirdPrime, forthPrime]
                            if takeAndConcatenate(array):
                                for fifth in range(forth + 1, lenPrimes):
                                    fifthPrime = primes[fifth]
                                    array = [firstPrime, secondPrime, thirdPrime, forthPrime, fifthPrime]
                                    if takeAndConcatenate(array):
                                        print("Five primes are:", array)
                                        print("Sum of them is:", sum(array))
                                        return


main()
