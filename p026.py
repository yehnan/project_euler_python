

# Problem 26: Reciprocal cycles
# https://projecteuler.net/problem=26

# apply Fermat's little theorem
# see http://blog.dreamshire.com/project-euler-26-solution/

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

def rc(n):
    for p in reversed(sorted(prime_sieve(n))):
        c = 1
        while pow(10, c, p) - 1 != 0:
            c += 1
        if p-1 == c:
            return p

#
def test():
    if rc(10) == 7:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return rc(1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

