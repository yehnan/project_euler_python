

# Problem 7: 10001st prime
# https://projecteuler.net/problem=7

#
def primes(n_th):
    primes = [2]
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True
    
    p = primes[-1] + 1
    while len(primes) < n_th:
        if is_prime(p):
            primes.append(p)
        p += 1

    return primes[-1]

#
def is_prime(n):
    if n % 2 == 0: 
        return False
        
    p = 3
    while p < (n//2 + 1):
        if n % p == 0: 
            return False
        p += 2
    return True

def nth_prime(n):
    prime = 2
    p_next = 3
    while n > 1:
        if is_prime(p_next):
            prime = p_next
            n -= 1
        p_next += 2
    return prime

#
def test():
    if primes(6) == 13: #  and nth_prime(6) == 13
        return 'Pass'
    else:
        return 'Fail'
    
def main():
    #return nth_prime(10001)
    return primes(10001)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

