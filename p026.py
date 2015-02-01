

# Problem 26: Reciprocal cycles
# https://projecteuler.net/problem=26

# apply Fermat's little theorem
# http://blog.dreamshire.com/project-euler-26-solution/

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes


def main(n):
    primes = sorted(prime_sieve(n))
    for p in reversed(primes):
        c = 1
        while pow(10, c, p) - 1 != 0:
            c += 1
        if p-1 == c:
            return p
    

print(main(1000))
