

# Problem 10: Summation of primes
# https://projecteuler.net/problem=10

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

def sop(n):
    return sum(prime_sieve(n))

#
def test():
    if sop(10) == 17:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return sop(2 * 1000 * 1000)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

