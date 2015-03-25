

# Problem 41: Pandigital prime
# https://projecteuler.net/problem=41

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
    
from itertools import permutations as perm

def pp():
    n_max = 0
    dcheck = [4, 7]
    for d in dcheck:
        ds = '123456789'[:d]
        for nst in perm(ds):
            n = int(''.join(nst))
            if is_prime(n) and n > n_max:
               n_max = n
    return n_max

#
def test():
    return 'No test'

def main():
    return pp()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        print(test())
    else:
        print(main())

