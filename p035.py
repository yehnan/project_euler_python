

# Problem 35: Circular primes
# https://projecteuler.net/problem=35

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes
    
def circulars(n):
    result = []
    s = str(n)
    for i in range(len(s)):
        result.append(int(s[i:] + s[0:i]))
    return result
    
def all_in(iterable, primes):
    for x in iterable:
        if x not in primes:
            return False
    return True
    
def cp(max):
    primes = prime_sieve(max)
    count = 0
    for p in primes:
        cs = circulars(p)
        if all_in(cs, primes):
            count += 1
    return count

#
def test():
    if cp(100) == 13:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return cp(1 * 1000 * 1000)

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

