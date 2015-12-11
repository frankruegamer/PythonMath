import math
import sys


def check(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    else:
        return True


def fact(x):
    facts = []
    d = 2
    while d <= math.sqrt(x):
        while x % d == 0:
            facts.append(d)
            x //= d
        d += 1
    if x > 1:
        facts.append(x)
    return facts


def phi(m):
    product = 1
    for f in fact(m):
        product *= (f - 1)
    return product


def sqrfree(m):
    facts = fact(m)
    return True if len(facts) == len(set(facts)) else False


numberlist = []
longest = 0
for arg in sys.argv:
    try:
        n = int(arg)
        if n <= 0:
            raise ValueError
        length = len(str(n))
        longest = length if (length > longest) else longest
        numberlist.append(n)
    except ValueError:
        pass
if len(numberlist) != 0:
    print("\nIs <n> a prime number?")
    for n in numberlist:
        prime = check(n)
        print(("{0:<%d} {1}" % (longest + 1)).format("%d:" % n, prime), end="")
        if not prime:
            print(" (%s)" % ('*'.join(map(str, fact(n)))), end="")
        if sqrfree(n):
            print(", Φ(m)=%d" % phi(n))
        else:
            print()
else:
    print("Syntax: prime.py number1 [number2 ...]")
print()
