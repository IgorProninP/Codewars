"""
Define a function that takes one integer argument and returns logical value true or false depending
on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might
time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2,
will be too slow.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""


# Solutions from Codewars:
#
# def is_prime(n):
#     from math import sqrt
#     return n > 1 and all(n % d for d in range(2, int(sqrt(n)) + 1))
#
#
# import gmpy2
#
# def is_prime(num):
#     return gmpy2.is_prime(num) if num > 0 else False


#########################################################################

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return True
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num


if __name__ == '__main__':
    print(is_prime(19089234289))
