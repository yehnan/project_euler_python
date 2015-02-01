

# Problem 27: Quadratic primes
# https://projecteuler.net/problem=27

def prime_sieve(n, initials=set(), m=2):
    primes = set(range(m, n+1))
    if initials != set():
        primes |=  initials

    for i in range(2, (n+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes
n_max = 100
primes = prime_sieve(n_max)
def is_prime(n):
    global n_max
    global primes
    if n_max < n:
        n_max_new = n + (n//2)
        primes = prime_sieve(n_max_new, primes, n_max)
        n_max = n_max_new
    return n in primes
    
def howmany(a, b):
    n = 0
    while True:
        if is_prime(n**2 + a*n + b):
            n += 1
            continue
        else:
            break
    return n
        
def main():
    prod = 0
    n = 0
    for a in range(-1000, 1000+1):
        for b in range(-1000, 1000+1):
            hm = howmany(a, b)
            if hm > n:
                n = hm
                prod = a * b
    return prod
print(main())


