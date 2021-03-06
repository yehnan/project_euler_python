

# Problem 3: Largest prime factor
# https://projecteuler.net/problem=3

#
def prime_gf():
    primes = [2]
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True
    while True:
        p = primes[-1]
        yield p
        while True:
            p += 1
            if is_prime(p):
                primes.append(p)
                break
prime_f = prime_gf()

def lpf(n):
    max = 1
    for i in prime_f:
        if i <= n:
            while n % i == 0:
                n /= i
                max = i
        else:
            break
    return max

#
def test():
    if lpf(13195) == 29:
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    return lpf(600851475143)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

