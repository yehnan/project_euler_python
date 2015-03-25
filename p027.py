

# Problem 27: Quadratic primes
# https://projecteuler.net/problem=27

def prime_sieve(n, initials=set(), nmax=2):
    primes = set(range(nmax, n+1))
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
        
def qp():
    prod = None
    cnt_max = 0
    for a in range(-1000, 1000+1):
        for b in range(-1000, 1000+1):
            cnt = howmany(a, b)
            if cnt > cnt_max:
                cnt_max = cnt
                prod = a * b
    return prod

#
def test():
    if howmany(1, 41) == 40 and howmany(-79, 1601) == 80:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return qp()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

