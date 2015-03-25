

# Problem 47: Distinct primes factors
# https://projecteuler.net/problem=47

def trial_division(n, bound=None):
    if n == 1: 
        return 1
        
    for p in [2, 3, 5]:
        if n % p == 0: 
            return p
            
    if bound == None: 
        bound = n
        
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7
    i = 1
    while m <= bound and m*m <= n:
        if n % m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

def prime_factors(n):
    if n == 1:
        return []
        
    factors = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1
            n /= p
        factors.append((p, e))
        
    factors.sort()
    return tuple(factors)

def dpf():
    n = 647
    while True:
        if (len(prime_factors(n)) == 4 and
            len(prime_factors(n+1)) == 4 and
            len(prime_factors(n+2)) == 4 and
            len(prime_factors(n+3)) == 4):
            return n
        n += 1

#
def test():
    if (prime_factors(14) == ((2, 1), (7, 1)) and
        prime_factors(15) == ((3, 1), (5, 1)) and    
        prime_factors(644) == ((2, 2), (7, 1), (23, 1)) and
        prime_factors(645) == ((3, 1), (5, 1), (43, 1)) and
        prime_factors(646) == ((2, 1), (17, 1), (19, 1))):
        return 'Pass'
    else:
        return 'Fail'

def main():
    return dpf()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

