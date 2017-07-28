def allprimes(n):
    """
    returns all prime numbers between 2 and n in a list primes using the prime1 function to
    test whether a number is prime
    :type n: integer
    :param n: integer
    :return: list of all primes between 2 and n
    """
    primes = []
    for c in range(2, n + 1):
        if prime1(c) is True:
            primes.append(c)
    return primes


def prime1(n):
    """
    returns true is specified value is prime, false if not
    :param n:integer
    :return:true or false
    """
    import math
    for x in range(2, round(math.sqrt(n)) + 1):
        if n % x == 0 and x != 1:
            return False

    else:
        return True


def sieve1(n):
    """
    This function performs a version of Eratosthenes's sieve. It browses a list of the integers between 2
    and n, then is checks which numbers in that list are divisible by the numbers from 2 to square root n
    one at a time. Every number in targets is checked to see if it is divisible by the currently selected
    number between 2 and squareroot n. If they are divisible, those numbers are removed from the list
    targets, and the process is repeated for each number in targets. After the first appearance of the
    next number in between 2 and square root n in targets. A list of primes between 2 and n is returned.
    :param n: integer
    :return: list of primes between 2 and n
    """
    import math
    targets = list(range(2, n + 1))
    for x in range(2, round(math.sqrt(n) + 1)):
        if x in targets:
            for y in targets[1:]:
                if y % x == 0 and y != x:
                    targets.remove(y)
    print(targets)


def newton(x, f, g, tol):
    """
    preforms newtons method to approximate the root of a given function, accurate to a certain tolerance,
    from a specified initial approximation. The number of iterations is functionally limited by the
    tolerance value.
    :param x: initial approximation
    :param f: function whose root is being approximated
    :param g: derivative of function f
    :param tol: the limit on the size of the value of f(x)
    :return: approximation of the root of f nearest the initial approximation, x.
    """
    while abs(f(x)) > tol:
        x = x - (f(x) / g(x))
    print(x)