

# Problem 10: Summation of primes
# https://projecteuler.net/problem=10

# this is slow for the problem
def prime(p_max):
    primes = [2]
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True
    def next_prime():
        p = primes[-1]
        while True:
            p += 1
            if is_prime(p):
                return p
    while True:
        yield primes[-1]
        np = next_prime()
        if np > p_max:
            break
        else:
            primes.append(np)

prime_10 = prime(10)
print(sum(prime_10))
# prime_2m = prime(2 * 1000 * 1000)
# print(sum(prime_2m))   # slow

# Sieve is faster
def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

print(sum(prime_sieve(10)))
print(sum(prime_sieve(2 * 1000)))
print(sum(prime_sieve(2 * 1000 * 1000)))

